import csv 
import json 
import requests 

requests.packages.urllib3.disable_warnings() 

url_base = "http://localhost:58000/api/v1"

r_ticket = requests.post( 
    f"{url_base}/ticket", 
    json={"username": "cisco", "password": "class"}, 
    verify=False, 
) 

ticket = r_ticket.json()["response"]["serviceTicket"] 
headers = {"X-Auth-Token": ticket} 

devices = requests.get( 
    f"{url_base}/network-device", headers=headers, verify=False 
).json()["response"] 

hosts = requests.get(f"{url_base}/host", headers=headers, verify=False).json()[ 
    "response" 
] 

with open("inventario_red.csv", mode="w", newline="", encoding="utf-8") as f: 
    writer = csv.writer(f)
    writer.writerow( 
        ["CATEGORIA", "HOSTNAME", "TIPO", "IP", "MAC", "ESTADO_PING"] 
    )
    for d in devices: 
        writer.writerow( 
            [ 
                "Dispositivo de Red", 
                d.get("hostname"), 
                d.get("type"), 
                d.get("managementIpAddress"), 
                d.get("macAddress"), 
                d.get("collectionStatus"), 
            ] 
        ) 


    for h in hosts: 
        writer.writerow( 
            [ 
                "Host / Cliente", 
                h.get("hostName"), 
                h.get("hostType"), 
                h.get("hostIp"), 
                h.get("hostMac"), 
                h.get("pingStatus"), 
            ] 
        ) 
        
print("¡Inventario exportado con éxito a 'inventario_red.csv'!")