import base64
import requests
from requests.structures import CaseInsensitiveDict


"""
Request a spotify token
Returns:
{
   "access_token": "NgCXRKc...MzYjw",
   "token_type": "bearer",
   "expires_in": 3600
} 
"""
def get_token(client_id, client_secret):
    url = 'https://accounts.spotify.com/api/token'

    encoded_secrets = str(base64.b64encode(bytes(client_id + ":" + client_secret, 'utf-8')), 'utf-8')

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Basic " + encoded_secrets
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    response = requests.post(url=url, headers=headers, params={'grant_type': 'client_credentials'})

    if(response.status_code == 200):
        return response.json()
    else:
        raise Exception("error getting token " + response.status_code + ":" + response.text)


