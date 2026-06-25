# Pull Request: ProcessSmith Agent Platform Architecture

**PR Type:** Technical Architecture + Development Roadmap  
**Date:** June 15, 2026  
**Author:** Jimmy (Research/Architecture)  
**Target:** Programmer/Codex for implementation planning  
**Status:** Ready for Review  

---

## Summary

Proposes a new **three-layer architecture** for ProcessSmith agent deployments combining:
- **Omnigent** (meta-orchestration layer, open-source)
- **OpenClaw** (custom contractor Skills)
- **Hermes** (local LLM for privacy/cost)
- **Brewton Firm Brain** principles (encoded reusable workflows)

This shifts ProcessSmith from "VM packaging" to **"agent orchestration platform for contractors"** with enterprise-grade governance and industry-specific intelligence.

---

## Problem Statement

### Current Gaps

1. **No multi-agent orchestration:** OpenClaw alone can't coordinate multiple agent types (local vs. cloud, code vs. research)
2. **Weak governance:** Basic tool allowlists insufficient for cost control, approval workflows
3. **No collaboration features:** Can't share live agent sessions with team members
4. **Manual delivery:** No encoded "Firm Brain" Skills for repeatable contractor workflows

### Validated Needs (from research)

- Contractors need orchestrated workflows, not single-task agents
- Cost control is critical (SMBs fear runaway bills)
- Privacy matters (local inference for sensitive data)
- Collaboration required (PMs, supers, multiple stakeholders)

---

## Proposed Solution

### Architecture Overview

```
┌─────────────────────────────────────────────────┐
│         Omnigent Meta-Harness Layer            │
│  • Multi-agent composition                      │
│  • Contextual policies (cost, approval gates)   │
│  • Real-time collaboration                      │
│  • Security sandbox                             │
└──────────────┬──────────────────────────────────┘
               │
       ┌───────┴───────┬─────────────┐
       │               │             │
┌──────▼───────┐ ┌────▼─────┐ ┌────▼────────┐
│  OpenClaw    │ │  Claude  │ │  Codex      │
│  + Hermes    │ │  Code    │ │  (optional) │
│  (Local)     │ │  (Cloud) │ │             │
└──────┬───────┘ └────┬─────┘ └─────────────┘
       │               │
┌──────▼───────────────▼──────────────────────────┐
│        ProcessSmith Firm Brain                  │
│  • Discovery Brief Generator                    │
│  • Workflow Audit Scorer                        │
│  • Proposal/SOW Generator                       │
│  • Implementation Backlog Generator             │
└─────────────────────────────────────────────────┘
```

### Key Components

#### 1. Omnigent Integration

**What:** Databricks' open-source meta-harness for agent orchestration

**Why:** 
- Provides enterprise-grade governance (cost caps, approval gates, dynamic policies)
- Real-time collaboration (share sessions, co-drive with teammates)
- Secure sandbox (credential brokering, network interception)
- Multi-agent composition built-in

**Implementation:**
- Install Omnigent server (Docker-based)
- Connect OpenClaw as Omnigent agent (via uniform API)
- Define ProcessSmith-specific policies (YAML config)
- Expose via web UI, mobile, CLI

**References:**
- Omnigent docs: https://omnigent.ai/
- GitHub: https://github.com/omnigent-ai/omnigent
- License: Apache 2.0 (open-source)

#### 2. OpenClaw Custom Skills

**What:** Contractor-specific integrations (Procore, Buildertrend, QuickBooks, etc.)

**Why:** 
- Industry knowledge that generic agents lack
- Control over integration logic
- Ability to run locally (privacy, cost)

**Implementation:**
- Maintain existing OpenClaw skills
- Package as Omnigent-compatible agent
- Add Firm Brain Skills (discovery, audit, proposal)

#### 3. Hermes Local LLM

**What:** Open-source LLMs (Hermes 2/3, Llama, Qwen) running locally via Ollama/llama.cpp

