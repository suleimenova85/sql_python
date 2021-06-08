import datetime
import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

with conn.cursor() as cursor:
    conn.autocommit = True
    values = [
        ('Book 1', '123456', datetime.datetime.now().date(), 'Author 1'),
        ('Book 2', '1234567', datetime.datetime.now().date(), 'Author 2'),
        ('Book 3', '12345678', datetime.datetime.now().date(), 'Author 3'),
    ]
    insert = sql.SQL('INSERT INTO books (name, author, added, book_autor) VALUES {}').format(
        sql.SQL(',').join(map(sql.Literal, values))
    )
    cursor.execute(insert)