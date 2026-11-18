import json
import requests

requests.packages.urllib3.disable_warnings()
r_ticket = requests.post(
    "http://localhost:58000/api/v1/ticket", 
    json={"username": "cisco", "password": "class"}, 
    verify=False,
)

ticket = r_ticket.json()["response"]["serviceTicket"]

url = "http://localhost:58000/api/v1/host"
headers = {"X-Auth-Token": ticket, "Content-Type": "application/json"}
response = requests.get(url, headers=headers, verify=False)

print(f"Status Code: {response.status_code}") 
print(json.dumps(response.json(), indent=2))


