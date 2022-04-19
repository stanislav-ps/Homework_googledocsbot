import os
from dotenv import load_dotenv

load_dotenv()


CREDENTIALS = {
  "type": "service_account",
  "project_id": "my-first-project-346709",
  "private_key_id": os.getenv('PRIVATE_KEY_ID', ''),
  "private_key": os.getenv('PRIVATE_KEY', ''). replace('\\n', '\n'),
  "client_email": "omnomnom@my-first-project-346709.iam.gserviceaccount.com",
  "client_id": os.getenv('CLIENT_ID', ''),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/omnomnom%40my-first-project-346709.iam.gserviceaccount.com"
}

TG_TOKEN = os.getenv('TG_TOKEN', '')
SHEET_ID = '1cPLjCjuGAAmqBychhme-ziV0b0nwvI_vt-erTUQuYEM'
SHEET_URL = 'https://docs.google.com/spreadsheets/d/1cPLjCjuGAAmqBychhme-ziV0b0nwvI_vt-erTUQuYEM/edit#gid=0'