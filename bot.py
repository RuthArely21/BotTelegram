from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import os

token="5884705123:AAF5Z1Zp9aCpEajwXX4aCfHautZ9wibJIq8"

def start(bot,update):
    try:
        user_data = update.message.from_user
        update.message.reply_text("Hola estoy listo")
        print(f"{user_data}")
    except Exception as e:
        print(f"Error start:{e.args}")
        
def help(bot,update):
    try:
        update.message.reply_text("Este bot tiene los siguientes comandos....")
    except Exception as e:
        print(f"Error help:{e.args}")
        
def echo(bot, update ):
    try:
        text = update.message.text
        update.message.reply_text(f"{text}")
    except Exception as e:
        print(f"Error echo: {e.args}")

def image(bot, update): 
    try:
        print("Recibiendo imagen")
        user_data = update.message.from_user
        print(user_data)
        file = bot.getFile(update.message.photo[-1].file_id)
        filename = os.path.join('descargas/imagenes/','imagen.jpg')
        file.download(filename)
        update.message.reply_text(f"Imagen recibida")
    except Exception as e:
        print(f"Error image:{e.args}")
        
def error(bot, update, error):
    try:
        print(f"Update: {update} genero el error {error}")
    except Exception as e:
        print(f"Error en error: {e.args}")
        
def operacion(bot,update):
    try:
        update.message.reply_text("operaciones")
    except Exception as e:
        print(f"Error operacion:{e.args}")


        
        

def main():
    try:
        print("S.A.M.M. iniciando el token")
        updater = Updater(token)
        
        print("S.A.M.M iniciando dispacher")
        dp = updater.dispatcher
        
        print("S.A.M.M iniciando commandHandler")
        dp.add_handler(CommandHandler("start",start))
        dp.add_handler(CommandHandler("help",help))
        dp.add_handler(CommandHandler("operacion",operacion))
        
        dp.add_handler(MessageHandler(Filters.text,echo))
        dp.add_handler(MessageHandler(Filters.photo,image))       
        dp.add_error_handler(error)
        
        updater.start_polling()
        
        print("S.A.M.M. Iniciando el bot")
        updater.idle()
    
    except Exception as e:
        print(f"Error main: {e.args}")
        
if _name_ == "_main_":
    main()