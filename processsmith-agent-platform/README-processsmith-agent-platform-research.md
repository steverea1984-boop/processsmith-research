# ProcessSmith Agent Platform Research Package

**Date:** June 15, 2026  
**Research Lead:** Jimmy (OpenClaw)  
**Status:** Ready for Review & Development  

---

## Overview

This research package synthesizes three investigation streams into a unified **ProcessSmith Agent Platform Architecture** proposal:

1. **Technical Feasibility** - VM package deployment options
2. **Omnigent Meta-Harness** - Databricks' agent orchestration layer
3. **Brewton AI-Fluent Model** - Operating system redesign principles

**Key Recommendation:** Build ProcessSmith as an **Omnigent-powered platform** combining enterprise orchestration with contractor-specific "Firm Brain" Skills.

---

## Documents in This Package

### 1. ProcessSmith Client VM Options Report
**File:** `processsmith-client-vm-options-2026-06-15.md`

**Summary:** Comprehensive technical and business analysis of deploying AI agents to contractor clients via VM/container packages.

**Key Findings:**
- ✅ Technically feasible (OpenClaw + Hermes + Claude Code)
- ⚠️ Business viability conditional on support burden, client adoption
- Recommended: Cloud-hosted Docker container as MVP

**Sections:**
1. Component Clarification (Hermes, Claude Code, OpenClaw)
2. VM Platform Options (VirtualBox, VMware, Docker)
3. Delivery Models (standalone, cloud, hybrid)
4. Security & Compliance
5. Cost Structure Analysis
6. Integration Architecture
7. Competitive Landscape
8. ProcessSmith Business Fit
9. Risks & Open Questions
10. Recommendations (phased validation approach)

---

### 2. Omnigent vs ProcessSmith Comparison
**File:** `omnigent-processsmith-comparison-2026-06-15.md`

**Summary:** Comparative analysis of Databricks' Omnigent meta-harness vs. original ProcessSmith VM approach.

**Key Insight:** Omnigent is not a competitor—it's a potential foundation for ProcessSmith.

**Key Differences:**
- **Omnigent:** Meta-orchestration layer (multi-agent, enterprise governance)
- **ProcessSmith VM:** Single-agent runtime environment
- **Opportunity:** Build "Omnigent for Contractors" with industry-specific Skills

**Sections:**
1. What is Omnigent?
2. How Omnigent Compares to ProcessSmith VM
3. Key Differences (abstraction, philosophy, collaboration, governance)
4. How Omnigent Fits ProcessSmith Business Model
5. Opportunities (workflow builder, skills marketplace, managed hosting)
6. Risks & Considerations
7. Recommendations (4-week pilot, decision criteria)

---

### 3. Omnigent + Brewton + ProcessSmith Synthesis
**File:** `omnigent-brewton-processsmith-synthesis-2026-06-15.md`

**Summary:** Unified architecture proposal combining Omnigent orchestration, Brewton's "Firm Brain" principles, and ProcessSmith contractor domain expertise.

**Proposed Stack:**
```
[Omnigent Meta-Harness] ← Orchestration + governance
    ↓
[OpenClaw + Hermes + Claude Code] ← Agent fleet
    ↓
[ProcessSmith Firm Brain Skills] ← Contractor intelligence
```

**Key Components:**
- **Omnigent:** Multi-agent orchestration, policies, collaboration
- **OpenClaw:** Custom contractor integrations (Procore, Buildertrend)
- **Hermes:** Local LLM for privacy/cost
- **Firm Brain:** Reusable delivery Skills (discovery, audit, proposal)

**Sections:**
1. Three-Layer Architecture
2. Mapping Brewton's Loop to ProcessSmith
3. Improvements Over Current ProcessSmith
4. Cost & Feasibility Analysis
5. Development Roadmap (4 phases, 12 weeks)
6. Risk Mitigation
7. Success Metrics
8. Comparison to Alternatives

---

### 4. Development Pull Request
**File:** `PR-omnigent-processsmith-platform.md`

