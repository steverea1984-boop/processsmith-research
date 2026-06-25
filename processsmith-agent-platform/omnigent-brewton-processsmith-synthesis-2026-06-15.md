# ProcessSmith Agent Platform Architecture: Synthesis & Development Roadmap

**Date:** June 15, 2026  
**Prepared by:** Jimmy (OpenClaw Research)  
**Version:** 1.0  
**Context:** Combines Omnigent meta-harness analysis + Brewton AI-fluent consulting model

---

## Executive Summary

This document synthesizes three research streams:
1. **ProcessSmith VM Package feasibility** (original technical analysis)
2. **Omnigent meta-harness** (Databricks' agent orchestration layer)
3. **Brewton's AI-fluent consulting model** (operating system redesign)

### Key Recommendation

**Build ProcessSmith as an Omnigent-powered "Firm Brain" for contractors:**

- **Foundation:** Omnigent meta-harness (orchestration + governance)
- **Agents:** OpenClaw (custom skills) + Claude Code (coding) + Hermes (local/private)
- **Intelligence Layer:** Reusable Skills that encode contractor workflows
- **Delivery Model:** Brewton-style research → judgment → execution → output loops

This combines enterprise-grade orchestration (Omnigent) with industry-specific intelligence (ProcessSmith Skills) and privacy-conscious local compute (Hermes).

---

## The Three-Layer Architecture

### Layer 1: Omnigent Meta-Harness (Orchestration)

**What it provides:**
- Multi-agent composition (OpenClaw + Claude Code + Codex working together)
- Contextual policies (cost caps, approval gates, dynamic state tracking)
- Real-time collaboration (shared sessions, co-driving)
- Security sandbox (credential brokering, network interception)

**Why it's the right foundation:**
- Open-source (Apache 2.0), not vendor lock-in
- Enterprise-grade governance that SMBs actually need (cost control, approval flows)
- Collaboration features contractors will use (share session with PM/super)
- Let Databricks maintain the hard orchestration problems

### Layer 2: Agent Fleet (Execution)

**Three complementary agents:**

1. **OpenClaw (Custom Contractor Skills)**
   - Procore/Buildertrend integrations
   - Industry-specific workflows (RFI tracking, change orders, schedule updates)
   - Memory/context for client projects
   - Local execution when privacy matters

2. **Hermes (Local LLM - Privacy/Cost)**
   - Routine tasks (email triage, report generation)
   - Sensitive data stays on-premise
   - Zero API costs for simple workflows
   - 9B-27B models on commodity hardware

3. **Claude Code (Cloud Power - Complex Tasks)**
   - Heavy lifting (contract analysis, complex SOPs, code generation)
   - Better quality for sophisticated reasoning
   - Omnigent routes expensive tasks here only when needed

**Routing Logic (via Omnigent policies):**
```yaml
# Simple/sensitive → Hermes (local)
- trigger: task.sensitivity == "high" OR task.complexity == "low"
  agent: openClaw_hermes

# Complex/public → Claude Code (cloud)
- trigger: task.complexity == "high" AND cost_budget_remaining > $10
  agent: claude_code
  
# Collaborative → Share session
- trigger: user_invites_teammate
  action: omnigent_share_session
```

### Layer 3: Firm Brain (Intelligence)

**Brewton's insight:** The gain isn't from "using AI tools"—it's from encoding repeatable workflows as executable Skills.

**ProcessSmith Firm Brain Components:**

1. **Voice & Standards**
   - Deliverable templates (audit reports, SOPs, proposals)
   - Writing style guide (anti-AI-slop rules)
   - Safety/approval policy (when to require human judgment)

2. **Pricing & Offer Rules**
   - ICP scoring (construction niche, size, tech-readiness)
   - Package matching (Audit → Build Sprint → Ongoing)
   - Pricing calculator (fixed-scope, not hourly)

3. **Reusable Workflow Skills**
   - Discovery Brief Generator
   - Workflow Audit Scorer (impact/ease/risk/data-readiness)
   - Proposal/SOW Generator
   - 30-Day Implementation Backlog Generator

4. **Delivery Playbooks**
   - Week-by-week audit runbook
   - Build sprint checklist
   - Handoff/training script

---

## Mapping Brewton's Loop to ProcessSmith

Brewton's consulting loop:
> **Research/Intelligence (Perplexity) → Human Judgment → Execution (Claude) → Client Output**

ProcessSmith implementation:

| Stage | Brewton | ProcessSmith (Omnigent-Powered) |
|-------|---------|--------------------------------|
| **Intelligence** | Perplexity search | OpenClaw (Hermes) + web research<br>Market/prospect monitoring |
| **Capture** | Meeting transcript | Client intake form + demo notes<br>Email/SMS ingestion |
| **Analysis** | Framework match (ICP, JTBD, Five Forces) | Workflow Audit Scorer Skill<br>Impact/ease/risk matrix |
| **Human Gate** | Consultant review | Steve/Jimmy approval via Omnigent policy |
| **Execution** | Claude drafts deliverable | Claude Code (complex) OR Hermes (routine)<br>Coordinated via Omnigent |
| **Output** | Polished proposal/report | Audit report + SOW + implementation backlog<br>PDF artifacts to Drive |

---

## Key Improvements Over Current ProcessSmith

### What's Already Strong

✅ Clear first offer (AI Workflow Audit + Build Sprint)  
✅ Practical SMB positioning  
✅ One-workflow scope control  
✅ Drive as file cabinet, ClickUp as CRM  
✅ Audit template with scoring rubric  
✅ Human approval points  

### What Needs Building

#### 1. Firm Brain Asset Library

**Current state:** Templates in Drive, scattered runbooks, no single source of truth

**Target state:** Structured Firm Brain in ProcessSmith workspace

```
processsmith-firm-brain/
├── voice/
│   ├── writing-style-guide.md
│   ├── deliverable-templates/
│   └── anti-slop-rules.md
├── offers/
│   ├── pricing-rules.md
│   ├── package-definitions.md
│   └── icp-scoring-rubric.md
├── skills/
│   ├── discovery-brief-generator/
│   ├── audit-scorer/
│   ├── proposal-generator/
│   └── backlog-generator/
└── playbooks/
    ├── audit-delivery-runbook.md
    ├── build-sprint-checklist.md
    └── client-handoff-script.md
```

#### 2. Reusable Delivery Skills (4 Priority Skills)

**Skill 1: Discovery Brief Generator**
- Input: Client intake form + demo transcript
- Output: Structured discovery brief (context, pain points, goals, constraints)
- Agent: Hermes (local) → preserves client confidentiality

**Skill 2: Workflow Audit Scorer**
- Input: Client workflows (email, docs, interviews)
- Process: Score each workflow on impact/ease/risk/data-readiness matrix
- Output: Prioritized opportunity list + audit report
- Agent: Claude Code (complex analysis) → Steve approval gate

**Skill 3: Proposal/SOW Generator**
- Input: Audit results + package selection (Audit only vs. Build Sprint)
- Output: Customized SOW with scope, timeline, pricing, deliverables
- Agent: Claude Code → Steve final edit

**Skill 4: Implementation Backlog Generator**
- Input: Approved audit + chosen workflows
- Output: 30-day sprint backlog (week-by-week breakdown, milestones, acceptance criteria)
- Agent: Hermes (routine structuring) + Claude Code (complex workflows)

#### 3. Discovery-to-Proposal Automation Lane

**Current gap:** Manual handoff between intake → audit → proposal

**Target state:** Omnigent-orchestrated pipeline with approval gates

```
[Prospect Inquiry]
    ↓
[Discovery Brief Skill] (Hermes)
    ↓
[Steve: Accept/Reject/Clarify]
    ↓ (if accepted)
[Audit Kickoff]
    ↓
[Audit Scorer Skill] (Claude Code)
    ↓
[Steve: Review Findings]
    ↓
[Proposal Generator Skill] (Claude Code)
    ↓
[Steve: Final Edit & Send]
    ↓
[Client Receives SOW]
```

**Omnigent benefits here:**
- Each stage is a session (shareable, auditable)
- Cost tracking per stage ($5 discovery, $30 audit, $15 proposal)
- Approval gates enforce quality control
- Teammates (future ProcessSmith staff) can co-drive sessions

#### 4. Pricing Shift: Fixed-Scope Productized

**Current:** Ad-hoc estimation, ~$950 validation pricing

**Brewton's principle:** If AI compresses 20 hours → 3 hours, hourly pricing punishes the business.

**Target:** Fixed-scope packages with clear deliverables

| Package | Deliverables | Price | Notes |
|---------|-------------|-------|-------|
| **Discovery Brief** | Context doc + opportunity list | $500 | Qualify leads, weed out bad fits |
| **Workflow Audit** | Full audit report + prioritized matrix | $3,500 | Current core offer |
| **Build Sprint** | SOW + implementation backlog + handoff | $7,500 | Add-on after audit |
| **Ongoing Retainer** | Monthly optimization + support | $1,200/mo | Post-implementation |

**Firm Brain encodes rules:**
- Discovery required before audit (qualify first)
- Audit + Build Sprint bundle discount: $10,000 (vs. $11,000 separate)
- Retainer requires completed Build Sprint (no unbounded support)

---

## Cost & Feasibility Analysis

### Infrastructure Costs (per client deployment)

| Component | Monthly Cost | Notes |
|-----------|-------------|-------|
| **Omnigent hosting** | $100 | Cloud VM (4 vCPU, 16GB RAM) |
| **Hermes (client hardware)** | $0-30 | Electricity if 24/7 local |
| **Claude Code subscription** | $20-150 | Pro → Max based on usage |
| **API costs (Claude/OpenAI)** | $50-200 | Variable by task routing |
| **Storage/backups** | $15 | Logs, session history |
| **Total per client** | **$185-495/mo** | |

**Gross margin at $1,200/month retainer:** 60-85%

### Development Effort Estimate

| Task | Effort | Priority |
|------|--------|----------|
| **Omnigent local install + proof-of-concept** | 8-12 hours | P0 (this week) |
| **OpenClaw → Omnigent integration** | 16-24 hours | P0 (week 2) |
| **Hermes local LLM setup + routing** | 8-12 hours | P1 (week 3) |
| **Discovery Brief Skill** | 12-16 hours | P1 (week 3-4) |
| **Audit Scorer Skill** | 20-30 hours | P1 (week 4-5) |
| **Proposal Generator Skill** | 16-20 hours | P2 (week 6) |
| **Backlog Generator Skill** | 12-16 hours | P2 (week 7) |
| **Firm Brain documentation** | 16-24 hours | P1 (ongoing) |
| **Total** | **~108-154 hours** | ~3-4 weeks full-time |

---

## Development Roadmap

### Phase 1: Foundation (Weeks 1-2)

**Goal:** Prove Omnigent + OpenClaw + Hermes stack works

**Tasks:**
1. Install Omnigent locally
2. Connect OpenClaw as Omnigent agent
3. Set up Hermes (Ollama) as local LLM backend
4. Build test workflow: Email → Hermes analysis → OpenClaw action → Omnigent approval gate
5. Document setup process, pain points, limitations

**Success Criteria:**
- Omnigent orchestrates OpenClaw + Hermes successfully
- Approval gate works (Steve can review/approve in Omnigent UI)
- Session sharing works (teammate can view live session)
- Cost tracking visible in Omnigent dashboard

### Phase 2: Firm Brain Core (Weeks 3-4)

**Goal:** Encode ProcessSmith delivery knowledge as Skills

**Tasks:**
1. Create Firm Brain directory structure
2. Document voice/style guide (anti-AI-slop rules)
3. Define package pricing rules + ICP scoring
4. Build Discovery Brief Generator Skill
5. Build Audit Scorer Skill prototype

**Success Criteria:**
- Discovery Brief Skill generates usable output from intake form
- Audit Scorer applies impact/ease/risk matrix correctly
- Skills follow style guide (no LLM slop)
- Approval gates require Steve review before final output

### Phase 3: Pilot Deployment (Weeks 5-8)

**Goal:** Deploy to 2-3 friendly clients, validate model

**Tasks:**
1. Build Proposal Generator Skill
2. Build Backlog Generator Skill
3. Package Omnigent + OpenClaw + Hermes as Docker Compose stack
4. Deploy to pilot clients (local OR cloud-hosted based on preference)
5. Track: setup time, support tickets, usage patterns, client feedback

**Success Criteria:**
- Setup takes <2 hours with docs
- <5 support tickets per client in first month
- Client uses agent 3+ times per week
- Clear 5+ hours/month time savings reported
- Willingness to pay $400-600/month post-pilot

### Phase 4: Scale Decision (Month 3)

**Goal:** Go/no-go on full productization

**Evaluate:**
- Is gross margin >50% after support costs?
- Can ProcessSmith onboard 5+ clients per month?
- Is client retention >80% at month 3?

**If GO:**
- Invest in polished onboarding (videos, automated setup)
- Build 4-6 more industry-specific Skills (Procore, QuickBooks, etc.)
- Hire support/delivery help

**If NO-GO:**
- Pivot to simpler cloud SaaS (hosted Omnigent, no local deployment)
- OR pivot to services-only (forget VM package, focus on consulting)

---

## Risk Mitigation

### Risk 1: Omnigent Alpha Instability

**Risk:** Omnigent is v0.x, breaking changes likely

**Mitigation:**
- Pin to stable Omnigent version for production
- Contribute to open-source (build influence on roadmap)
- Maintain OpenClaw fallback path (can drop Omnigent if needed)

### Risk 2: Complexity Overwhelms SMBs

**Risk:** Omnigent + OpenClaw + Hermes stack too complex for contractors to understand

**Mitigation:**
- Offer **managed hosting** as default (ProcessSmith runs infrastructure)
- Position local deployment as "premium privacy option" (higher price, lower volume)
- Abstract complexity: clients see "ProcessSmith Agent," not "Omnigent meta-harness"

### Risk 3: Support Burden Kills Margins

**Risk:** Heterogeneous client environments create endless support tickets

**Mitigation:**
- Start with **cloud-hosted only** (ProcessSmith controls environment)
- Build comprehensive docs + video tutorials
- Charge $500+/month minimum to cover 5-8 hours/month support
- Add premium tier ($700/month) with priority support

### Risk 4: Databricks Competes Directly

**Risk:** Databricks launches "Omnigent for Construction" offering

**Mitigation:**
- SMB contractors aren't Databricks' market (too small, not enough data)
- Build ProcessSmith brand + client base quickly (land grab)
- Differentiate on support + customization, not just hosting

---

## Comparison to Alternatives

### Alternative 1: Pure OpenClaw (No Omnigent)

**Pros:** Simpler stack, mature platform, lower learning curve  
**Cons:** No multi-agent orchestration, weaker governance, no collaboration features

**Verdict:** Good for MVP, but limits growth potential (no team collaboration, cost tracking)

### Alternative 2: Pure Omnigent (No OpenClaw)

**Pros:** Enterprise-grade, Databricks support, best collaboration  
**Cons:** Less customization, no contractor-specific Skills out-of-box

**Verdict:** Hard to differentiate without custom Skills (becomes "generic Omnigent hosting")

### Alternative 3: OpenClaw + Omnigent (Recommended)

**Pros:** Best of both worlds—custom Skills + enterprise orchestration  
**Cons:** Most complex to build, two platforms to maintain

**Verdict:** Worth complexity if it enables premium pricing + team collaboration

---

## Success Metrics

### Technical Metrics

- Setup time: <2 hours from zero to working agent
- Agent response latency: <3 seconds for routine tasks (Hermes)
- Cost per client session: <$5 for routine, <$50 for complex
- Uptime: >99% (cloud-hosted), >95% (client-hosted)

### Business Metrics

- Client acquisition cost: <$500 (organic, referrals)
- Time-to-value: <1 week from signup to first automation win
- Monthly recurring revenue: $400-700 per client
- Gross margin: >60% after support costs
- Client retention: >80% at 6 months
- Net Promoter Score: >50

### Delivery Metrics (Brewton-style)

- Discovery → Audit → Proposal cycle time: <2 weeks (vs. 4-6 weeks manual)
- Audit delivery time: 3-5 hours (AI-assisted) vs. 20+ hours (manual)
- Proposal win rate: >40% (qualified leads only)
- Time saved per client: 10+ hours/month
- Client ROI: 3:1 minimum (saves $3 for every $1 spent)

---

## Conclusion

**The Opportunity:**

ProcessSmith can become **"Omnigent for Contractors"**—taking enterprise-grade agent orchestration and making it accessible to SMB construction firms through:

1. **Industry-specific Intelligence** (Firm Brain Skills)
2. **Privacy-conscious Architecture** (Hermes local + cloud when needed)
3. **Managed Delivery** (ProcessSmith handles complexity)

**The Strategy:**

- Build on Omnigent (don't reinvent orchestration)
- Leverage OpenClaw (custom contractor Skills)
- Add Hermes (local inference for privacy/cost)
- Encode Brewton principles (discovery → judgment → execution loops)
- Validate with pilots before scaling

**The Bet:**

Contractors need more than "ChatGPT access"—they need **orchestrated multi-agent workflows** with governance, collaboration, and industry knowledge. ProcessSmith is positioned to deliver this.

**Next Action:**

Install Omnigent + OpenClaw + Hermes locally this week. Build one end-to-end workflow (email → analysis → action → approval). Decide: Is this better than pure OpenClaw?

---

## Appendices

### A. Reference Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│         Omnigent Meta-Harness Layer            │
│  (Orchestration, Policies, Collaboration)       │
└──────────────┬──────────────────────────────────┘
               │
       ┌───────┴───────┬─────────────┐
       │               │             │
┌──────▼───────┐ ┌────▼─────┐ ┌────▼────────┐
│  OpenClaw    │ │  Claude  │ │  Codex      │
│  + Hermes    │ │  Code    │ │  (OpenAI)   │
│  (Local)     │ │  (Cloud) │ │  (Cloud)    │
└──────┬───────┘ └────┬─────┘ └────┬────────┘
       │               │             │
┌──────▼───────────────▼─────────────▼────────┐
│        Contractor Workflows                  │
│  • Procore sync  • Email triage             │
│  • RFI tracking  • Contract analysis        │
│  • Reports       • Schedule updates         │
└──────────────────────────────────────────────┘
```

### B. Sample Omnigent Policy for Contractors

```yaml
policies:
  # Cost control
  - name: daily_spending_cap
    trigger: daily_llm_cost > $50
    action: pause_and_notify
    message: "Agent has spent $50 today. Continue?"
    
  # Approval gates
  - name: require_approval_for_client_sends
    trigger: action.type == "send_email" AND recipient.domain != "processsmith.com"
    action: require_approval
    message: "Agent wants to send email to client. Review draft?"
    
  # Privacy protection
  - name: local_only_for_sensitive
    trigger: data.contains_pii == true
    agent: openClaw_hermes
    reason: "PII detected, routing to local agent"
    
  # Intelligent routing
  - name: use_claude_for_complex
    trigger: task.complexity_score > 7 AND cost_budget_remaining > $10
    agent: claude_code
    reason: "Complex task, using cloud model"
```

### C. Firm Brain Skill Template

```markdown
# Skill: [Name]

## Purpose
[One-sentence description of what this Skill does]

## Input Requirements
- [Input 1]: [Description]
- [Input 2]: [Description]

## Process Steps
1. [Step 1]
2. [Step 2]
3. [Human approval gate]
4. [Step 3]

## Output Format
[Exact structure of deliverable]

## Agent Routing
- Primary: [Agent name + reason]
- Fallback: [Alternative agent if primary fails]

## Quality Checklist
- [ ] Follows ProcessSmith voice/style guide
- [ ] No AI slop patterns (check anti-slop-rules.md)
- [ ] All client-specific fields populated
- [ ] Approval gate enforced before final output

## Example Usage
\`\`\`
omnigent run skill:discovery-brief-generator --input intake-form.json
\`\`\`
```

---

**Document Control:**
- Version: 1.0
- Date: June 15, 2026
- Author: Jimmy (OpenClaw Research)
- References: 
  - ProcessSmith Client VM Options Report (2026-06-15)
  - Omnigent vs ProcessSmith Comparison (2026-06-15)
  - Brewton AI-Fluent Consulting Analysis (2026-06-14)
- Next Review: After Phase 1 POC completion (2 weeks)
- Distribution: ProcessSmith research archive
