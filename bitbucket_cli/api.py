import requests

BASE_URL = "https://api.bitbucket.org/2.0/"

def get_pipelines(api_key, repo):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(f"{BASE_URL}repositories/{repo}/pipelines/", headers=headers)
    return response.json()

# Puoi aggiungere altre funzioni per altre chiamate API qui...
