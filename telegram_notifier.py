# enviar_telegram.py

import requests
import sys

# === CONFIGURACIÓN DE TELEGRAM ===
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def enviar_mensaje_telegram(texto):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': texto}
    response = requests.get(url, params=params)
    return response.json()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python enviar_telegram.py \"mensaje a enviar\"")
        sys.exit(1)

    mensaje = sys.argv[1]
    resultado = enviar_mensaje_telegram(mensaje)

    if resultado.get('ok'):
        print("✅ Mensaje enviado con éxito.")
    else:
        print("❌ Error al enviar mensaje:", resultado)
