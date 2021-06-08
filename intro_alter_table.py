import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

#cursor.execute(""" 
                #ALTER TABLE books 
                #ADD COLUMN url varchar(255)
                #"""
                #)
cursor.execute(""" 
                ALTER TABLE books 
                ADD COLUMN genres varchar(255)
                """)
conn.commit()