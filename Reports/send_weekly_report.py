#!/usr/bin/env python3
"""
Weekly Report Email Automation
Sends bilingual reports to risto.paarni2024@lifetime.fi
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import glob

def send_weekly_report():
    """Send weekly reports in English and Finnish"""

    # Email configuration
    sender_email = os.getenv("SMTP_SENDER", "noreply@dws6.com")
    sender_password = os.getenv("SMTP_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))

    # Recipients: Support multiple emails from env var or file
    recipients_env = os.getenv("REPORT_RECIPIENTS")

    if recipients_env:
        # From environment variable (comma-separated)
        recipients = [email.strip() for email in recipients_env.split(',')]
    else:
        # From file (one email per line)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        recipients_file = os.path.join(script_dir, "recipients.txt")

        if os.path.exists(recipients_file):
            with open(recipients_file, 'r') as f:
                recipients = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        else:
            # Default recipient if no list configured
            recipients = ["risto.paarni2024@lifetime.fi"]

    if not recipients:
        print("❌ No recipients configured")
        return False

    print(f"📧 Sending to {len(recipients)} recipient(s)")

    # Get latest reports (support both from repo root and Reports/ directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    en_pattern = os.path.join(script_dir, "en/WEEKLY_REPORT_W*.pdf")
    fi_pattern = os.path.join(script_dir, "fi/WEEKLY_REPORT_W*.pdf")

    en_reports = sorted(glob.glob(en_pattern), reverse=True)
    fi_reports = sorted(glob.glob(fi_pattern), reverse=True)

    if not en_reports or not fi_reports:
        print("❌ No PDF reports found")
        print("💡 Run 'python generate_pdf.py' first to create PDFs")
        return False

    en_report = en_reports[0]
    fi_report = fi_reports[0]

    # Create email with BCC for privacy (recipients hidden from each other)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = sender_email  # Sender as To: field
    msg['Bcc'] = ', '.join(recipients)  # All recipients in BCC (hidden from each other)
    msg['Subject'] = f"DWS6 Weekly Progress Report - {datetime.now().strftime('%Y-%m-%d')}"

    # Email body (generic since recipients are hidden via BCC)
    body = f"""
Hello,

Your weekly DWS6 progress report is attached in both English and Finnish (PDF format).

📊 This Week's Highlights:
- Production-ready AI agent system complete (25 files, 2,087 lines)
- 2 AI agents operational (Customer Satisfaction + Viability)
- 5 Nordic companies profiled for sales targeting
- €0 pilot cost confirmed
- Ready for deployment to api.dws6.com

📎 Attachments:
- WEEKLY_REPORT.pdf (English)
- WEEKLY_REPORT_FI.pdf (Finnish / Suomi)

These reports are formatted for presentation to:
✓ University partners
✓ Investors
✓ Media contacts

Copies automatically uploaded to Google Drive.

Next Steps:
→ Deploy to Google Cloud Run
→ Map api.dws6.com domain
→ Test with real Groq API credits

---
Lifetime Group - DWS IQ Platform
Team Lead: Risto Anton Päärni
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Status: 🟢 ON TRACK
    """

    msg.attach(MIMEText(body, 'plain'))

    # Get week number for attachment filenames
    now = datetime.now()
    year, week, _ = now.isocalendar()

    # Attach English report
    try:
        with open(en_report, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename=DWS6_Weekly_Report_W{week:02d}_{year}_EN.pdf')
            msg.attach(part)
    except Exception as e:
        print(f"❌ Failed to attach English report: {e}")
        return False

    # Attach Finnish report
    try:
        with open(fi_report, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename=DWS6_Weekly_Report_W{week:02d}_{year}_FI.pdf')
            msg.attach(part)
    except Exception as e:
        print(f"❌ Failed to attach Finnish report: {e}")
        return False

    # Send email
    try:
        if not sender_password:
            print("⚠️  SMTP_PASSWORD not set. Email not sent (dry run mode).")
            print(f"📧 Would send to: {', '.join(recipients)}")
            print(f"📎 Attachments: {os.path.basename(en_report)}, {os.path.basename(fi_report)}")
            return True

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print(f"✅ Weekly report sent to {len(recipients)} recipient(s)")
        for recipient in recipients:
            print(f"   → {recipient}")
        print(f"📎 Attached: DWS6_Weekly_Report_W{week:02d}_{year}_EN.pdf, DWS6_Weekly_Report_W{week:02d}_{year}_FI.pdf")
        return True

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

if __name__ == "__main__":
    success = send_weekly_report()
    exit(0 if success else 1)
