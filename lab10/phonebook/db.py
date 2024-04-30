import csv
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect("postgres://salman:C27w35dr7yZuPeSyg5HSL9C52txPjBU4@dpg-coipqan79t8c738lbhug-a.frankfurt-postgres.render.com/phonebook_and_snake", sslmode='require')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(50)
    )
""")

conn.commit()

def insert_data(first_name, last_name, phone):
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()

def upload_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            name, lastname, phone = row[0].split(';')
            insert_data(name, lastname, phone)

def enter_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    insert_data(first_name, last_name, phone)

def update_data(id, first_name=None, phone=None):
    if first_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE id = %s", (first_name, id))
    if phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (phone, id))
    conn.commit()

def query_data(filter=None):
    if filter:
        cur.execute("SELECT * FROM phonebook WHERE %s", (filter,))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(name=None, phone=None):
    if name:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    if phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()


