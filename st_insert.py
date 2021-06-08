import datetime
import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

with conn.cursor() as cursor:
    conn.autocommit = True
    values = [
        ('Decode 1', '1', 'Assem'),
        ('Decode 2', '2', 'Akbota'),
        ('Decode 3', '3', 'Maxim'),
        ('Decode 4', '4', 'Beksultan'),
    ]
    insert = sql.SQL('INSERT INTO students (group_code, course, st_name) VALUES {}').format(
        sql.SQL(',').join(map(sql.Literal, values))
    )
    cursor.execute(insert)