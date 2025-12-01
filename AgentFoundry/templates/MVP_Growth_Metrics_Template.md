# MVP Growth Metrics - Google Sheets Template

**Use this for manual tracking during MVP phase (5-20 customers)**

---

## Setup Instructions

1. Create new Google Sheet: "DWS IQ - Growth Metrics"
2. Create 4 sheets (tabs) as shown below
3. Update weekly (15 minutes)
4. Export to PowerPoint for investor presentations

---

## Sheet 1: Customer Master List

| Customer ID | Company Name | Start Date | Status | MRR (€) | Vertical | Payback (mo) | Churn Risk | Last Updated |
|-------------|--------------|------------|--------|---------|----------|--------------|------------|--------------|
| cust_001 | Demo Construction Ltd | 2025-12-01 | Active | 2000 | Construction | 1.8 | Low | 2025-12-01 |
| cust_002 | Acme Builders Oy | 2025-12-01 | Active | 2000 | Construction | 1.9 | High | 2025-12-01 |
| cust_003 | BuildCo Ltd | 2025-12-01 | Active | 2000 | Construction | 1.9 | Medium | 2025-12-01 |
| cust_004 | Nordic Builders AB | 2025-12-08 | Active | 1500 | Construction | 2.1 | Low | 2025-12-08 |
| cust_005 | SitePro Construction | 2025-12-08 | Active | 2500 | Construction | 1.8 | Low | 2025-12-08 |

**Formulas:**
- Cell B1: Total Active Customers: `=COUNTIF(D:D,"Active")`
- Cell B2: Total MRR: `=SUMIF(D:D,"Active",E:E)`
- Cell B3: Average MRR: `=B2/B1`
- Cell B4: Avg Payback: `=AVERAGE(G2:G100)`

---

## Sheet 2: Monthly Growth

| Month | MRR (€) | ARR (€) | Customers | New | Churned | Growth % | ARPU (€) | Notes |
|-------|---------|---------|-----------|-----|---------|----------|----------|-------|
| Dec 2025 | 10000 | 120000 | 5 | 5 | 0 | - | 2000 | MVP launch - 5 pilot customers |
| Jan 2026 | 18000 | 216000 | 9 | 4 | 0 | 80% | 2000 | Added 4 customers week 5-8 |
| Feb 2026 | 28000 | 336000 | 14 | 5 | 0 | 56% | 2000 | Post-seed funding received |
| Mar 2026 | 42000 | 504000 | 21 | 7 | 0 | 50% | 2000 | Accelerating growth |

**Formulas:**
- ARR: `=B2*12`
- Growth %: `=(B3-B2)/B2`
- ARPU: `=B2/D2`

**Chart:** Create line chart showing MRR growth over time

---

## Sheet 3: Investor Snapshot (LIVE)

### Key Metrics (Auto-Updated)

| Metric | Value | Formula | Target | Status |
|--------|-------|---------|--------|--------|
| **Revenue** | | | | |
| MRR | €10,000 | =Monthly!B2 | - | - |
| ARR | €120,000 | =MRR*12 | - | - |
| ARPU | €2,000 | =MRR/Customers | €2,000+ | ✅ |
| MRR Growth (MoM) | - | =(This month - Last)/Last | 20%+ | - |
| | | | | |
| **Customers** | | | | |
| Total Active | 5 | =COUNTIF(Master!D:D,"Active") | 5 | ✅ |
| New This Month | 5 | =Monthly!E2 | - | - |
| Churned | 0 | =Monthly!F2 | <10% | ✅ |
| Churn Rate | 0% | =Churned/Total*100 | <5% | ✅ |
| | | | | |
| **Unit Economics** | | | | |
| Avg Payback | 1.9 months | =AVERAGE(Master!G:G) | ≤2.0 | ✅ |
| Gross Margin | 94% | =Fixed (from Viability Agent) | ≥60% | ✅ |
| CAC | €500 | =Marketing Spend / New Customers | <€1,000 | ✅ |
| LTV | €48,000 | =ARPU*24 months | - | - |
| LTV/CAC | 96x | =LTV/CAC | >3x | ✅ |
| | | | | |
| **Efficiency** | | | | |
| CAC Payback | 0.25 months | =CAC/(ARPU*Margin) | <12 | ✅ |
| Magic Number | - | =(New MRR this Q / Sales spend last Q) | >0.75 | - |
| Burn Rate | €5,000/mo | =Fixed | - | - |
| Runway | 30 months | =Cash / Burn | >12 | ✅ |

### Status Indicators
- ✅ Green: On target
- ⚠️ Yellow: Close to threshold
- ❌ Red: Below target

---

## Sheet 4: Weekly Investor Update (Template)

