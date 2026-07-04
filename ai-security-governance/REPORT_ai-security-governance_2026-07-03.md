# AI Security & Governance for a Solo Canadian AI-Automation Consultancy

**Date:** 2026-07-03
**Question:** What AI security, data-protection, and AI-governance standards and
regulations should ProcessSmith adopt, and how can they become practical operating
protocols and a client-trust asset?
**Method:** Deep-research harness — 5 parallel search angles, 23 sources fetched,
113 claims extracted, top 25 adversarially verified (3 independent refute-attempt votes
per claim). Claims whose vote pool was cut off by session limits were verified manually
against their primary sources the same day (marked *inline-verified*).
**Status:** Research findings — **not legal advice, and not signed-off policy.**
Operational adoption happens only through the ProcessSmith Security Framework
(`processsmith-systems/docs/security/`), whose public commitments are gated on Steve's
sign-off table and whose paid-client readiness is gated on privacy-lawyer review
(processsmith-systems issue #28). Until those gates close, everything below is research
input to that process, not a compliance position.
**Outcome:** The findings were operationalized as the ProcessSmith Security Framework —
`processsmith-systems/docs/security/` (merged PR #27) — and the `agent-security-standard`
agent skill. This report is the evidence base; the framework is the policy. Update the
framework, not this report, when practice changes.

---

## Bottom line

1. **No AI-specific statute binds ProcessSmith.** Canada's AIDA died with prorogation in
   January 2025 and has no replacement; the EU AI Act's extraterritorial triggers don't
   reach a BC consultancy serving Canadian SMBs, and its headline high-risk deadlines were
   delayed in May 2026 anyway.
2. **Existing Canadian privacy law already covers all of it.** The privacy commissioners'
   joint generative-AI principles apply PIPEDA/provincial law to anyone developing,
   providing, or *using* generative AI — and explicitly name prompt injection as a threat
   organizations must safeguard personal information against. Agent security is privacy
   compliance in Canada, not optional best practice.
3. **The right posture for a solo firm:** comply with PIPEDA/BC PIPA; align to (not
   certify against) NIST AI RMF, OWASP LLM/agentic guidance, and the ISED voluntary code;
   defer ISO 42001 / SOC 2 until procurement demands them; and turn the written standard
   into a client-trust asset, because competitors at this scale answer the data question
   with a shrug.

---

## Verified findings

### Canadian law (what actually binds)

| # | Finding | Verification |
|---|---|---|
| 1 | AIDA (Bill C-27) died on the order paper 2025-01-06 when Parliament prorogued; Canada has no comprehensive federal AI statute as of mid-2026, and reintroduction is not guaranteed. | 3-0 ([Schwartz Reisman Institute](https://srinstitute.utoronto.ca/news/whats-next-for-aida)) |
| 2 | The OPC + all provincial/territorial commissioners issued joint principles applying existing privacy law to generative AI, covering developers, providers, **and organizations using such systems** — a consultancy deploying AI for clients is in the stated audience. | 3-0 ([OPC principles](https://www.priv.gc.ca/en/privacy-topics/technology/artificial-intelligence/gd_principles_ai/)) |
| 3 | Organizations must document their **legal authority** for collection/use/disclosure/deletion of personal information; where consent is the basis it must be valid and meaningful, "as specific as possible," without deceptive design. | 3-0 (OPC principles) |
| 4 | Accountability requires being able to **demonstrate compliance**, including Privacy Impact Assessments and Algorithmic Impact Assessments. | 3-0 (OPC principles) |
| 5 | The safeguards principle **explicitly names prompt injection, model inversion, and jailbreaking** as threats to protect personal information against. | 2-0 (OPC principles) |
| 6 | Canada's ISED **Voluntary Code of Conduct** for advanced generative AI (Sept 2023) defines complementary "developer" and "manager" roles — a firm that deploys/operates AI systems it didn't train is a **manager** — with six principles: accountability, safety, fairness & equity, transparency, human oversight & monitoring, validity & robustness. | 3-0 ([ISED code](https://ised-isde.canada.ca/site/ised/en/voluntary-code-conduct-responsible-development-and-management-advanced-generative-ai-systems)) |

### Recording & automated-calling consent (inline-verified against primary texts)

| # | Finding | Source |
|---|---|---|
| 7 | Recording a customer call requires informing the person, stating the purpose, and obtaining consent; **implied consent** holds if the customer proceeds after clear disclosure. | [OPC call-recording guidance](https://www.priv.gc.ca/en/privacy-topics/surveillance/02_05_d_14/) |
| 8 | Purpose limitation: a recording made for one stated purpose (e.g. reviewing workflow needs) may not be reused for another (marketing, profiling, training). An alternative channel must be offered if the caller objects. | Same |
| 9 | Meaningful consent must emphasize four elements up front: what is collected, who it's shared with, for what purpose, and risk of harm. **Express** consent is required when info is sensitive, the use is outside reasonable expectations, or there's meaningful residual risk of significant harm. | [OPC/OIPC consent guidelines](https://www.priv.gc.ca/en/privacy-topics/business-privacy/collecting-personal-information/consent/gl_omc_201805/) |
| 10 | CRTC: automated-voice (ADAD) **telemarketing** calls require express prior consent. **Even non-solicitation ADAD calls** must open with who the call is on behalf of and its purpose (public-service calls exempt; appointment-reminder-type calls not specifically addressed). | [CRTC Unsolicited Telecommunications Rules, Part IV](https://www.crtc.gc.ca/eng/trules-reglest.htm) |
| 11 | Criminal Code s. 184(1) makes knowingly intercepting a private communication an offence; s. 184(2)(a) exempts interception with "the consent to intercept, express or implied, of the originator ... or of the person intended ... to receive it" — i.e., one-party consent. A participant (or their tool) may lawfully record a conversation they're part of. Criminal legality does not remove PIPEDA's commercial consent duties — both bars apply. | [Criminal Code s. 184](https://laws-lois.justice.gc.ca/eng/acts/c-46/section-184.html) (primary); commentary: [privacylawyer.ca](https://blog.privacylawyer.ca/2025/09/recording-conversations-using-ai.html) |

### EU AI Act (why it doesn't bind, and what changed in 2026)

| # | Finding | Verification |
|---|---|---|
| 12 | Prohibitions + AI-literacy provisions in force since 2025-02-02; GPAI model obligations since 2025-08-02. | 3-0 ([EU AI Act Service Desk timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act)) |
| 13 | Claims that the Annex III high-risk + Article 50 transparency deadlines land 2026-08-02 were **REFUTED (0-3)**: the **Digital Omnibus on AI** (provisional agreement 2026-05-07) delayed key compliance deadlines. Treat any pre-May-2026 timeline summary as stale. | Refuted 0-3; delay per [Global Policy Watch](https://www.globalpolicywatch.com/2026/05/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/) |
| 14 | Extraterritorial reach requires placing AI on the EU market or having system **output used in the EU**. A BC consultancy serving Canadian SMBs, no EU touchpoints, is outside scope. Relevance is as a template ("Brussels effect"), not an obligation. | Two independent legal analyses ([William Fry](https://www.williamfry.com/knowledge/a-practical-guide-to-the-extraterritorial-reach-of-the-ai-act/), [CMS](https://cms.law/en/chl/publication/guide-to-the-eu-ai-act-for-businesses-outside-the-eu)) |

### Agentic-AI security practice (inline-verified against OWASP)

| # | Finding | Source |
|---|---|---|
| 15 | OWASP's 2025 GenAI Top 10 ranks **prompt injection #1** (LLM01), distinguishing direct vs **indirect** (malicious instructions inside content the model ingests — transcripts, emails, web pages). | [OWASP LLM01](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) |
| 16 | OWASP published a **Top 10 for Agentic Applications for 2026** (2025-12-09), peer-reviewed by 100+ practitioners, positioned as a practical starting point. | [OWASP agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) |
| 17 | The OWASP **AI Agent Security Cheat Sheet** catalogs agent-specific risks (prompt injection, tool abuse & privilege escalation, memory poisoning, goal hijacking, excessive autonomy, denial-of-wallet, high-impact action abuse) and prescribes: least-privilege per-tool scoping with allowlists; treating **all external data as untrusted** with sanitization/delimiters; and **separating decision from execution** — the agent proposes, an independent layer validates, humans approve irreversible/financial/admin actions. | [OWASP cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) |
| 18 | NIST AI RMF is free, voluntary, certification-less (Govern/Map/Measure/Manage); NIST publishes an official **crosswalk to ISO/IEC 42001**, so aligning to one substantially covers the other. | [NIST crosswalk PDF](https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf) |

### Market/trust packaging (secondary sources, directional)

- SOC 2 Type II and ISO 27001 are enterprise-procurement credentials; small-business buyers
  don't ask for them, and a solo consultancy shouldn't buy them speculatively.
- Practitioner guidance for small firms converges on: a **one-page AI/data policy** (not a
  40-page binder), a named governance owner, vendor/subprocessor transparency, and asking
  every AI vendor the questions clients will ask you.
- DPAs are a GDPR-world artifact (Art. 28) but the *shape* (what's processed, by whom,
  commitments on deletion/breach) is what SMB clients increasingly expect in plain language.

---

## What was refuted (and why it matters)

The only killed claims were the EU Aug-2026 deadline claims (#13). This is the cautionary
tale of the whole exercise: the most-repeated "fact" in 2025-era coverage was overturned by
a May 2026 legislative event. Any security/compliance claim ProcessSmith makes publicly
should carry a review date, which the framework's semi-annual cadence provides.

## How this became policy

- **Framework:** `processsmith-systems/docs/security/` — SECURITY-FRAMEWORK.md (5 layers +
  go-live gates), agent-security-standard.md (per-build checklist, mandatory injection
  test), ai-data-handling-standard.md (client one-pager, gated on a sign-off table),
  client-training-checklist.md, incident-response.md, learning-path.md. Merged as PR #27
  after two reviewer-agent rounds tightened the publication gates.
- **Skill:** `agent-security-standard` (Claude skill) auto-applies the checklist when
  agents are built or reviewed; the repo doc is canonical.
- **Open gates:** the one-pager's sign-off table (Steve) and privacy-lawyer retention
  (processsmith-systems issue #28) gate paid-client readiness.

## Source register

Primary: EU AI Act Service Desk (EC), OPC generative-AI principles, OPC call-recording
guidance, OPC/OIPC meaningful-consent guidelines, CRTC Unsolicited Telecommunications
Rules, ISED Voluntary Code of Conduct, OWASP GenAI project (LLM01, agentic Top 10, agent
cheat sheet), NIST AI RMF / ISO 42001 crosswalk.
Secondary: Schwartz Reisman Institute (AIDA), William Fry & CMS (extraterritoriality),
Global Policy Watch (Digital Omnibus), privacylawyer.ca (recording), assorted 2026
practitioner guides (SMB compliance packaging).