**Why:**
- Sensitive data stays on-premise (privacy)
- Zero API costs for routine tasks (cost)
- Acceptable quality for simple workflows

**Implementation:**
- Install Ollama on client hardware or ProcessSmith hosting
- Configure OpenClaw to use Hermes as default model
- Omnigent policies route complex tasks to Claude/Codex

**Hardware Requirements:**
- Minimum: 16GB RAM
- Recommended: 32GB RAM for comfortable performance
- Optional: GPU for faster inference

#### 4. Firm Brain Skills

**What:** Reusable ProcessSmith workflows encoded as executable Skills

**Why:**
- Compress delivery time (20 hours → 3 hours)
- Consistent quality (no reinventing each time)
- Enables fixed-scope pricing (vs. hourly)

**Priority Skills (Phase 1):**

1. **Discovery Brief Generator**
   - Input: Client intake form + demo transcript
   - Output: Structured discovery brief
   - Agent: Hermes (local, confidential)

2. **Workflow Audit Scorer**
   - Input: Client workflows
   - Output: Impact/ease/risk/data-readiness matrix + audit report
   - Agent: Claude Code (complex analysis) + approval gate

3. **Proposal/SOW Generator**
   - Input: Audit results + package selection
   - Output: Customized SOW (scope, timeline, pricing)
   - Agent: Claude Code + Steve final edit

4. **Implementation Backlog Generator**
   - Input: Approved audit + workflows
   - Output: 30-day sprint backlog
   - Agent: Hermes + Claude Code (hybrid)

---

## Development Phases

### Phase 1: Foundation POC (Weeks 1-2)

**Goal:** Prove Omnigent + OpenClaw + Hermes stack works

**Tasks:**
1. Install Omnigent locally (Docker Compose)
2. Configure OpenClaw as Omnigent agent
3. Set up Hermes (Ollama) backend
4. Build test workflow:
   ```
   Email → Hermes analysis → OpenClaw action → Omnigent approval gate
   ```
5. Test collaboration features (session sharing)
6. Document setup process, issues, limitations

**Acceptance Criteria:**
- [ ] Omnigent orchestrates OpenClaw successfully
- [ ] Hermes responds via OpenClaw within 5 seconds
- [ ] Approval gate works (Steve can review in Omnigent UI)
- [ ] Session sharing functional (teammate can view live)
- [ ] Cost tracking visible in Omnigent dashboard
- [ ] Setup documented (<2 hours for fresh install)

**Deliverables:**
- Working local stack (Omnigent + OpenClaw + Hermes)
- Setup documentation (README.md)
- Test workflow demo (video/screenshots)
- Decision: GO/NO-GO on full integration

---

### Phase 2: Firm Brain Core (Weeks 3-4)

**Goal:** Encode ProcessSmith delivery knowledge as Skills

**Tasks:**
1. Create Firm Brain directory structure:
   ```
   processsmith-firm-brain/
   ├── voice/
   │   ├── writing-style-guide.md
   │   └── anti-slop-rules.md
   ├── offers/
   │   ├── pricing-rules.md
   │   └── icp-scoring-rubric.md
   ├── skills/
   │   ├── discovery-brief-generator/
   │   └── audit-scorer/
   └── playbooks/
       ├── audit-delivery-runbook.md
       └── build-sprint-checklist.md
   ```

2. Build Discovery Brief Generator Skill
   - Parse intake form JSON
   - Extract context, pain points, goals
   - Generate structured brief (markdown)
   - Style: anti-AI-slop rules enforced

3. Build Audit Scorer Skill prototype
   - Input: client workflow descriptions
   - Score: impact (1-5), ease (1-5), risk (1-5), data-readiness (Y/N)
   - Output: prioritized matrix + narrative report
   - Approval gate: Steve reviews before final

**Acceptance Criteria:**
- [ ] Firm Brain structure created and documented
- [ ] Discovery Brief Skill generates usable output
- [ ] Audit Scorer applies scoring rubric correctly
- [ ] Skills follow style guide (no generic LLM patterns)
- [ ] Approval gates enforced (no auto-send to client)

