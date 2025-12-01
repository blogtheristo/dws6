# Dockerfile for Claude Agent Router Service
# Deploys to Google Cloud Run

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Create directories for configs
RUN mkdir -p /app/configs/instances /app/configs/templates

# Environment variables (set in Cloud Run)
# - ANTHROPIC_API_KEY
# - GROQ_API_URL
# - SUPABASE_CONNECTION_STRING

# Expose port 8083
EXPOSE 8083

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import httpx; httpx.get('http://localhost:8083/health')"

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8083"]
