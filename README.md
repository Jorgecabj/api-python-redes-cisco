# Network Automation Scripts - Cisco Packet Tracer Network Controller API 

Este repositorio contiene los scripts en Python desarrollados para interactuar programáticamente con la API REST del Network Controller en Cisco Packet Tracer (TP Integrador Redes). 

## Requisitos y Entorno Virtual 
1. Crear y activar el entorno virtual de Python: 
bash
python3 -m venv venv
source venv/bin/activate # En Linux/macOS
# venv\\Scripts\\activate # En Windows

Instalar las dependencias necesarias:
pip install requests tabulate

* 01_get-ticket.py: Solicita el ticket de autenticación (serviceTicket) enviando usuario y contraseña.
* 02_get-network-device.py: Obtiene el inventario de dispositivos de red en formato JSON.
* 03_get-host.py: Obtiene la lista de hosts y clientes conectados en formato JSON.
* 04_tabulate.py: Presenta la información consolidada de dispositivos y hosts en tablas formateadas por consola.
* 05_export_inventory_csv.py *(Script propio)*: Extrae el inventario de la API REST y lo exporta a un archivo inventario_red.csv.
