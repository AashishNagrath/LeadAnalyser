# SimplifIQ AI Lead Automation System

An AI-powered automated business audit system built for the SimplifIQ AI Software Developer Intern Assessment.

## Features

- Lead intake form
- Website scraping & enrichment
- AI-generated business analysis using Gemini
- Automated PDF report generation
- Automatic email delivery
- End-to-end workflow automation

## Tech Stack

- FastAPI
- Python
- Gemini API
- BeautifulSoup
- ReportLab
- Gmail SMTP
- TailwindCSS

## Workflow

1. User submits company details
2. Website content is scraped
3. AI generates personalized analysis
4. PDF audit report is created
5. Report emailed automatically

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_key
EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_app_password
```