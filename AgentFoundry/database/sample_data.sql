-- DWS6 Pilot - Sample Data
-- 5 Nordic Construction Companies for Sales Demo

-- ============================================
-- INSERT CUSTOMERS
-- ============================================

INSERT INTO customers_mvp (customer_id, customer_name, country, status, onboarded_at) VALUES
  ('cust_001_veidekke_no', 'Veidekke Entreprenør AS', 'NO', 'active', NOW() - INTERVAL '60 days'),
  ('cust_002_skanska_se', 'Skanska Sverige AB - Malmö', 'SE', 'active', NOW() - INTERVAL '90 days'),
  ('cust_003_yit_fi', 'YIT Rakennus Oy - Turku', 'FI', 'active', NOW() - INTERVAL '120 days'),
  ('cust_004_ncc_dk', 'NCC Construction Denmark A/S', 'DK', 'active', NOW() - INTERVAL '45 days'),
  ('cust_005_peab_se', 'Peab Asfalt AB - Göteborg', 'SE', 'active', NOW() - INTERVAL '75 days')
ON CONFLICT (customer_id) DO NOTHING;

-- ============================================
-- CUSTOMER 1: Veidekke (Healthy, Low Risk)
-- ============================================

-- Note: In production, these would be inserted by the API after agent analysis
-- For demo, we're pre-populating with expected results

INSERT INTO customer_health_mvp (
  customer_id, customer_name, country,
  health_score, risk_level,
  nps_score, open_tickets, days_since_contact, usage_trend,
  primary_concern, recommended_action,
  agent_response
) VALUES (
  'cust_001_veidekke_no',
  'Veidekke Entreprenør AS',
  'NO',
  92, -- Excellent health
  'Low',
  9, 1, 8, 'Increasing',
  'None - customer is highly engaged and satisfied',
  'Continue quarterly check-ins to maintain relationship',
  '{"health_score": 92, "risk_level": "Low", "analysis": "Promoter with high engagement"}'::jsonb
);

INSERT INTO viability_analysis_mvp (
  customer_id, customer_name,
  setup_hours, monthly_revenue_eur,
  payback_months, gross_margin_percent,
  verdict, reasoning,
  agent_response
) VALUES (
  'cust_001_veidekke_no',
  'Veidekke Entreprenør AS',
  5, 850.00,
  1.4, -- (700 + 400) / 800 = 1.375
  94.1, -- (850 - 50) / 850 = 0.941
  'Approve',
  'Excellent unit economics with 1.4 month payback and 94% margin',
  '{"payback_months": 1.4, "verdict": "Approve", "calculation": "(700+400)/800=1.4"}'::jsonb
);

-- ============================================
-- CUSTOMER 2: Skanska (Medium Risk)
-- ============================================

INSERT INTO customer_health_mvp (
  customer_id, customer_name, country,
  health_score, risk_level,
  nps_score, open_tickets, days_since_contact, usage_trend,
  primary_concern, recommended_action
) VALUES (
  'cust_002_skanska_se',
  'Skanska Sverige AB - Malmö',
  'SE',
  63, -- Moderate health
  'Medium',
  7, 4, 28, 'Stable',
  'Passive NPS score and several open tickets indicate potential dissatisfaction',
  'Schedule check-in call within 7 days to address open tickets and gather feedback'
);

INSERT INTO viability_analysis_mvp (
  customer_id, customer_name,
  setup_hours, monthly_revenue_eur,
  payback_months, gross_margin_percent,
  verdict, reasoning
) VALUES (
  'cust_002_skanska_se',
  'Skanska Sverige AB - Malmö',
  7, 700.00,
  1.9, -- (700 + 560) / 650 = 1.94
  92.9, -- (700 - 50) / 700 = 0.929
  'Approve',
  'Good unit economics at 1.9 months, within 2-month target'
);

-- ============================================
-- CUSTOMER 3: YIT (High Risk - CHURN ALERT!)
-- ============================================

INSERT INTO customer_health_mvp (
  customer_id, customer_name, country,
  health_score, risk_level,
  nps_score, open_tickets, days_since_contact, usage_trend,
  primary_concern, recommended_action
) VALUES (
  'cust_003_yit_fi',
  'YIT Rakennus Oy - Turku',
  'FI',
  38, -- Critical health
  'High',
  5, 8, 52, 'Declining',
  'CRITICAL: Detractor NPS, 8 open tickets, no contact in 52 days, declining usage',
  'URGENT: Immediate CSM intervention required. Schedule call within 24 hours. Prepare retention offer.'
);

INSERT INTO viability_analysis_mvp (
  customer_id, customer_name,
  setup_hours, monthly_revenue_eur,
  payback_months, gross_margin_percent,
  verdict, reasoning
) VALUES (
  'cust_003_yit_fi',
  'YIT Rakennus Oy - Turku',
  9, 650.00,
  2.4, -- (700 + 720) / 600 = 2.37
  92.3, -- (650 - 50) / 650 = 0.923
  'Review',
  'Borderline case at 2.4 months payback. Good margin but longer payback. Monitor closely.'
);

