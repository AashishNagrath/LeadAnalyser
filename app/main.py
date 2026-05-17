from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.scraper import scrape_website
from app.ai_service import generate_business_analysis
from app.pdf_service import generate_pdf_report
from app.email_service import send_email_with_report
from app.sheets_service import log_lead_to_sheet


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/submit")
async def submit_form(
    name: str = Form(...),
    email: str = Form(...),
    company: str = Form(...),
    website: str = Form(...)
):

    print("\nNEW LEAD RECEIVED")
    print("Name:", name)
    print("Email:", email)
    print("Company:", company)
    print("Website:", website)

    # SCRAPE WEBSITE
    scraped_data = scrape_website(website)

    print("\nSCRAPED DATA:")
    print(scraped_data)

    analysis = generate_business_analysis(scraped_data)
    
    print("\nAI ANALYSIS:")
    print(analysis)
    
    # GENERATE PDF REPORT
    pdf_path = generate_pdf_report(
        name=name,
        company=company,
        analysis=analysis
    )

    print("\nPDF GENERATED:")
    print(pdf_path)
    
    send_email_with_report(
    recipient_email=email,
    recipient_name=name,
    company=company,
    pdf_path=pdf_path
    )

    print("\nEMAIL SENT SUCCESSFULLY")
    
    
    log_lead_to_sheet(
    name=name,
    email=email,
    company=company,
    website=website,
    status="Report Sent"
    )

    print("\nLEAD LOGGED TO GOOGLE SHEETS")


    if "Error:" in analysis:
        return {
            "status": "error",
            "message": analysis
        }

    return {
        "status": "success",
        "analysis": analysis
    }