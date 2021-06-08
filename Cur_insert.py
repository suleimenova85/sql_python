import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

with conn.cursor() as cursor:
    conn.autocommit = True
    values = [
        ('Decode 1', '1', '1'),
        ('Decode 2', '2', '2'),
        ('Decode 3', '3', '3'),
        ('Decode 4', '4', '4'),
    ]
    insert = sql.SQL('INSERT INTO curator (group_code, course, th_id) VALUES {}').format(
        sql.SQL(',').join(map(sql.Literal, values))
    )
    cursor.execute(insert)