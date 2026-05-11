import os
import requests
from msal import ConfidentialClientApplication

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

WORKSPACE_ID = "553aabb5-491d-4d52-9ac6-8f66ba542ef6"

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
    "Authorization": f"Bearer {access_token}"
}

url = f"https://api.powerbi.com/v1.0/myorg/groups/{WORKSPACE_ID}/datasets"

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
