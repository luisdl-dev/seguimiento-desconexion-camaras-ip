import subprocess
import time
import threading
import os
from datetime import datetime
import subprocess

# === CONFIGURACIÓN ===
# IPS DE EJEMPLO
RANGOS_IP = [
    ("192.168.1.5", "192.168.1.115"), #NVR 1
    ("192.168.0.5", "192.168.0.25"), #NVR 2
    ("192.168.3.5", "192.168.3.41"), #NVR 3
    ("192.168.3.5", "192.168.3.51") #NVR 4
]

# Lista de IPs de ejemplo que deben ser ignoradas por equipos que se encuentran desactivadas, en mantenimiento, etc.
IPS_IGNORADAS = [
    "192.168.1.64",
    "192.168.1.56",
    "192.168.1.110",
    "192.168.1.38",
    "192.168.1.39"
]

CHEQUEO_INTERVALO_SEG = 15  # cada cuánto tiempo se verifica
TIEMPO_DESCONEXION_ALERTA = 60  # segundos que deben pasar para considerar desconexión

# Diccionario para registrar tiempo de última conexión exitosa
estado_ips = {}

def ip_a_int(ip):
    return sum(int(oct) << (24 - i*8) for i, oct in enumerate(ip.split('.')))

def int_a_ip(n):
    return '.'.join(str((n >> (24 - i*8)) & 0xFF) for i in range(4))

def generar_lista_ips(inicio, fin):
    return [int_a_ip(i) for i in range(ip_a_int(inicio), ip_a_int(fin)+1)]

def esta_activa(ip):
    try:
        resultado = subprocess.run(["ping", "-n", "1", "-w", "1000", ip], stdout=subprocess.DEVNULL)
        return resultado.returncode == 0
    except:
        return False



def enviar_alerta(ip):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
    mensaje = f"{ahora}\n🚨 La IP {ip} está desconectada por más de {TIEMPO_DESCONEXION_ALERTA} segundos."
    
    subprocess.run(["python", "msg_telegram.py", mensaje])

def monitorear_ip(ip):
    while True:
        if esta_activa(ip):
            estado_ips[ip] = time.time()
        else:
            tiempo_desde_ultima_respuesta = time.time() - estado_ips.get(ip, 0)
            if tiempo_desde_ultima_respuesta > TIEMPO_DESCONEXION_ALERTA:
                enviar_alerta(ip)
                # Para evitar múltiples alertas repetidas, reiniciamos el tiempo
                estado_ips[ip] = time.time()
        time.sleep(CHEQUEO_INTERVALO_SEG)

def main():
    todas_las_ips = []
    for inicio, fin in RANGOS_IP:
        todas_las_ips.extend(generar_lista_ips(inicio, fin))

    # ➖ Filtrar IPs ignoradas
    todas_las_ips = [ip for ip in todas_las_ips if ip not in IPS_IGNORADAS]

    print(f"🔍 Monitoreando {len(todas_las_ips)} IPs...")

    for ip in todas_las_ips:
        estado_ips[ip] = time.time()  # Asumimos que al inicio todas están conectadas
        hilo = threading.Thread(target=monitorear_ip, args=(ip,), daemon=True)
        hilo.start()

    while True:
        time.sleep(100)

if __name__ == "__main__":
    main()
