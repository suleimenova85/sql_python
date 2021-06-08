#  pip install psycopg2
import psycopg2
from psycopg2 import sql

import datetime
#  pip install pyTelegramBotAPI

import telebot
from telebot import types

SECRET_CODE = "1866823302:AAES3bD93foQSneHQBjmGvqZAX_Qesbgnis"

conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

bot = telebot.TeleBot(f"{SECRET_CODE}")

# cursor.execute('SELECT * FROM book')
# all_data = cursor.fetchall()

def add_to_table(conn, **kwargs):
    with conn.cursor() as cursor:
        conn.autocommit = True
        values = [
            (
                kwargs.get('book_name'), 
                kwargs.get('author_id'), 
                datetime.datetime.now().date(), 
                kwargs.get('book_author'), 
                kwargs.get('url'),
                kwargs.get('genres')
                )
        ]
        insert = sql.SQL('INSERT INTO books (name, author, added, book_autor, url, genres) VALUES {}').format(
            sql.SQL(',').join(map(sql.Literal, values))
        )
        cursor.execute(insert)

# print("All data: ", all_data)
 
@bot.message_handler(commands=['start', 'help'])
def send_hello(message):
    bot.reply_to(message, "Привет, Друг!")

@bot.message_handler(commands=['create'])
def create(message):
    bot.reply_to(message, """Пожалуйста введите данные в заданном порядке\n 
                            name$book_author$url$genres""")
    print(message.from_user.id)

@bot.message_handler(func=lambda m: True)
def message_handler(message):
    message_list = message.text.split('$')
    message_dict = {
        "book_name": message_list[0],
        "book_author": message_list[1],
        "url": message_list[2],
        "genres": message_list[3],
        "author_id": message.from_user.id
    } 
    add_to_table(conn, **message_dict)


@bot.message_handler(commands=['read'])
def read(message):
    # print(message)
    bot.reply_to(message, "Hello my friend")

@bot.message_handler(commands=['update'])
def update(message):
    # print(message)
    bot.reply_to(message, "Hello my friend")

@bot.message_handler(commands=['delete'])
def delete(message):
    # print(message)
    bot.reply_to(message, "Hello my friend")


bot.polling()