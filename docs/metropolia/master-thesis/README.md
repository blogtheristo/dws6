# Metropolia Master's Thesis: DWS6 Operating Model
**Student:** Risto Anton Päärni
**Company:** Lifetime Oy (Firehorse brand)
**Program:** [TBD]
**Timeline:** [TBD - typically 6 months]

---

## Thesis Focus

**Title:** Operating Model of Firehorse Product Manufacturing: A Hybrid AI-Edge Architecture for Climate-Intelligent Industrial Platforms

**Research Question:**
*How can a bootstrapped industrial AI platform achieve product-market fit through a hybrid cloud-edge operating model while maintaining <€400/month operational costs?*

**Approach:** Action Research + Case Study (implementing DWS6 MVP → Alpha phases)

---

## Documents in This Folder

### Core Thesis Documents

1. **[THESIS_OUTLINE.md](THESIS_OUTLINE.md)**
   - Complete thesis structure (8 chapters)
   - Research questions and objectives
   - Theoretical framework (Lean Startup, Platform Economics, Edge Computing)
   - Timeline and milestones
   - Expected contributions

2. **[RESEARCH_FRAMEWORK.md](RESEARCH_FRAMEWORK.md)**
   - Detailed methodology (mixed methods)
   - Data collection protocols (quantitative + qualitative)
   - Analysis plan (cost validation, thematic coding)
   - Validity, reliability, ethics
   - Quality criteria

### Supporting Documents (To Be Created)

