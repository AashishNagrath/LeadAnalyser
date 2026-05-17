import os
import smtplib

from dotenv import load_dotenv

from email.message import EmailMessage

load_dotenv()


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email_with_report(
    recipient_email,
    recipient_name,
    company,
    pdf_path
):

    msg = EmailMessage()

    msg["Subject"] = f"{company} - AI Business Audit Report"

    msg["From"] = EMAIL_ADDRESS

    msg["To"] = recipient_email

    msg.set_content(
        f"""
Hi {recipient_name},

Thank you for your interest.

We analyzed {company}'s digital presence and prepared a personalized AI-powered business audit report.

The report is attached to this email.

Best regards,
SimplifIQ Automation System
"""
    )

    # ATTACH PDF
    with open(pdf_path, "rb") as f:

        file_data = f.read()

        file_name = os.path.basename(pdf_path)

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename=file_name
    )

    # SEND EMAIL
    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            EMAIL_ADDRESS,
            EMAIL_PASSWORD
        )

        smtp.send_message(msg)

    return True