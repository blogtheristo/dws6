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
    recipient_email = "risto.paarni2024@lifetime.fi"

    # Get latest reports (support both from repo root and Reports/ directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    en_pattern = os.path.join(script_dir, "en/WEEKLY_REPORT*.md")
    fi_pattern = os.path.join(script_dir, "fi/WEEKLY_REPORT*.md")

    en_reports = sorted(glob.glob(en_pattern), reverse=True)
    fi_reports = sorted(glob.glob(fi_pattern), reverse=True)

    if not en_reports or not fi_reports:
        print("❌ No reports found")
        return False

    en_report = en_reports[0]
    fi_report = fi_reports[0]

    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"DWS6 Weekly Progress Report - {datetime.now().strftime('%Y-%m-%d')}"

    # Email body
    body = f"""
Hi Risto,

Your weekly DWS6 progress report is attached in both English and Finnish.

📊 This Week's Highlights:
- Production-ready AI agent system complete (25 files, 2,087 lines)
- 2 AI agents operational (Customer Satisfaction + Viability)
- 5 Nordic companies profiled for sales targeting
- €0 pilot cost confirmed
- Ready for deployment to api.dws6.com

📎 Attachments:
- WEEKLY_REPORT.md (English)
- WEEKLY_REPORT_FI.md (Finnish / Suomi)

Next Steps:
→ Deploy to Google Cloud Run
→ Map api.dws6.com domain
→ Test with real Groq API credits

---
Team Lead: Risto Anton Päärni
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Status: 🟢 ON TRACK
    """

    msg.attach(MIMEText(body, 'plain'))

    # Attach English report
    try:
        with open(en_report, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename=WEEKLY_REPORT_EN.md')
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
            part.add_header('Content-Disposition', f'attachment; filename=WEEKLY_REPORT_FI.md')
            msg.attach(part)
    except Exception as e:
        print(f"❌ Failed to attach Finnish report: {e}")
        return False

    # Send email
    try:
        if not sender_password:
            print("⚠️  SMTP_PASSWORD not set. Email not sent (dry run mode).")
            print(f"📧 Would send to: {recipient_email}")
            print(f"📎 Attachments: {os.path.basename(en_report)}, {os.path.basename(fi_report)}")
            return True

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print(f"✅ Weekly report sent to {recipient_email}")
        print(f"📎 Attached: {os.path.basename(en_report)}, {os.path.basename(fi_report)}")
        return True

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

if __name__ == "__main__":
    success = send_weekly_report()
    exit(0 if success else 1)
