from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

from oauth2client.service_account import ServiceAccountCredentials


FOLDER_ID = "18Wt_CWLwMSf_tEob8MKn2jGYmiYHmJYG"


def upload_pdf_to_drive(pdf_path):

    gauth = GoogleAuth()

    scope = [
        "https://www.googleapis.com/auth/drive"
    ]

    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json",
        scope
    )

    drive = GoogleDrive(gauth)

    file = drive.CreateFile(
        {
            "title": pdf_path.split("/")[-1],
            "parents": [
                {
                    "id": FOLDER_ID
                }
            ]
        }
    )

    file.SetContentFile(pdf_path)

    file.Upload()

    return file["id"]