-- ============================================
-- CUSTOMER 4: NCC Denmark (Healthy, Low Risk)
-- ============================================

INSERT INTO customer_health_mvp (
  customer_id, customer_name, country,
  health_score, risk_level,
  nps_score, open_tickets, days_since_contact, usage_trend,
  primary_concern, recommended_action
) VALUES (
  'cust_004_ncc_dk',
  'NCC Construction Denmark A/S',
  'DK',
  90, -- Excellent health
  'Low',
  9, 2, 12, 'Increasing',
  'None - highly engaged promoter with growing usage',
  'Request case study testimonial. Consider upsell opportunity for additional sites.'
);

INSERT INTO viability_analysis_mvp (
  customer_id, customer_name,
  setup_hours, monthly_revenue_eur,
  payback_months, gross_margin_percent,
  verdict, reasoning
) VALUES (
  'cust_004_ncc_dk',
  'NCC Construction Denmark A/S',
  6, 900.00,
  1.4, -- (700 + 480) / 850 = 1.39
  94.4, -- (900 - 50) / 900 = 0.944
  'Approve',
  'Excellent customer with 1.4 month payback and highest monthly revenue in cohort'
);

-- ============================================
-- CUSTOMER 5: Peab (Borderline - Low Risk but Review Viability)
-- ============================================

INSERT INTO customer_health_mvp (
  customer_id, customer_name, country,
  health_score, risk_level,
  nps_score, open_tickets, days_since_contact, usage_trend,
  primary_concern, recommended_action
) VALUES (
  'cust_005_peab_se',
  'Peab Asfalt AB - Göteborg',
  'SE',
  78, -- Good health
  'Low',
  8, 3, 21, 'Stable',
  'Healthy customer but moderate engagement - could improve with proactive outreach',
  'Schedule monthly check-in to ensure continued satisfaction'
);

INSERT INTO viability_analysis_mvp (
  customer_id, customer_name,
  setup_hours, monthly_revenue_eur,
  payback_months, gross_margin_percent,
  verdict, reasoning
) VALUES (
  'cust_005_peab_se',
  'Peab Asfalt AB - Göteborg',
  8, 550.00,
  2.7, -- (700 + 640) / 500 = 2.68
  90.9, -- (550 - 50) / 550 = 0.909
  'Review',
  'Lower revenue customer with 2.7 month payback. Good margin but exceeds 2-month target. Consider pricing adjustment or efficiency improvements.'
);

-- ============================================
-- SAMPLE AGENT USAGE DATA
-- ============================================

-- Simulate some agent invocations
INSERT INTO agent_usage_mvp (
  agent_id, customer_id,
  input_tokens, output_tokens,
  estimated_cost_eur, actual_cost_eur,
  latency_ms, status
) VALUES
  ('customersat-construction-mvp', 'cust_001_veidekke_no', 245, 112, 0.00025, 0.0000, 1240, 'success'),
  ('viability-construction-mvp', 'cust_001_veidekke_no', 198, 89, 0.00020, 0.0000, 980, 'success'),
  ('customersat-construction-mvp', 'cust_002_skanska_se', 251, 118, 0.00026, 0.0000, 1320, 'success'),
  ('viability-construction-mvp', 'cust_002_skanska_se', 203, 94, 0.00021, 0.0000, 1050, 'success'),
  ('customersat-construction-mvp', 'cust_003_yit_fi', 268, 134, 0.00028, 0.0000, 1450, 'success'),
  ('viability-construction-mvp', 'cust_003_yit_fi', 211, 102, 0.00022, 0.0000, 1120, 'success'),
  ('customersat-construction-mvp', 'cust_004_ncc_dk', 242, 108, 0.00025, 0.0000, 1180, 'success'),
  ('viability-construction-mvp', 'cust_004_ncc_dk', 195, 86, 0.00020, 0.0000, 940, 'success'),
  ('customersat-construction-mvp', 'cust_005_peab_se', 247, 115, 0.00025, 0.0000, 1260, 'success'),
  ('viability-construction-mvp', 'cust_005_peab_se', 200, 91, 0.00020, 0.0000, 1000, 'success');

-- ============================================
-- VERIFICATION QUERIES
-- ============================================

-- Uncomment to run after inserting data:

-- SELECT 'Customers' as table_name, COUNT(*) as row_count FROM customers_mvp
-- UNION ALL
-- SELECT 'Customer Health', COUNT(*) FROM customer_health_mvp
-- UNION ALL
-- SELECT 'Viability Analysis', COUNT(*) FROM viability_analysis_mvp
-- UNION ALL
-- SELECT 'Agent Usage', COUNT(*) FROM agent_usage_mvp;

-- -- View summary
-- SELECT * FROM customer_health_summary ORDER BY health_score DESC;
-- SELECT * FROM viability_summary ORDER BY payback_months ASC;
-- SELECT * FROM agent_cost_summary;
