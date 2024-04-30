import csv
import psycopg2
from db import insert_data, query_data, delete_data, update_data, enter_data, upload_csv

conn = psycopg2.connect("postgres://salman:C27w35dr7yZuPeSyg5HSL9C52txPjBU4@dpg-coipqan79t8c738lbhug-a.frankfurt-postgres.render.com/phonebook_and_snake", sslmode='require')
cur = conn.cursor()




# enter_data()
#upload_csv('numbers.csv')
#enter_data()

delete_data(name='balbes')

query_data()