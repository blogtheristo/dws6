# Research Framework: DWS6 Operating Model Study
**Metropolia University Master's Thesis**

---

## 1. Research Design Overview

**Type:** Mixed Methods (Action Research + Case Study)
**Duration:** 6-7 months (aligned with DWS6 MVP → Alpha deployment)
**Setting:** Lifetime Oy's product development process
**Role:** Participant-observer (founder implementing the operating model)

---

## 2. Research Philosophy

### 2.1 Epistemology: Pragmatism

**Why pragmatism fits DWS6:**
- Focus on "what works" rather than pure theory
- Combines quantitative (costs, metrics) and qualitative (customer feedback) data
- Action-oriented: research outputs directly improve the product

**Key principles:**
- Knowledge comes from doing (implementing MVP)
- Multiple perspectives valid (technical, business, customer)
- Results matter more than philosophical purity

### 2.2 Ontology: Critical Realism

**Reality has layers:**
1. **Empirical:** What we observe (cost data, customer NPS)
2. **Actual:** Events that happen (deployments, bugs, customer churn)
3. **Real:** Underlying mechanisms (why free tier strategy works, why edge AI creates moat)

**Applied to DWS6:**
- We measure costs (empirical)
- We track deployments (actual)
- We theorize why hybrid cloud-edge beats cloud-only (real)

---

## 3. Data Collection Methods

### 3.1 Quantitative Data

#### A) Cost Tracking (Daily)
**Source:** Automated cost monitoring dashboard

| Metric | Frequency | Target | Data Source |
|--------|-----------|--------|-------------|
| Daily infrastructure cost | Real-time | €0-12/day | Google Cloud Console, Groq API dashboard |
| Monthly burn rate | Weekly rollup | €0 (MVP), €50-150 (Alpha) | Aggregated billing |
| Startup credits used | Monthly | <10% of $135K total | AWS, Google, Groq credit balance |
| Edge AI savings | Monthly | €27,750/month vs cloud | NVIDIA power usage vs cloud inference costs |

**Collection tool:** Google Sheets with automated imports from Cloud Billing API

#### B) Performance Metrics (Per Agent Invocation)
| Metric | Target | Measurement |
|--------|--------|-------------|
| Response time | <2s (cloud), <100ms (edge) | Application logs |
| Uptime | >99% | Uptime Robot pings |
| Error rate | <1% | Sentry error tracking |
| Token usage | <1,500 tokens/invocation | Groq API response headers |

#### C) Customer Metrics (Weekly)
| Metric | Target | Measurement |
|--------|--------|-------------|
| NPS score | ≥30 | Typeform survey (monthly) |
| Churn rate | 0% (MVP), <5% (Alpha) | Customer database |
| Payback period | ≤2 months | Financial analysis per customer |
| Agent invocations per customer | ≥10/day | Usage logs |

### 3.2 Qualitative Data

#### A) Customer Interviews (Semi-Structured)

**MVP Phase:** Interview all 5 pilot customers
**Timing:** Weeks 1 (onboarding), 2 (mid-pilot), 4 (end)

**Interview Protocol:**

**Onboarding Interview (Week 1):**
1. What manual processes do you hope DWS6 will automate?
2. What's your biggest pain point with current tools (Excel, Jira, etc.)?
3. How do you currently track customer health / project viability?
4. What would make you pay for DWS6 after the free pilot?
5. What concerns do you have about AI making decisions?

**Mid-Pilot Interview (Week 2):**
1. Show me how you've used the agents so far.
2. What surprised you (positively or negatively)?
3. Are the agent recommendations accurate? Give examples.
4. What features are missing that you expected?
5. Would you recommend DWS6 to a peer?

**End-of-Pilot Interview (Week 4):**
1. Did DWS6 save you time? How much (hours/week)?
2. Calculate your payback period based on time saved.
3. What would stop you from becoming a paying customer?
4. If you could change one thing, what would it be?
5. NPS question: On a scale of 0-10, how likely are you to recommend DWS6?

**Data analysis:** Thematic coding in NVivo (or manual coding in Google Sheets)

#### B) Development Logs (Weekly Reflections)

**Format:** Markdown journal in `docs/metropolia/master-thesis/logs/`

**Weekly reflection template:**
```md
# Week N Reflection (YYYY-MM-DD)

## What we built this week
- [List features, bug fixes, deployments]

## What worked
- [Successes, pleasant surprises]

## What didn't work
- [Failures, technical debt created]

## Costs this week
- Actual: €X
- Budget: €Y
- Variance: €Z (explain if >10%)

## Customer feedback highlights
- [Quote 1-2 customer messages]

## Lessons learned
- [What would we do differently?]

## Next week priorities
- [Top 3 tasks]
```

