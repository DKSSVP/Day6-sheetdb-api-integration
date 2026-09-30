import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETDB_API_URL = os.getenv("SHEETDB_API_URL")

candidate = {
    "Name": "Rahul Kumar",
    "Email": "rahul.kumar@example.com",
    "Role": "GenAI Engineer",
    "Status": "Verified"
}

payload = {
    "data": [candidate]
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(
    SHEETDB_API_URL,
    json=payload,
    headers=headers,
    timeout=10
)

print("HTTP Status Code:", response.status_code)

if response.status_code == 201:
    print("Candidate record added successfully.")
else:
    print("SheetDB request failed.")
    print("Response:", response.text)