Copy this template and fill in each Monday:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DWS IQ - Weekly Update
Week of: [DATE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 METRICS
Revenue:
- MRR: €[X] ([+/-Y]% vs last week)
- ARR: €[X]
- ARPU: €[X]

Customers:
- Total: [X] active
- New: [X] this week
- Churned: [X]
- Pipeline: [X] in trials

🎯 HIGHLIGHTS
- [Major achievement 1]
- [Major achievement 2]
- [Customer win/story]

⚠️ CHALLENGES
- [Blocker 1 + mitigation plan]
- [Risk 2 + mitigation plan]

📈 NEXT WEEK
- [Goal 1]
- [Goal 2]
- [Milestone]

💰 FINANCIAL
- Cash: €[X]
- Burn: €[X]/month
- Runway: [X] months

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Sample Filled Template (Week 1)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DWS IQ - Weekly Update
Week of: December 1, 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 METRICS
Revenue:
- MRR: €10,000 (new baseline)
- ARR: €120,000
- ARPU: €2,000

Customers:
- Total: 5 active pilot customers
- New: 5 this week (onboarding complete)
- Churned: 0
- Pipeline: 3 warm leads

🎯 HIGHLIGHTS
- ✅ Deployed 2 AI agents (Customer Sat + Viability)
- ✅ All 5 pilot customers approved (payback <2 months)
- ✅ Identified 1 at-risk customer early (Acme Builders)
- ✅ CSM intervention prevented potential churn

⚠️ CHALLENGES
- Nordic Builders payback 2.1 months (over 2.0 target)
  → Mitigation: Review setup process efficiency
- Need to build demo site for investor meetings
  → Timeline: Complete by Dec 8

📈 NEXT WEEK
- Deploy weekly automated health reports to Slack
- Onboard 2 additional pilot customers
- Prepare investor pitch deck with MVP results
- Schedule investor demo calls

💰 FINANCIAL
- Cash: €25,000 (bootstrapped)
- Burn: €5,000/month (founders + infra)
- Runway: 5 months
- Seeking: €150K SAFE @ €3.8M cap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Dashboard Visualization (Optional)

**If you want to impress investors, add charts:**

### Chart 1: MRR Growth
- Type: Line chart
- X-axis: Month
- Y-axis: MRR (€)
- Data: Monthly Growth sheet columns A and B

### Chart 2: Customer Count
- Type: Bar chart
- X-axis: Month
- Y-axis: Customers
- Data: Monthly Growth sheet columns A and D

### Chart 3: Unit Economics
- Type: Gauge chart
- Metrics: Payback (target: 2.0), Gross Margin (target: 60%), LTV/CAC (target: 3x)

---

## Automation (Optional - Post-Seed)

### When you have 20+ customers, automate with:

**1. Stripe → Google Sheets**
Use Zapier (free tier: 100 tasks/month):
- Trigger: New Stripe subscription
- Action: Add row to "Customer Master List"

**2. Supabase → Google Sheets**
Use Apps Script:
```javascript
function updateMetrics() {
  // Fetch from Supabase API
  var response = UrlFetchApp.fetch('https://xxx.supabase.co/rest/v1/customers');
  var data = JSON.parse(response.getContentText());

  // Write to sheet
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Customer Master List');
  // ... update logic
}
```

**3. Weekly Slack Report**
Use Apps Script + Slack webhook:
```javascript
function sendWeeklyUpdate() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Investor Snapshot');
  var mrr = sheet.getRange('B2').getValue();

  var payload = {
    "text": "📊 Weekly Metrics: MRR €" + mrr
  };

  UrlFetchApp.fetch(SLACK_WEBHOOK_URL, {
    method: 'post',
    payload: JSON.stringify(payload)
  });
}
```

---

## Export to PowerPoint (For Investor Deck)

**Slide 1: Key Metrics**
1. Copy "Investor Snapshot" table
2. Paste as image in PowerPoint
3. Add title: "30-Day MVP Results"

**Slide 2: Growth Chart**
1. Copy MRR Growth chart
2. Paste in PowerPoint
3. Add annotation: "80% MoM growth rate"

**Slide 3: Customer Health**
1. Screenshot of "Customer Master List"
2. Highlight: "5/5 customers meet payback criteria"

---

## Weekly Maintenance (15 minutes)

**Monday Morning Ritual:**

1. **Update Customer Master List** (5 min)
   - Add new customers
   - Update status (Active/Churned)
   - Update MRR if changes
   - Update churn risk from Customer Sat Agent

2. **Update Monthly Growth** (3 min)
   - If new month, add new row
   - Copy formulas down

3. **Review Investor Snapshot** (2 min)
   - Check all green checkmarks
   - Flag any yellow/red warnings
   - Take screenshot for records

4. **Send Weekly Update** (5 min)
   - Copy template from Sheet 4
   - Fill in current numbers
   - Email to investors/advisors

**Total: 15 minutes**

---

## When to Graduate to Growth Tracker Agent

**Triggers (any one):**
- ✅ 20+ customers (updating takes >30 min/week)
- ✅ Multiple verticals (need segmented analytics)
- ✅ Board meetings (need polished reports)
- ✅ Series A prep (investors expect automation)

**At that point, deploy the Growth Tracker Agent from the full system.**

---

## Example: Investor Meeting Prep (5 minutes)

**Before meeting, open this Google Sheet and show:**

1. **Tab 1 (Customer Master List):**
   "Here are our 5 pilot customers. All active, zero churn."

2. **Tab 3 (Investor Snapshot):**
   "All green checkmarks. 1.9 month payback, 94% gross margin."

3. **Tab 2 (Monthly Growth - Chart):**
   "MRR growing 80% month-over-month."

4. **Tab 4 (Weekly Update):**
   "This is what I send investors every Monday. Takes 5 minutes."

**Investor sees:**
- ✅ Organized and data-driven
- ✅ Tracking right metrics
- ✅ Hitting targets
- ✅ Transparent communication

**Cost:** €0, 15 min/week

---

## Summary

**For MVP (5-20 customers):**
- ✅ Use this Google Sheets template
- ✅ 15 minutes/week to maintain
- ✅ €0 cost
- ✅ Sufficient for investor due diligence

**For Scale (20+ customers):**
- ✅ Deploy Growth Tracker Agent
- ✅ Automate weekly reports
- ✅ Real-time dashboard

**Don't over-engineer during MVP. Keep it simple.**
