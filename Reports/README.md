# DWS6 Weekly Reports

Automated weekly progress reports in English and Finnish.

## 📁 Folder Structure

```
Reports/
├── en/                    # English reports
│   └── WEEKLY_REPORT.md
├── fi/                    # Finnish reports (Suomi)
│   └── WEEKLY_REPORT_FI.md
├── send_weekly_report.py  # Email automation script
└── README.md              # This file
```

## 📧 Email Automation

Reports are automatically emailed every **Monday at 10:00 Helsinki time** to:
- **Recipient:** risto.paarni2024@lifetime.fi
- **Format:** Markdown attachments (EN + FI)
- **Automation:** GitHub Actions workflow

### Workflow Schedule

- **Automatic:** Every Monday 08:00 UTC (10:00 Helsinki)
- **Manual:** Can be triggered via GitHub Actions interface

## 🔧 Setup Instructions

### 1. Configure Email Secrets

Add these secrets to your GitHub repository:

1. Go to **Settings → Secrets and variables → Actions**
2. Add the following secrets:

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `SMTP_SENDER` | Sender email address | `noreply@dws6.com` |
| `SMTP_PASSWORD` | Email account password | `your_app_password` |
| `SMTP_SERVER` | SMTP server (optional) | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP port (optional) | `587` |

### 2. Gmail Setup (if using Gmail)

If using Gmail as SMTP server:

1. Enable **2-Factor Authentication** on your Google account
2. Generate an **App Password**:
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and "Other (Custom name)"
   - Name it "DWS6 Reports"
   - Copy the 16-character password
3. Use this password as `SMTP_PASSWORD` secret

### 3. Test Locally

```bash
cd Reports

# Set environment variables
export SMTP_SENDER="your-email@gmail.com"
export SMTP_PASSWORD="your-app-password"
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"

# Run script
python send_weekly_report.py
```

### 4. Manual Trigger (GitHub)

1. Go to **Actions** tab in GitHub
2. Select **Weekly Report Email Automation**
3. Click **Run workflow**
4. Click **Run workflow** button

## 📊 Report Contents

Each weekly report includes:

- **Executive Summary** - Key metrics and achievements
- **Major Achievements** - Completed deliverables
- **Technical Architecture** - Stack and infrastructure
- **Cost Analysis** - Budget and savings
- **Development Metrics** - Code statistics and commits
- **Strategic Decisions** - Key choices and rationale
- **Pending Tasks** - Next steps and priorities
- **Risk Assessment** - Current risks and mitigation
- **Team Contributions** - Individual accomplishments
- **KPI Dashboard** - Performance indicators

## 🗓️ Report Naming Convention

Reports are named with date stamps for versioning:

```
WEEKLY_REPORT_2025-12-03.md       # English
WEEKLY_REPORT_FI_2025-12-03.md    # Finnish
```

## 🔍 Troubleshooting

### Email not sending?

1. **Check secrets** - Verify all SMTP secrets are set correctly
2. **Test locally** - Run script locally with debug output
3. **Check logs** - View GitHub Actions logs for error messages
4. **Gmail blocks** - Ensure "Less secure app access" or App Passwords enabled

### Reports not found?

```bash
# Verify reports exist
ls -la Reports/en/
ls -la Reports/fi/

# Check file permissions
chmod +x Reports/send_weekly_report.py
```

## 📝 Manual Report Generation

To manually create a new report:

1. Copy previous week's report
2. Update dates and content
3. Save in appropriate language folder
4. Run email script or wait for scheduled send

## 🚀 Future Enhancements

- [ ] HTML email formatting with charts
- [ ] PDF attachment generation
- [ ] Multiple recipient support
- [ ] Slack/Teams integration
- [ ] Custom report templates
- [ ] Automated metrics collection

---

**Last Updated:** December 3, 2025
**Maintained By:** Claude Code "The Lead"
**Team Lead:** Risto Anton Päärni
