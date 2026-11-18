import json 
import requests 
from tabulate import tabulate

requests.packages.urllib3.disable_warnings()

url_base = "http://localhost:58000/api/v1"
r_ticket = requests.post( 
    f"{url_base}/ticket", 
    json={"username": "cisco", "password": "class"}, 
    verify=False, 
)

ticket = r_ticket.json()["response"]["serviceTicket"] 
headers = {"X-Auth-Token": ticket}

devs = requests.get( 
    f"{url_base}/network-device", headers=headers, verify=False 
).json()["response"] 
dev_table = [
    [ 
        d.get("hostname"), 
        d.get("type"), 
        d.get("managementIpAddress"),
        d.get("macAddress"), 
        d.get("collectionStatus"), 
    ] 
    for d in devs 
]

hosts = requests.get(f"{url_base}/host", headers=headers, verify=False).json()[ 
    "response"
] 
host_table = [
    [h.get("hostName"), h.get("hostType"), h.get("hostIp"), h.get("hostMac")] 
    for h in hosts 
]

print("\\n=== DISPOSITIVOS DE RED ===") 
print( 
    tabulate( 
        dev_table, 
        headers=["Hostname", "Tipo", "IP Admin", "MAC", "Estado"], 
        tablefmt="grid", 
        ) 
    )

print("\\n=== HOSTS / CLIENTES ===") 
print( 
    tabulate( 
        host_table, headers=["Hostname", "Tipo", "IP", "MAC"], tablefmt="grid" 
        ) 
    )











