IP Network Monitor con Alertas por Telegram

Herramienta de monitoreo de red desarrollada en Python que escanea rangos de direcciones IP y envía alertas automáticas por Telegram cuando un dispositivo permanece desconectado durante un tiempo determinado.

🚀 Características

	Escaneo de rangos de IP personalizados

	Monitoreo concurrente usando multithreading

	Lista de IPs ignoradas (mantenimiento o desactivadas)

	Alertas automáticas mediante Telegram

	Tiempo de desconexión configurable

	Verificación periódica automática

🛠 Tecnologías utilizadas

	Python 3.10+

	threading

	subprocess

	requests

	API de Telegram Bot

📦 Instalación

	Clonar el repositorio:

	git clone https://github.com/luisdl-dev/seguimiento-desconexion-camaras-ip.git
	cd ip-network-monitor

	Instalar dependencias:

	pip install -r requirements.txt

⚙ Configuración

	Crear un archivo .env con las siguientes variables:

	TELEGRAM_TOKEN=tu_token_aqui
	TELEGRAM_CHAT_ID=tu_chat_id_aqui

	Nota: El archivo .env no debe subirse al repositorio.

▶ Uso

	Ejecutar el programa:

	python main.py

	El sistema comenzará a monitorear las IP locales configuradas y enviará una alerta al bot telegram si alguna permanece desconectada por más del tiempo definido.

📌 Posibles mejoras futuras

	Compatibilidad multiplataforma (Windows / Linux)

	Implementación de logging profesional

	Interfaz gráfica

	Configuración mediante archivo JSON

	Exportación de reportes
	

👨‍💻 Autor

	Luis de la Torre Palomino
	Desarrollador autodidacta enfocado en automatización en general, monitoreo de redes e implementación de soluciones del sistemas CCTV con inteligencia artificial.