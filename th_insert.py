import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="decode_python", user="decode_user",
                        password="password", host="localhost")

cursor = conn.cursor()

with conn.cursor() as cursor:
    conn.autocommit = True
    values = [
        ('Python', 'mathematics', 'Professor', 'Sahaev'),
        ('sql', 'physics', 'Doctor', 'Serov'),
        ('Java', 'chemistery', 'Graduate student', 'Ivanov'),
        ('Ruby', 'it', 'Candidate', 'Suleymenov'),
    ]
    insert = sql.SQL('INSERT INTO teacher (subject, departament, status, th_name) VALUES {}').format(
        sql.SQL(',').join(map(sql.Literal, values))
    )
    cursor.execute(insert)