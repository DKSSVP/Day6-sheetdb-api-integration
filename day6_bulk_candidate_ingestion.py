import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETDB_API_URL = os.getenv("SHEETDB_API_URL")

candidates = [
    {
        "Name": "Sandeep Reddy Vanga",
        "Email": "sandeep.reddy.vanga@example.com",
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
    },
    {
        "Name": "Raja Mouli",
        "Email": "raja.mouli@example.com",
        "Role": "GenAI Engineer",
        "Status": "Verified"
    }
]

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Get existing candidates from SheetDB
existing_response = requests.get(
    SHEETDB_API_URL,
    headers=headers,
    timeout=10
)

print("GET Status Code:", existing_response.status_code)

if existing_response.status_code == 200:

    existing_candidates = existing_response.json()

    # Store existing emails for duplicate checking
    existing_emails = {
        candidate.get("Email")
        for candidate in existing_candidates
    }

    new_candidates = []
    processed_emails = set()

    # Check each incoming candidate
    for candidate in candidates:

        candidate_email = candidate.get("Email")

        if candidate_email in existing_emails:
            print(f"Duplicate skipped: {candidate_email}")
            continue

        if candidate_email in processed_emails:
            print(
                f"Duplicate in current batch skipped: "
                f"{candidate_email}"
            )
            continue

        new_candidates.append(candidate)
        processed_emails.add(candidate_email)

    print("New candidates to add:", len(new_candidates))

    # Add only new candidates
    if new_candidates:

        payload = {
            "data": new_candidates
        }

        response = requests.post(
            SHEETDB_API_URL,
            json=payload,
            headers=headers,
            timeout=10
        )

        print("HTTP Status Code:", response.status_code)

        if response.status_code == 201:
            print(
                f"{len(new_candidates)} "
                "candidate records added successfully."
            )
        else:
            print("SheetDB request failed.")
            print("Response:", response.text)

    else:
        print("No new candidates to add.")
        print("No existing data was updated.")

else:
    print("Unable to retrieve existing candidates.")
    print("Response:", existing_response.text)