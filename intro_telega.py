import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE books (id serial, name varchar(255), author varchar(255), added date, 
                    book_autor varchar(255)) 
                        ''')
conn.commit()