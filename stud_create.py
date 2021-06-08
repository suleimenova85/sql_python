import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE students (id serial, group_code varchar(255), course varchar(255), st_name varchar(255)) 
                        ''')
conn.commit()