**Deliverables:**
- Firm Brain repository with documentation
- 2 working Skills (discovery, audit)
- Test cases with sample client data
- Performance metrics (time, cost, quality)

---

### Phase 3: Pilot Deployment (Weeks 5-8)

**Goal:** Deploy to 2-3 clients, validate model

**Tasks:**
1. Build Proposal Generator Skill
2. Build Backlog Generator Skill
3. Create deployment package (Docker Compose + docs)
4. Deploy to pilot clients:
   - Option A: Cloud-hosted by ProcessSmith
   - Option B: Client self-hosted (if privacy required)
5. Train clients on agent usage
6. Track metrics:
   - Setup time
   - Support tickets (frequency, resolution time)
   - Usage patterns (daily sessions, task types)
   - Time savings (client-reported)
   - Willingness to pay

**Acceptance Criteria:**
- [ ] Setup takes <2 hours per client
- [ ] <5 support tickets per client in first month
- [ ] Client uses agent 3+ times per week
- [ ] 5+ hours/month time savings reported
- [ ] Client says "I'd pay $400-600/month"

**Deliverables:**
- 4 complete Skills (discovery, audit, proposal, backlog)
- Pilot deployment package (Docker Compose)
- Setup/training documentation
- Client feedback report
- Go/no-go recommendation for Phase 4

---

### Phase 4: Scale Decision (Month 3+)

**Goal:** Productize or pivot based on pilot results

**Evaluate:**
- Gross margin >50% after support costs?
- Can onboard 5+ clients per month?
- Client retention >80% at month 3?

**If GO (3+ criteria met):**
- Invest in polished onboarding (videos, automated setup)
- Build 4-6 more Skills (Procore, QuickBooks, etc.)
- Hire support/delivery help
- Launch marketing campaign

**If NO-GO (<3 criteria met):**
- Pivot to cloud SaaS (drop local deployment)
- OR pivot to services-only (no VM/agent product)
- Document lessons learned

---

## Technical Requirements

### Infrastructure

**Development:**
- Ubuntu 22.04+ or macOS
- Docker Desktop or Docker CE
- 16GB+ RAM (32GB recommended for Hermes)
- 50GB+ free disk space

**Production (per client):**
- Cloud VM: 4 vCPU, 16GB RAM, 50GB SSD
- OR client hardware: 16GB+ RAM, modern CPU
- Network: stable internet for cloud API calls
- Backup: daily snapshots, 30-day retention

### Software Stack

| Component | Version | License | Notes |
|-----------|---------|---------|-------|
| **Omnigent** | v0.x (alpha) | Apache 2.0 | Meta-harness |
| **OpenClaw** | Latest stable | Apache 2.0 | Custom skills |
| **Hermes (Ollama)** | Llama 3.3 9B-27B | Apache 2.0 | Local LLM |
| **Claude API** | Latest | Commercial | Cloud model |
| **Node.js** | v20+ | MIT | For OpenClaw |
| **Python** | 3.11+ | PSF | For Omnigent |
| **Docker** | v24+ | Apache 2.0 | Container runtime |

### Cost Structure (per client/month)

| Item | Cost | Notes |
|------|------|-------|
| Omnigent hosting | $100 | Cloud VM (4 vCPU, 16GB) |
| Hermes | $0-30 | Electricity if 24/7 local |
| Claude Code subscription | $20-150 | Pro → Max |
| API usage (Claude) | $50-200 | Variable by routing |
| Storage/backups | $15 | Logs, sessions |
| **Total** | **$185-495** | |

**Target pricing:** $600-1,200/month → 55-85% gross margin

---

## Risk Assessment

### Technical Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Omnigent alpha instability | Medium | Pin stable version, maintain OpenClaw fallback |
| Hermes performance on low-end hardware | Medium | Offer cloud-hosted default, local as premium |
| Integration complexity (3 platforms) | High | Thorough testing, phased rollout |
| Network latency (local ↔ cloud agents) | Low | Async workflows, local caching |

