import os
import requests
from msal import ConfidentialClientApplication

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

DATASETS = [
    "acba31c4-8014-4c55-92e4-f8020ca8c5ca",
    "84e646d6-51a0-497d-8314-8343e1aa7ca2"
]

authority = f"https://login.microsoftonline.com/{TENANT_ID}"

app = ConfidentialClientApplication(
    CLIENT_ID,
    authority=authority,
    client_credential=CLIENT_SECRET
)

token_response = app.acquire_token_for_client(
    scopes=["https://analysis.windows.net/powerbi/api/.default"]
)

access_token = token_response["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

for dataset_id in DATASETS:

    refresh_url = (
        f"https://api.powerbi.com/v1.0/myorg/"
        f"datasets/{dataset_id}/refreshes"
    )

    response = requests.post(
        refresh_url,
        headers=headers,
        json={}
    )

    print("\n===================")
    print("Dataset:", dataset_id)
    print("Status:", response.status_code)
    print("Response:", response.text)
