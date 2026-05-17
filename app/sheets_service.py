import gspread

from oauth2client.service_account import ServiceAccountCredentials

from datetime import datetime


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

client = gspread.authorize(creds)

sheet = client.open(
    "LeadAnalyserSheet"
).sheet1


def log_lead_to_sheet(
    name,
    email,
    company,
    website,
    status
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    row = [
        timestamp,
        name,
        email,
        company,
        website,
        status
    ]

    sheet.append_row(row)

    return True