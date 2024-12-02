# Proyecto Telegram bot

## Descripción
Proyecto de introducción al desarrollo de bots de Telegram utilizando Python y la librería python-telegram-bot. 

## Características
- Bot simple que repite los mensajes recibidos
- Implementación de comando `/start`
- Muestra información básica del usuario

## Requisitos
- Python 3.8+
- Librería python-telegram-bot

## Configuración
1. Clonar el repositorio
2. Crear entorno virtual
3. Instalar dependencias: `pip install -r requirements.txt`
4. Crear un archivo `config.py` con el token del bot:
   ```python
   BOT_TOKEN = "tu_token_de_bot_aqui"
   ```
   **Importante:** Añadir `config.py` al `.gitignore`

## Ejecución
```bash
python bot.py
```

## Objetivos del Proyecto
- Aprender conceptos básicos de desarrollo de bots
- Practicar programación con Python
- Entender la interacción con APIs de mensajería
- Implementar buenas prácticas de seguridad con credenciales