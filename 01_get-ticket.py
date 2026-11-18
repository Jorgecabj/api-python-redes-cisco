import json
import requests

requests.packages.urllib3.disable_warnings()
url = "http://localhost:58000/api/v1/ticket"

payload = json.dumps({"username": "cisco", "password": "class"})
headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers, data=payload, verify=False)
print(f"Status Code: {response.status_code}")
print(response.text)