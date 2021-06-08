import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE teacher (id serial, subject varchar(255), departament varchar(255), status varchar(255), th_name varchar(255))
                        ''')
conn.commit()