import requests
import json

def GerarToken():
    url = 'https://account.uipath.com/oauth/token'
    payload = {
        "grant_type": "refresh_token",
        "client_id": "8DEv1AMNXczW3y4U15LL3jYf62jK93n5",
        "refresh_token": "ZPtY8pwOZg4uBtZX0mDUgKUg4Wvhgc5HMpDq0i-e9j_Gj"
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print('Erro')
        return None
    else:
        return response.json()['access_token']

def ExecutaRpa(token):
    url = "https://cloud.uipath.com/uipatqecdljs/DefaultTenant/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"
    payload = json.dumps({
        "startInfo": {
            "ReleaseKey": "45c5f7ac-30a2-4772-beae-cc9b56e43a7c",
            "Strategy": "ModernJobsCount",
            "JobsCount": 1,
            "InputArguments": "{}"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'X-UIPATH-TenantName': 'DefaultTenant',
        'X-UIPATH-OrganizationUnitId': '3971013',
        'Authorization': f'Bearer {token}'
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Erro")
        return False
    else:
        return True
    
# Chame a função e imprima o resultado
token = GerarToken()
ExecutaRpa(token)
