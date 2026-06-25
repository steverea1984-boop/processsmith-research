# BIMLOGiQ Demo Research Brief

Source: summarized demo notes from 2026-06-03. Raw meeting artifacts and recording links are intentionally excluded from this public research repo.

## Meeting summary
- Demo purpose: BIMLOGiQ showed Revit automation tools for a mechanical contractor workflow.
- Context: mid-sized MEP/mechanical contractor with multi-office Revit users.
- Primary pain: MEP detailing/documentation time, especially tagging and dimensioning for piping, plumbing, medical gas, and large institutional projects.
- Smart Annotation: automates Revit tagging/dimensioning with configurable rules, collision/overlap avoidance, background/server processing, batch processing, and red-highlight QA for imperfect placements.
- Limitation: dimensioning appears strongest for simple/regular drawings; no chain dimensions were identified in the demo notes; complex drawings still need manual review.
- BIMLOGiQ Argus beta: natural-language assistant for generating/saving reusable C# Revit commands, command libraries, team sharing, and admin governance.
- Spooling angle: Argus could potentially automate view creation, sheet placement, and annotation around spooling workflows.
- Demo example: compared air terminals in mechanical model against louvers in architectural link; identified missing louvers/highlighted terminals, with a noted beta selection bug.

## Research links
- BIMLOGiQ Smart Annotation product page: https://bimlogiq.com/product/smart-annotation
- Smart Annotation docs/introduction: https://bimlogiq.com/docs/smart-annotation/docs/smart-annotation-introduction
- Tagging using Smart Annotation docs: https://bimlogiq.com/docs/copilot/docs/tagging-smart-annotation
- BIMLOGiQ command customization article: https://bimlogiq.com/docs/articles/mastering-command-customization
- Autodesk BIMLOGiQ partner page: https://www.autodesk.com/integrations/partner/bimlogiq

## Project relevance
This demo is directly aligned with the MEP BIM Automation project. It should be evaluated as both:
1. A potential off-the-shelf tool for immediate annotation/detailing productivity.
2. A benchmark for our Codex/Revit/MEP automation strategy: Smart Annotation covers annotation automation; Argus/Copilot overlaps with natural-language reusable Revit command generation.

## Evaluation questions
- Does Smart Annotation handle real pipe/duct/plumbing/fabrication views well enough to reduce detailing hours?
- Can rules be standardized and shared across the team/templates?
- Can it tag fabrication parts and linked models reliably in production models?
- What data leaves the machine/cloud processing path? Where is model/view data processed?
- Does Argus store generated C# commands in a controlled library with approval/publishing gates?
- Can generated commands be exported/versioned/reviewed outside BIMLOGiQ?
- How does Argus compare with Codex/Claude Code + pyRevit/C# for custom internal tools?
- What is licensing/pricing for 25–30 Revit users?
