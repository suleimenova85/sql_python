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

def delete(conn, name: str):
    try:
        with conn.cursor() as cursor:
            conn.autocommit = True
            command_for_delete = sql.SQL(f"sdelete from book where name='{name}'")
            cursor.execute(command_for_delete)
    except Exception as error:
        import pdb
        pdb.set_trace()
        print(f"Name like {name} doesn't exist", error)

def get_all_data(conn):
    my_result = []
    with conn.cursor() as cursor:
        conn.autocommit = True
        select = sql.SQL("SELECT * FROM book")
        cursor.execute(select)
        my_result = cursor.fetchall()
    return my_result

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
        insert = sql.SQL('INSERT INTO book (name, author_id, added, book_author, url, genres) VALUES {}').format(
            sql.SQL(',').join(map(sql.Literal, values))
        )
        cursor.execute(insert)

def get_data_with_params(conn, *args):
    my_result = []
    with conn.cursor() as cursor:
        conn.autocommit = True
        select = sql.SQL(f"SELECT * FROM book where name = {name}")
        cursor.execute(select)
        my_result = cursor.fetchall()
    return my_result
# print("All data: ", all_data)
 
@bot.message_handler(commands=['start', 'help'])
def send_hello(message):
    bot.reply_to(message, """Привет, Друг!\n
                            Пожалуйста введите данные в заданном порядке\n 
                            method$name$book_author$url$genres""")

@bot.message_handler(func=lambda m: True)
def message_handler(message):
    message_list = message.text.split('$')
    if (message_list[0]).lower() == "create":
        message_dict = {
            "method": message_list[0],
            "book_name": message_list[1],
            "book_author": message_list[2],
            "url": message_list[3],
            "genres": message_list[4],
            "author_id": message.from_user.id
        } 
        add_to_table(conn, **message_dict)
    elif (message_list[0]).lower() == 'read':
        data = get_all_data(conn)
        data_dict = dict()
        default_str = ""
        for item in data:
            data_dict[item[1]] = item[5]
        for key, value in data_dict.items():
            default_str += f"""{key} - {value}\n"""
        bot.reply_to(message, default_str)
    elif (message_list[0]).lower() == 'delete':
        delete(conn, name=message_list[1])
        bot.reply_to(message, message_list[1])
bot.polling()