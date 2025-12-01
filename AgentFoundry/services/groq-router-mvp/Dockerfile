# Dockerfile for Groq Agent Router - MVP
# Optimized for minimal cost on Google Cloud Run

FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Create directories for configs
RUN mkdir -p /app/configs/mvp

# Copy MVP agent configs
COPY ../../configs/mvp/*.yaml /app/configs/mvp/

# Environment variables (set in Cloud Run deployment)
# - GROQ_API_KEY
# - MVP_GOOGLE_SHEET_ID
# - SLACK_WEBHOOK_URL

# Expose port
EXPOSE 8083

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import httpx; httpx.get('http://localhost:8083/health')"

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8083"]
