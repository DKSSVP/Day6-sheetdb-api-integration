import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETDB_API_URL = os.getenv("SHEETDB_API_URL")

candidates = [
    {
        "Name": "Rahul Kumar",
        "Email": "rahul.kumar@example.com",
        "Role": "GenAI Engineer",
        "Status": "Verified"
    },
    {
        "Name": "Preethi Shetty",
        "Email": "preethishetty@example.com",
        "Role": "AI Engineer",
        "Status": "Verified"
    },
    {
        "Name": "Arjun Reddy",
        "Email": "arjun.reddy@example.com",
        "Role": "Python Developer",
        "Status": "Verified"
    },
    {
        "Name": "Neeraja Goswami",
        "Email": "neeraja.goswami@example.com",
        "Role": "Data Analyst",
        "Status": "Verified"
    },
    {
        "Name": "Vikram Rathod",
        "Email": "vikram.rathod@example.com",
        "Role": "Software Engineer",
        "Status": "Verified"
    }
]

payload = {
    "data": candidates
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
    print("Candidate records added successfully.")
else:
    print("SheetDB request failed.")
    print("Response:", response.text)

