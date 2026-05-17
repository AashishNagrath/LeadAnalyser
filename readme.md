# SimplifIQ AI Lead Automation System

An AI-powered automated lead enrichment and business audit platform built for the SimplifIQ AI Software Developer Intern Assessment.

The system captures lead information, enriches company data through website scraping, generates personalized business audit reports using Gemini AI, creates professional PDF reports, and automatically emails them to prospects without human intervention.

---

# Features

## Core Workflow

- Lead intake form
- Website scraping and company enrichment
- AI-generated business analysis
- Automated PDF report generation
- Automatic email delivery
- End-to-end workflow automation

## Bonus Features

- Google Sheets lead logging
- Google Drive PDF archiving (with graceful fallback handling)

---

# Tech Stack

## Frontend
- HTML5
- TailwindCSS

## Backend
- FastAPI
- Python

## AI
- Google Gemini API (Gemini 2.5 Flash)

## Web Scraping
- BeautifulSoup4
- requests

## PDF Generation
- ReportLab

## Email Delivery
- Gmail SMTP

## Logging & Storage
- Google Sheets API
- Google Drive API

---

# System Workflow

```text
User submits lead form
        ↓
Website scraping & enrichment
        ↓
Gemini AI business analysis
        ↓
PDF audit report generation
        ↓
Automatic email delivery
        ↓
Google Sheets logging
        ↓
Google Drive archival attempt
```

---

# Project Structure

```text
LeadFormAnalyser/
│
├── app/
│   ├── main.py
│   ├── scraper.py
│   ├── ai_service.py
│   ├── pdf_service.py
│   ├── email_service.py
│   ├── sheets_service.py
│   └── drive_service.py
│
├── templates/
│   └── index.html
│
├── generated_reports/
│
├── requirements.txt
├── reflection.txt
├── credentials.json
├── .env
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd LeadFormAnalyser
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

---

# Google Sheets Setup

## Enable APIs
- Google Sheets API
- Google Drive API

## Create Service Account
- Download `credentials.json`
- Place in project root

## Share Sheet
[(https://docs.google.com/spreadsheets/d/1UgGeg1F_2NuLFdY0QzCFJ1SiUWpuR6SuTP1jX878FbE/edit?usp=sharing)]
---

# Run Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

# Key Engineering Decisions

- FastAPI was selected for rapid API development and workflow orchestration.
- Gemini API was chosen for its free-tier availability and strong AI generation quality.
- ReportLab was used instead of WeasyPrint to avoid Windows dependency issues and ensure reliable PDF generation.
- The frontend was intentionally lightweight to prioritize automation workflow quality and backend functionality.

---

# Error Handling & Reliability

The system includes:
- API error handling
- Graceful failure handling
- Scraping fallback logic
- Email authentication validation
- Google Drive upload fallback handling

The workflow is designed so that optional failures do not interrupt the core report generation process.

---

# Limitations

- Some websites may block scraping requests.
- AI output quality depends on available website content.
- Google Drive uploads may require additional OAuth configuration for production-scale deployment.
- PDF styling can be enhanced further.

---

# Future Improvements

- Improved PDF design and branding
- Asynchronous task queues
- Advanced enrichment APIs
- Admin dashboard
- Authentication system
- Analytics and monitoring
- Better frontend UX

---

# Author

Aashish Nagrath

Built as part of the SimplifIQ AI Software Developer Intern Assessment.