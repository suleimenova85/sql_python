import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE curator (group_code varchar(255), course varchar(255), th_id integer)
                        ''')
conn.commit()