### Business Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Support burden too high | High | Start cloud-hosted, charge premium ($500+/mo) |
| Client adoption (too complex) | Medium | Abstract complexity, focus on outcomes |
| Databricks competition | Low | SMB market not their focus, move fast |
| Open-source commoditization | Medium | Differentiate on Skills, not hosting |

---

## Success Metrics

### Technical KPIs

- Setup time: <2 hours
- Agent response: <3 seconds (Hermes), <10 seconds (Claude)
- Cost per session: <$5 (routine), <$50 (complex)
- Uptime: >99% (cloud), >95% (local)

### Business KPIs

- Customer acquisition cost: <$500
- Time-to-value: <1 week
- Monthly recurring revenue: $400-700/client
- Gross margin: >60%
- Retention: >80% at 6 months
- NPS: >50

### Delivery KPIs (Brewton model)

- Discovery → proposal: <2 weeks (vs. 4-6 weeks manual)
- Audit delivery: 3-5 hours (vs. 20+ hours)
- Proposal win rate: >40%
- Client time saved: 10+ hours/month
- ROI: 3:1 minimum

---

## Open Questions for Programmer

1. **Omnigent Integration Strategy**
   - Best approach to wrap OpenClaw as Omnigent agent?
   - Use Omnigent's SDK or custom API bridge?
   - Where should policies live (Omnigent config vs. OpenClaw)?

2. **Hermes Configuration**
   - Which model size for ProcessSmith use case (9B, 13B, 27B)?
   - Ollama vs. llama.cpp vs. vLLM for production?
   - GPU required or CPU-only viable?

3. **Firm Brain Skills Architecture**
   - Implement as OpenClaw Skills or separate service?
   - How to version/deploy Skills (git, Docker, other)?
   - Template engine for deliverables (Jinja, Handlebars, custom)?

4. **Deployment Model**
   - Docker Compose sufficient or need Kubernetes?
   - Single-tenant (one VM per client) or multi-tenant?
   - Database requirements (SQLite, Postgres, other)?

5. **Testing Strategy**
   - Unit tests for Skills (how to mock LLM responses)?
   - Integration tests for Omnigent ↔ OpenClaw?
   - Load testing (how many concurrent sessions per VM)?

---

## References

1. **Omnigent Meta-Harness**
   - Blog: https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents
   - Docs: https://omnigent.ai/
   - GitHub: https://github.com/omnigent-ai/omnigent

2. **ProcessSmith Research**
   - VM Package Feasibility Report (2026-06-15)
   - Omnigent Comparison Analysis (2026-06-15)
   - Brewton AI-Fluent Consulting Study (2026-06-14)

3. **OpenClaw Documentation**
   - https://docs.openclaw.ai/

4. **Hermes LLM**
   - Nous Research: https://nousresearch.com/
   - Ollama: https://ollama.ai/

---

## Next Steps

### Immediate (This Week)

1. **Programmer Review:**
   - Read synthesis document (`omnigent-brewton-processsmith-synthesis-2026-06-15.md`)
   - Answer open questions above
   - Propose implementation plan for Phase 1

2. **Steve Decision:**
   - Review architecture proposal
   - Approve/reject/modify scope
   - Green-light Phase 1 POC

3. **Jimmy:**
   - Install Omnigent locally (manual test)
   - Document setup process
   - Provide feedback to Programmer

### Week 2

- Programmer builds Phase 1 POC
- Jimmy tests and documents
- Steve reviews demo
- Team decides: proceed to Phase 2 or pivot

---

## Approval

- [ ] **ProcessSmith:** Architecture approved, proceed to Phase 1
- [ ] **Programmer/Codex:** Implementation plan ready, work can begin
- [ ] **Jimmy (Research):** Documentation complete, ready to support

---

**Document Control:**
- PR ID: PR-2026-06-15-001
- Date: June 15, 2026
- Author: Jimmy (Research/Architecture)
- Status: Awaiting Review
- Next Review: After Phase 1 POC completion
