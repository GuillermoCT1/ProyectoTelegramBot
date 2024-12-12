# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN

# Configuración del token del bot

# Función para manejar el comando /start
async def start(update: Update, context):
    user = update.effective_user
    # Responde con un saludo al usuario
    await update.message.reply_text(
        f"Hola, {user.first_name}! Soy un bot Echo. ¡Envíame algo y te lo devolveré!"
    )
    

# Función para manejar los mensajes de texto (eco)
async def echo(update: Update, context):
    # Repite el mensaje recibido
    await update.message.reply_text(update.message.text)

# Añadir el handler para el comando /start
def add_start_handler(app):
    start_handler = CommandHandler("start", start)
    app.add_handler(start_handler)

# Añadir el handler para los mensajes de texto
def add_echo_handler(app):
    echo_handler = MessageHandler(filters.ALL, echo)
    app.add_handler(echo_handler)

# Función principal para ejecutar el bot
def main():
    # Crear la aplicación del bot
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Añadir los handlers
    add_start_handler(app)
    add_echo_handler(app)

    # Iniciar el bot
    print("El bot está en funcionamiento...")
    app.run_polling()

if __name__ == "__main__":
    main()