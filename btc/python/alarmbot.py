import telegram
from telegram.ext import Updater
Token = "489893423:AAHzD6yYYHN8ySds5khQMrMxNO_bEtoTRfE"
chat_id = 489172102
bot = telegram.Bot(token = Token)
updater = Updater(token=Token)
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_uid, text="i'm not a robot")

