[CmdletBinding()]
param([switch]$Check)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$validator = Join-Path $PSScriptRoot 'Test-ProcessSmithResearchCatalog.ps1'

& pwsh -NoProfile -File $validator -All
if ($LASTEXITCODE -ne 0) { throw 'Catalog validation failed before compilation.' }

. $validator -Library
$discoveredProjects = @(Get-ResearchProjects $root)
$catalogs = @($discoveredProjects | ForEach-Object { Get-Item -LiteralPath (Join-Path $_.directory 'catalog.json') } | Sort-Object FullName)
$tables = [ordered]@{ projects=@(); entities=@(); relations=@(); mentions=@(); tools=@(); claims=@(); price_observations=@(); comparisons=@(); citations=@(); record_sources=@() }
$untraceable = 0
foreach ($file in $catalogs) {
    $catalog = Get-Content -Raw -LiteralPath $file.FullName | ConvertFrom-Json -Depth 100
    $catalogPath = [IO.Path]::GetRelativePath($root, $file.FullName).Replace('\','/')
    $projectDir = Split-Path -Parent $file.FullName
    $project = [ordered]@{}
    foreach ($property in $catalog.project.PSObject.Properties) { $project[$property.Name] = $property.Value }
    $project.catalog_path = $catalogPath
    $project.source_file = [IO.Path]::GetRelativePath($root, (Join-Path $projectDir $catalog.project.source_locator.file)).Replace('\','/')
    $project.source_locator_type = $catalog.project.source_locator.locator_type
    $project.source_locator_value = $catalog.project.source_locator.value
    $tables.projects += [pscustomobject]$project
    foreach ($name in @('entities','relations','mentions','tools','claims','price_observations','comparisons','citations')) {
        foreach ($item in @($catalog.$name)) {
            $row = [ordered]@{}
            foreach ($property in $item.PSObject.Properties) {
                if ($property.Name -notin @('source_locator','source_ids')) { $row[$property.Name] = $property.Value }
            }
            $row.catalog_path = $catalogPath
            $row.source_file = [IO.Path]::GetRelativePath($root, (Join-Path $projectDir $item.source_locator.file)).Replace('\','/')
            $row.source_locator_type = $item.source_locator.locator_type
            $row.source_locator_value = $item.source_locator.value
            $tables[$name] += [pscustomobject]$row
            $recordKey = if ($name -eq 'citations') { "$($item.project_id):$($item.source_id)" } else { $item.record_id }
            [array]$ids = if ($name -eq 'citations') { @($item.source_id) } else { @($item.source_ids) }
            foreach ($sourceId in $ids) { $tables.record_sources += [pscustomobject]@{ record_id=$recordKey; project_id=$item.project_id; source_id=$sourceId; catalog_path=$catalogPath } }
            if (-not $row.source_file -or -not $row.source_locator_type -or -not $row.source_locator_value -or $ids.Count -eq 0) { $untraceable++ }
        }
    }
}

$indexedCount = (Select-String -LiteralPath (Join-Path $root 'index.md') -Pattern '^\|\s*PSR-\d{4}-\d{3}\s*\|').Count
$coverage = if ($indexedCount -eq 0) { 0 } else { [math]::Round(100 * $tables.projects.Count / $indexedCount, 2) }
$stateSummary = $tables.projects | Group-Object catalog_state | Sort-Object Name | ForEach-Object { "$($_.Name)=$($_.Count)" }
Write-Output "BUILD: projects=$($tables.projects.Count) catalogs=$($catalogs.Count) coverage=$coverage%"
Write-Output "BUILD: states $($stateSummary -join ' ')"
Write-Output "BUILD: entities=$($tables.entities.Count) relations=$($tables.relations.Count) mentions=$($tables.mentions.Count) tools=$($tables.tools.Count) claims=$($tables.claims.Count) prices=$($tables.price_observations.Count) comparisons=$($tables.comparisons.Count) citations=$($tables.citations.Count) record_sources=$($tables.record_sources.Count)"
Write-Output "BUILD: untraceable_records=$untraceable"
if ($Check -and ($coverage -ne 100 -or $untraceable -ne 0 -or $tables.projects.Count -ne $catalogs.Count)) { throw 'Build check failed coverage or traceability.' }
Write-Output 'PASS: normalized in-memory build is complete and disposable; no database was written'