**Summary:** Technical specification and development roadmap for Programmer/Codex to implement ProcessSmith Agent Platform.

**Status:** Ready for Programmer review and implementation planning

**Contents:**
- Problem statement
- Proposed solution (detailed architecture)
- Development phases (Foundation → Firm Brain → Pilot → Scale)
- Technical requirements (infrastructure, stack, costs)
- Risk assessment
- Success metrics
- Open questions for Programmer
- Next steps

**Phase 1 Deliverables (Weeks 1-2):**
- Working Omnigent + OpenClaw + Hermes stack
- Test workflow (email → analysis → action → approval)
- Setup documentation
- GO/NO-GO decision

---

## Key Recommendations Summary

### Architecture Decision

**Adopt layered stack:**
1. **Omnigent** (orchestration) - Open-source, enterprise-grade
2. **OpenClaw** (custom skills) - Contractor-specific integrations
3. **Hermes** (local LLM) - Privacy + cost optimization
4. **Firm Brain Skills** (intelligence) - Encoded delivery workflows

### Business Model Shift

**From:** "VM packaging + agent runtime"  
**To:** "Omnigent-powered contractor workflow orchestration"

**Value Proposition:**
> "We orchestrate a whole team of AI agents (Claude Code, Codex, custom) to handle your contractor workflows—with built-in collaboration, approval gates, and cost controls. It's like having an AI project manager that never sleeps."

### Pricing Strategy

**Fixed-scope packages** (not hourly):
- Discovery Brief: $500
- Workflow Audit: $3,500
- Build Sprint: $7,500
- Ongoing Retainer: $600-1,200/month

### Development Approach

**Phased validation (avoid big upfront bet):**

**Phase 1 (2 weeks):** Prove stack works (Omnigent + OpenClaw + Hermes)  
**Phase 2 (2 weeks):** Build core Firm Brain Skills  
**Phase 3 (4 weeks):** Pilot with 2-3 clients  
**Phase 4 (ongoing):** Scale or pivot based on data  

---

## Success Criteria

### Technical

- [ ] Setup time <2 hours
- [ ] Agent response <3 seconds (Hermes), <10 seconds (Claude)
- [ ] Cost per session <$5 (routine), <$50 (complex)
- [ ] >99% uptime (cloud-hosted)

### Business

- [ ] Gross margin >60%
- [ ] Client retention >80% at 6 months
- [ ] Can onboard 5+ clients/month
- [ ] NPS >50

### Delivery

- [ ] Discovery → proposal <2 weeks
- [ ] Audit delivery 3-5 hours (vs. 20+ manual)
- [ ] Proposal win rate >40%
- [ ] Client ROI 3:1 minimum

---

## Next Actions

### This Week

1. **Steve:** Review synthesis + PR, approve Phase 1 POC
2. **Programmer:** Read PR, answer open questions, propose implementation plan
3. **Jimmy:** Install Omnigent locally, document setup

### Week 2

4. **Programmer:** Build Phase 1 POC (Omnigent + OpenClaw + Hermes)
5. **Jimmy:** Test, document issues, validate setup process
6. **Steve:** Review demo
7. **Team:** Decide GO/NO-GO for Phase 2

---

## References

### External Resources

- **Omnigent:** https://omnigent.ai/ | https://github.com/omnigent-ai/omnigent
- **OpenClaw:** https://docs.openclaw.ai/
- **Hermes/Ollama:** https://ollama.ai/ | https://nousresearch.com/
- **Brewton Article:** (reference in previous analysis)

### Internal Documents

- Markdown source documents in this folder
- Markdown sources in `team/research/`
- Related: ProcessSmith SOP wiki in ClickUp

---

## Questions?

**For architecture/research questions:** Jimmy  
**For business/strategy questions:** Steve  
**For implementation questions:** Programmer (after PR review)

---

**Package Version:** 1.0  
**Date:** June 15, 2026  
**Status:** Ready for Review & Development  
