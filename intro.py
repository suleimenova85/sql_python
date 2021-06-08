# pip install psycopd2
import psycopg2
from psycopg2 import sql
# pip install pyTelegramBotAPI

import telebot

SECRET_CODE = "1866823302:AAES3bD93foQSneHQBjmGvqZAX_Qesbgnis"

bot = telebot.TeleBot(f"{SECRET_CODE}")

@bot.message_handler(commands=['start','help'])
def send_hello(message):
    #print(message)
    bot.reply_to(message,"Hello my friend")

bot.polling()