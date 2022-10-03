from telegram import Update
from telegram.ext import CallbackContext
import datetime
import weather




def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/help\n/Weather <City>')

def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def weather_command(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    update.message.reply_text(f'{weather.weather(items[1])}\n')
   

    
 