**Analysis:** Identify patterns across weeks (recurring issues, improvement trends)

#### C) GitHub Projects Data (Kanban)

**Automated data extraction:**
- Tasks moved: Backlog → This Week → In Progress → Done
- Cycle time: Time from "In Progress" to "Done"
- Throughput: Tasks completed per week

**Qualitative analysis:**
- Why did some tasks take longer than expected?
- What caused blockers?
- What tasks were abandoned (and why)?

---

## 4. Data Analysis Plan

### 4.1 Quantitative Analysis

#### A) Cost Model Validation

**Hypothesis:** DWS6 can achieve MVP with €0/month operational cost using free tiers.

**Analysis:**
1. Calculate actual daily costs (Dec 2025 - Feb 2026)
2. Compare to budget (€0 target)
3. If variance >10%, investigate root cause (e.g., exceeded free tier limits)
4. Project costs for Alpha (50 customers) and V1 (100+ customers)

**Visualization:**
- Line chart: Daily cost over 90 days (MVP phase)
- Stacked bar chart: Cost breakdown by service (Groq, Cloud Run, Supabase)
- Comparison table: DWS6 vs Rovo (€0 vs €1,400/month)

#### B) Edge AI ROI Validation

**Hypothesis:** NVIDIA Jetson hardware pays for itself in <2 months vs cloud inference.

**Analysis:**
1. Measure cloud inference cost per 1,000 requests (using Groq free tier as baseline)
2. Calculate edge inference cost (hardware amortized over 36 months + electricity)
3. Compare total cost of ownership over 1, 2, 3 years
4. Calculate break-even point

**Formula:**
```
Cloud cost/month = (Requests/month) × (Cost per 1,000 requests)
Edge cost/month = (Hardware cost / 36 months) + (Electricity cost)
Break-even = Hardware cost / (Cloud cost/month - Edge cost/month)
```

**Expected result:** Break-even at 1.95 months (based on preliminary calculations)

#### C) Customer Payback Period

**Hypothesis:** Customers achieve ≤2 month payback.

**Analysis:**
1. Calculate customer investment: (Hardware + Setup fees)
2. Calculate monthly savings: (Manual hours saved) × (Hourly labor cost)
3. Payback = Investment / Monthly savings

**Example (Construction customer):**
- Investment: €2,000 setup fee
- Savings: 20 hours/month × €50/hour = €1,000/month
- Payback: 2.0 months ✓

### 4.2 Qualitative Analysis

#### A) Thematic Coding (Customer Interviews)

**Process:**
1. Transcribe all interviews (or use AI transcription with Whisper)
2. Import into NVivo (or use Google Sheets for manual coding)
3. First cycle coding: Open coding (identify all themes)
4. Second cycle coding: Axial coding (group related themes)
5. Third cycle coding: Selective coding (identify core narrative)

**Expected themes:**
- Trust and risk (AI making decisions)
- Time savings (manual processes automated)
- Compliance (EU regulations)
- Cost sensitivity (SME budgets)
- Feature requests (product roadmap)

**Output:** Theme frequency table + representative quotes for thesis

#### B) Development Log Analysis

**Process:**
1. Review 12 weeks of logs (MVP phase)
2. Tag each entry: Success, Failure, Cost variance, Customer insight, Technical debt
3. Calculate tag frequency (what issues recur?)
4. Identify turning points (when did we solve a major blocker?)

**Output:** Narrative timeline of MVP development with lessons learned

---

## 5. Validity & Reliability

### 5.1 Internal Validity (Are findings accurate?)

