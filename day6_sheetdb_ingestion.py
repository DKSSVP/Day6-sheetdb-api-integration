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

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

existing_response = requests.get(
    SHEETDB_API_URL,
    headers=headers,
    timeout=10
)

print("GET Status Code:", existing_response.status_code)

if existing_response.status_code == 200:

    existing_candidates = existing_response.json()

    candidate_email = candidate["Email"]

    duplicate_found = any(
        existing_candidate.get("Email") == candidate_email
        for existing_candidate in existing_candidates
    )

    if duplicate_found:
        print("Candidate already exists in Google Sheet.")
        print("No new record was added.")
        print("Existing data was not updated.")

    else:
        payload = {
            "data": [candidate]
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

else:
    print("Unable to retrieve existing candidates.")
    print("Response:", existing_response.text)