3. **data-collection/**
   - `customer-interview-protocol.md` (semi-structured questions)
   - `cost-tracking-template.xlsx` (Google Sheets format)
   - `weekly-log-template.md` (developer reflection format)
   - `performance-metrics-dashboard.md` (monitoring setup)

4. **logs/**
   - `week-01-reflection.md` (weekly dev logs during MVP)
   - `week-02-reflection.md`
   - ... (12 weeks total for MVP phase)

5. **analysis/**
   - `cost-analysis.xlsx` (actual vs budget, edge ROI calculations)
   - `customer-feedback-themes.md` (thematic coding output)
   - `competitor-comparison.md` (DWS6 vs Rovo vs SAP)
   - `kanban-velocity-analysis.md` (GitHub Projects data)

6. **appendices/**
   - `operating-model-canvas.pdf` (visual 1-pager)
   - `agent-config-samples.yaml` (example agent templates)
   - `cost-calculator.xlsx` (reusable tool for other startups)
   - `deployment-playbook.md` (step-by-step guide)

---

## Connection to DWS6 Implementation

**This thesis documents the REAL implementation of DWS6:**

### MVP Phase (Month 1-3) = Thesis Data Collection
- 5 pilot customers → Customer interviews (data source)
- €0 operational cost → Cost model validation (hypothesis)
- 2 agents deployed → Implementation chapter (evidence)
- GitHub Projects → Development velocity analysis (data source)

### Alpha Phase (Month 4-6) = Thesis Analysis
- Scale to 50 customers → Generalizability testing
- €50-150/month costs → Cost model scaling validation
- Rovo option added → Competitive positioning analysis
- Edge AI deployed → ROI validation (€333K/year savings claim)

### Thesis Outputs → Business Artifacts
- Chapter 4 (Operating Model) → Investor pitch deck
- Cost analysis → Fundraising financial projections
- Customer interviews → Product roadmap prioritization
- Lessons learned → Team training and process improvement

---

## Key Theoretical Contributions

### 1. Free-Tier Bootstrap Model
**Gap in literature:** Lean Startup focuses on MVPs but not infrastructure funding strategies.

**DWS6 contribution:** Demonstrates how $135K in startup credits (AWS, Google, Groq) can fund 6+ years of operations, eliminating need for seed funding before product-market fit.

**Validation:** Track actual credit usage vs runway (target: <10% used by end of MVP).

### 2. Hybrid Cloud-Edge Economics
**Gap in literature:** Edge computing papers focus on latency, not total cost of ownership (TCO) for startups.

**DWS6 contribution:** Proves NVIDIA Jetson hardware (€1,084/site) beats cloud inference (€555/month/site) with 1.95-month payback.

**Validation:** Compare actual edge vs cloud costs over 12 months (V1 phase).

### 3. Phased Trust-Building in High-Risk AI
**Gap in literature:** AI adoption models don't address regulatory industries (construction, manufacturing).

**DWS6 contribution:** 3-phase deployment (Silent → Advisor → Autonomous) de-risks AI in industries where errors have legal/safety consequences.

**Validation:** Measure customer trust scores (surveys) and churn rates across phases.

---

## Practical Outputs for Lifetime Oy

### Immediate Business Use
1. **Investor Pitch Deck**
   - Use Chapter 4 (Operating Model) as technical slides
   - Use cost analysis for financial projections
   - Use customer quotes for social proof

2. **Product Roadmap**
   - Customer interview themes → Feature prioritization
   - Competitor analysis → Differentiation strategy
   - Kanban velocity → Sprint planning

3. **Marketing Materials**
   - Operating Model Canvas → Website explainer graphic
   - Edge AI ROI → Sales collateral for enterprise customers
   - Deployment Playbook → Onboarding documentation

### Long-Term Strategic Value
1. **Open Source Contributions**
   - Agent configuration library (attract developer community)
   - Cost calculator tool (thought leadership, inbound leads)
   - Deployment playbook (establish DWS6 as industry standard)

2. **Replication Template**
   - Other industries (logistics, agriculture, energy) can use same model
   - Partner onboarding (show construction playbook, adapt to their vertical)
   - Franchise model (license operating model to regional partners)

---

## Timeline Alignment

| Month | Thesis Activity | DWS6 Milestone | Deliverable |
|-------|-----------------|----------------|-------------|
| **1-2** | Literature review, competitor analysis | MVP prep, infrastructure deployment | Chapter 2 (Theory), Chapter 3 (Current State) |
| **3** | Design operating model | Agent development (Customer Sat, Viability) | Chapter 4 (Operating Model Design) |
| **4-5** | Data collection (MVP phase) | 5 pilot customers onboarded | Chapter 5 (Implementation) |
| **6** | Data analysis | Alpha prep (scale to 20-50 customers) | Chapter 6 (Results & Analysis) |
| **7** | Writing, revisions | Alpha launch | Chapters 7-8 (Discussion, Conclusions) |

**Defense:** Month 8 (coincides with Alpha results available for validation)

---

## Success Criteria

### Thesis (Academic)
- ✅ Approved by Metropolia supervisor
- ✅ Grade: 4-5 (out of 5)
- ✅ Contribution to theory (3 gaps filled)
- ✅ Practical applicability (replicable model)

### DWS6 (Business)
- ✅ MVP deployed at €0/month operational cost
- ✅ 5 customers with 0 churn
- ✅ Customer payback ≤2 months proven
- ✅ Investor pitch successful (€150K SAFE raised)

### Open Source (Community)
- ✅ Agent templates downloaded 100+ times
- ✅ Cost calculator used by 10+ startups
- ✅ Deployment playbook cited in industry blogs

---

## How to Use This Folder

### For Risto (Researcher)
1. **Weekly:** Add logs to `logs/week-XX-reflection.md`
2. **Monthly:** Update `analysis/cost-analysis.xlsx` with actual costs
3. **After customer interviews:** Code themes in `analysis/customer-feedback-themes.md`
4. **Continuously:** Commit all changes to GitHub (audit trail)

### For Metropolia Supervisor
1. **Start here:** Read `THESIS_OUTLINE.md` (10-min overview)
2. **Methodology review:** Read `RESEARCH_FRAMEWORK.md` (30-min deep dive)
3. **Progress tracking:** Check `logs/` folder weekly
4. **Quality assurance:** Review `analysis/` before thesis writing

### For Lifetime Oy Team
1. **Understand the research:** Read `THESIS_OUTLINE.md` (sections 1-4)
2. **Contribute data:** Add customer feedback to shared Slack channel (I'll code it)
3. **Business outputs:** Check `appendices/` for reusable tools (cost calculator, playbook)
4. **Investor materials:** Use thesis findings for pitch deck (coordinate with Risto)

---

## Contact & Collaboration

**Student/Researcher:** Risto Anton Päärni
**Email:** risto@lifetime.fi
**LinkedIn:** [linkedin.com/in/ristopaarni](https://linkedin.com/in/ristopaarni)
**GitHub:** [github.com/blogtheristo/dws6](https://github.com/blogtheristo/dws6)
**Branch:** `claude/agents-setup-01Tw8Mj3rg96N2Hiy5VdhRCF`

**Metropolia Supervisor:** [TBD - awaiting assignment]

**Collaboration opportunities:**
- Co-authorship on academic papers (edge AI economics, free tier strategy)
- Guest lectures (Metropolia ICT/Business programs)
- Open source community (agent templates, cost calculator)

---

**Next Steps:**
1. ☐ Meet with Metropolia supervisor (finalize scope and timeline)
2. ☐ Set up data collection tools (cost dashboard, interview forms)
3. ☐ Begin MVP implementation (December 2025)
4. ☐ Start weekly reflection logs

---

**Last Updated:** December 3, 2025
**Document Version:** 1.0
**Status:** Draft (awaiting supervisor approval)