**Threats:**
- Researcher bias (I'm the founder, I want DWS6 to succeed)
- Small sample size (5 MVP customers)
- Self-reported data (customer time savings estimates)

**Mitigation:**
- Triangulation: Cross-check customer claims with usage logs
- Peer review: Weekly check-ins with Metropolia supervisor
- Negative case analysis: Actively look for evidence that contradicts hypotheses

### 5.2 External Validity (Are findings generalizable?)

**Threats:**
- Single case study (Lifetime Oy only)
- Industry-specific (construction, manufacturing)
- Geographic limits (Europe only)

**Mitigation:**
- Compare to literature (Lean Startup, Platform Economics)
- Identify transferable principles (free tier strategy, phased deployment)
- Discuss boundary conditions (when does this model NOT work?)

### 5.3 Reliability (Can findings be replicated?)

**Ensuring replicability:**
- Document all methods in detail (this framework)
- Publish data collection tools (interview protocol, cost tracking sheet)
- Share analysis code (if using scripts to process logs)
- Version control (GitHub for all thesis artifacts)

---

## 6. Ethical Considerations

### 6.1 Customer Data Privacy

**Risk:** Customer interviews contain sensitive business data.

**Protection:**
- Anonymize all customer quotes in thesis (use "Customer A", "Customer B")
- Store interview recordings encrypted (password-protected)
- Get signed consent forms (explain data will be used in academic thesis)
- Offer customers option to review thesis before publication

### 6.2 Researcher Positionality

**Disclosure:** I am the founder of Lifetime Oy, implementing the model I'm studying.

**Implications:**
- Bias toward positive results (I want DWS6 to succeed)
- Insider knowledge (deeper understanding, but risk of blind spots)
- Dual role (researcher + practitioner)

**Mitigation:**
- Reflexivity: Journal about my assumptions and biases
- External validation: Supervisor reviews findings for bias
- Negative evidence: Actively report failures and limitations

### 6.3 Intellectual Property

**Issue:** Thesis will contain proprietary DWS6 implementation details.

**Resolution:**
- Lifetime Oy retains IP rights (thesis license: "Proprietary - Lifetime Oy")
- Public thesis version (Metropolia library) will redact sensitive sections
- Full version available only to Metropolia supervisor and examiners

---

## 7. Data Management Plan

### 7.1 Data Storage

| Data Type | Storage Location | Backup | Retention |
|-----------|------------------|--------|-----------|
| Cost tracking | Google Sheets (encrypted) | Daily (Google Drive) | 5 years |
| Customer interviews | Encrypted folder (local + cloud) | Weekly (Google Drive) | 5 years (anonymized) |
| Development logs | GitHub repo (`docs/metropolia/master-thesis/logs/`) | Git version control | Indefinite |
| Performance metrics | Supabase database | Daily snapshots | 5 years |

### 7.2 Data Access

**Access levels:**
- Risto Päärni (researcher): Full access
- Metropolia supervisor: Full access (NDA signed)
- Thesis examiners: Anonymized access (sensitive data redacted)
- Public (Metropolia library): Redacted version only

### 7.3 Data Destruction

**After thesis completion:**
- Customer interview recordings: Delete after 1 year
- Anonymized transcripts: Retain 5 years
- Cost data: Retain 5 years (for tax purposes)
- Code and configs: Retain indefinitely (version controlled)

---

## 8. Quality Criteria (Lincoln & Guba)

| Criterion | Definition | How DWS6 Study Achieves It |
|-----------|------------|----------------------------|
| **Credibility** | Findings are believable | Triangulation (interviews + logs + metrics), Peer review (supervisor) |
| **Transferability** | Findings apply elsewhere | Thick description (detailed operating model docs), Boundary conditions (when model works/doesn't) |
| **Dependability** | Process is stable and consistent | Audit trail (GitHub commits, weekly logs), Documented methods (this framework) |
| **Confirmability** | Findings are shaped by data, not bias | Reflexivity journal, Negative case analysis, Data archived for review |

---

## 9. Timeline Integration

**Aligns with DWS6 roadmap:**

| Thesis Phase | Timeframe | DWS6 Phase | Data Collection |
|--------------|-----------|------------|-----------------|
| Literature review | Month 1-2 | Pre-MVP | Industry reports, competitor analysis |
| Design | Month 3 | MVP prep | Architecture docs, cost model |
| Implementation | Month 4-5 | MVP (5 customers) | Cost data, interviews, logs |
| Analysis | Month 6 | Alpha prep | Thematic coding, cost analysis |
| Writing | Month 6-7 | Alpha launch | Final results, discussion |

---

## 10. Expected Outputs

### 10.1 Thesis Chapters (Academic Output)

1. Theoretical contributions (free tier model, hybrid cloud-edge economics)
2. Empirical findings (cost validation, customer ROI, edge AI savings)
3. Practical framework (operating model template, deployment playbook)

### 10.2 Practical Outputs (Business Use)

1. **Operating Model Canvas** (visual 1-pager for investors)
2. **Cost Calculator** (Google Sheets tool for other startups)
3. **Agent Configuration Library** (YAML templates, open sourced)
4. **Deployment Playbook** (step-by-step guide for Construction, Manufacturing, Energy)

### 10.3 Open Source Contributions

**Planned GitHub releases:**
- `dws6-agent-templates` (YAML configs)
- `groq-router-fastapi` (reusable API service)
- `edge-ai-roi-calculator` (cost comparison tool)

**License:** MIT (technical code) + CC-BY (documentation)

---

**Document Status:** v1.0
**Last Updated:** December 3, 2025
**Next Review:** [TBD - after Metropolia supervisor first meeting]
