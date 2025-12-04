-- DWS6 Pilot - Supabase Database Schema
-- MVP Tables for Customer Health and Viability Analysis
-- Region: EU Central (Frankfurt) for GDPR compliance

-- Enable pgvector extension for future semantic search
CREATE EXTENSION IF NOT EXISTS vector;

-- ============================================
-- TABLE 1: Customer Health Analysis
-- ============================================

CREATE TABLE IF NOT EXISTS customer_health_mvp (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  
  -- Customer Info
  customer_id TEXT NOT NULL,
  customer_name TEXT NOT NULL,
  country TEXT, -- NO, SE, FI, DK
  
  -- Health Metrics
  health_score INT CHECK (health_score >= 0 AND health_score <= 100),
  risk_level TEXT CHECK (risk_level IN ('Low', 'Medium', 'High')),
  
  -- Supporting Data
  nps_score INT CHECK (nps_score >= 0 AND nps_score <= 10),
  open_tickets INT DEFAULT 0,
  days_since_contact INT DEFAULT 0,
  usage_trend TEXT CHECK (usage_trend IN ('Increasing', 'Stable', 'Declining')),
  
  -- Analysis Results
  primary_concern TEXT,
  recommended_action TEXT,
  agent_response JSONB, -- Full AI response for auditing
  
  -- Metadata
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for fast queries
CREATE INDEX idx_customer_health_customer_id ON customer_health_mvp(customer_id);
CREATE INDEX idx_customer_health_risk_level ON customer_health_mvp(risk_level);
CREATE INDEX idx_customer_health_created_at ON customer_health_mvp(created_at DESC);
CREATE INDEX idx_customer_health_country ON customer_health_mvp(country);

-- ============================================
-- TABLE 2: Viability Analysis
-- ============================================

CREATE TABLE IF NOT EXISTS viability_analysis_mvp (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  
  -- Customer Info
  customer_id TEXT NOT NULL,
  customer_name TEXT NOT NULL,
  
  -- Input Parameters
  hardware_cost_eur DECIMAL(10,2) DEFAULT 700.00,
  setup_hours INT NOT NULL,
  setup_cost_eur DECIMAL(10,2) GENERATED ALWAYS AS (setup_hours * 80) STORED,
  monthly_revenue_eur DECIMAL(10,2) NOT NULL,
  monthly_cogs_eur DECIMAL(10,2) DEFAULT 50.00,
  
  -- Calculated Metrics
  total_upfront_cost_eur DECIMAL(10,2) GENERATED ALWAYS AS (hardware_cost_eur + (setup_hours * 80)) STORED,
  monthly_gross_profit_eur DECIMAL(10,2) GENERATED ALWAYS AS (monthly_revenue_eur - 50.00) STORED,
  payback_months DECIMAL(4,2),
  gross_margin_percent DECIMAL(5,2),
  
  -- Verdict
  verdict TEXT CHECK (verdict IN ('Approve', 'Review', 'Reject')),
  reasoning TEXT,
  agent_response JSONB, -- Full AI response
  
  -- Metadata
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_viability_customer_id ON viability_analysis_mvp(customer_id);
CREATE INDEX idx_viability_verdict ON viability_analysis_mvp(verdict);
CREATE INDEX idx_viability_payback ON viability_analysis_mvp(payback_months);
CREATE INDEX idx_viability_created_at ON viability_analysis_mvp(created_at DESC);

-- ============================================
-- TABLE 3: Agent Usage Tracking
-- ============================================

CREATE TABLE IF NOT EXISTS agent_usage_mvp (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  
  -- Agent Info
  agent_id TEXT NOT NULL,
  customer_id TEXT,
  
  -- Usage Metrics
  input_tokens INT DEFAULT 0,
  output_tokens INT DEFAULT 0,
  total_tokens INT GENERATED ALWAYS AS (input_tokens + output_tokens) STORED,
  
  -- Cost Tracking
  estimated_cost_eur DECIMAL(10,4) DEFAULT 0.0000,
  actual_cost_eur DECIMAL(10,4) DEFAULT 0.0000, -- €0 if using free credits
  
  -- Performance
  latency_ms INT,
  
  -- Status
  status TEXT CHECK (status IN ('success', 'error', 'timeout')),
  error_message TEXT,
  
  -- Metadata
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_agent_usage_agent_id ON agent_usage_mvp(agent_id);
CREATE INDEX idx_agent_usage_customer_id ON agent_usage_mvp(customer_id);
CREATE INDEX idx_agent_usage_created_at ON agent_usage_mvp(created_at DESC);

-- ============================================
-- TABLE 4: Customers Master List (Optional)
-- ============================================

CREATE TABLE IF NOT EXISTS customers_mvp (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  
  customer_id TEXT UNIQUE NOT NULL,
  customer_name TEXT NOT NULL,
  country TEXT,
  
  -- Contact Info
  contact_person TEXT,
  contact_email TEXT,
  
  -- Status
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'churned', 'paused')),
  
  -- Dates
  onboarded_at TIMESTAMPTZ,
  churned_at TIMESTAMPTZ,
  
  -- Metadata
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_customers_customer_id ON customers_mvp(customer_id);
CREATE INDEX idx_customers_status ON customers_mvp(status);
CREATE INDEX idx_customers_country ON customers_mvp(country);

-- ============================================
-- VIEWS FOR REPORTING
-- ============================================

-- Customer Health Summary View
CREATE OR REPLACE VIEW customer_health_summary AS
SELECT 
  c.customer_name,
  c.country,
  ch.health_score,
  ch.risk_level,
  ch.nps_score,
  ch.open_tickets,
  ch.days_since_contact,
  ch.primary_concern,
  ch.recommended_action,
  ch.created_at as last_analysis
FROM customer_health_mvp ch
LEFT JOIN customers_mvp c ON ch.customer_id = c.customer_id
WHERE ch.created_at IN (
  SELECT MAX(created_at)
  FROM customer_health_mvp ch2
  WHERE ch2.customer_id = ch.customer_id
);

-- Viability Summary View
CREATE OR REPLACE VIEW viability_summary AS
SELECT 
  c.customer_name,
  c.country,
  v.monthly_revenue_eur,
  v.setup_hours,
  v.total_upfront_cost_eur,
  v.monthly_gross_profit_eur,
  v.payback_months,
  v.gross_margin_percent,
  v.verdict,
  v.created_at as last_analysis
FROM viability_analysis_mvp v
LEFT JOIN customers_mvp c ON v.customer_id = c.customer_id
WHERE v.created_at IN (
  SELECT MAX(created_at)
  FROM viability_analysis_mvp v2
  WHERE v2.customer_id = v.customer_id
);

-- Agent Cost Summary View
CREATE OR REPLACE VIEW agent_cost_summary AS
SELECT 
  agent_id,
  COUNT(*) as total_invocations,
  SUM(total_tokens) as total_tokens_used,
  SUM(estimated_cost_eur) as total_estimated_cost,
  SUM(actual_cost_eur) as total_actual_cost,
  AVG(latency_ms) as avg_latency_ms,
  COUNT(CASE WHEN status = 'success' THEN 1 END) as success_count,
  COUNT(CASE WHEN status = 'error' THEN 1 END) as error_count
FROM agent_usage_mvp
GROUP BY agent_id;

-- ============================================
-- ROW LEVEL SECURITY (RLS)
-- Enable for multi-tenancy in production
-- ============================================

-- Enable RLS on all tables
ALTER TABLE customer_health_mvp ENABLE ROW LEVEL SECURITY;
ALTER TABLE viability_analysis_mvp ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_usage_mvp ENABLE ROW LEVEL SECURITY;
ALTER TABLE customers_mvp ENABLE ROW LEVEL SECURITY;

-- For MVP, allow all authenticated users to read
-- In production, you'd restrict by organization_id

CREATE POLICY "Allow all for authenticated users" ON customer_health_mvp
  FOR ALL USING (auth.role() = 'authenticated');

CREATE POLICY "Allow all for authenticated users" ON viability_analysis_mvp
  FOR ALL USING (auth.role() = 'authenticated');

CREATE POLICY "Allow all for authenticated users" ON agent_usage_mvp
  FOR ALL USING (auth.role() = 'authenticated');

CREATE POLICY "Allow all for authenticated users" ON customers_mvp
  FOR ALL USING (auth.role() = 'authenticated');

-- ============================================
-- FUNCTIONS FOR ANALYTICS
-- ============================================

-- Function to get customer health trend over time
CREATE OR REPLACE FUNCTION get_customer_health_trend(p_customer_id TEXT, p_days INT DEFAULT 30)
RETURNS TABLE (
  date DATE,
  health_score INT,
  risk_level TEXT,
  nps_score INT
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    DATE(created_at) as date,
    customer_health_mvp.health_score,
    customer_health_mvp.risk_level,
    customer_health_mvp.nps_score
  FROM customer_health_mvp
  WHERE customer_id = p_customer_id
    AND created_at >= NOW() - (p_days || ' days')::INTERVAL
  ORDER BY created_at DESC;
END;
$$ LANGUAGE plpgsql;

-- ============================================
-- SAMPLE QUERIES FOR TESTING
-- ============================================

-- Query 1: Get all high-risk customers
-- SELECT * FROM customer_health_summary WHERE risk_level = 'High';

-- Query 2: Get all customers with payback > 2 months
-- SELECT * FROM viability_summary WHERE payback_months > 2.0;

-- Query 3: Get total agent costs
-- SELECT * FROM agent_cost_summary;

-- Query 4: Get health trend for specific customer
-- SELECT * FROM get_customer_health_trend('cust_003_yit_fi', 30);

-- ============================================
-- COMMENTS
-- ============================================

COMMENT ON TABLE customer_health_mvp IS 'Stores customer health analysis from Customer Satisfaction Agent';
COMMENT ON TABLE viability_analysis_mvp IS 'Stores viability calculations from Viability Agent';
COMMENT ON TABLE agent_usage_mvp IS 'Tracks agent usage, tokens, and costs for monitoring';
COMMENT ON TABLE customers_mvp IS 'Master list of pilot customers';

COMMENT ON VIEW customer_health_summary IS 'Latest health analysis for each customer';
COMMENT ON VIEW viability_summary IS 'Latest viability analysis for each customer';
COMMENT ON VIEW agent_cost_summary IS 'Aggregated cost metrics per agent';
