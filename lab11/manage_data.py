import csv
import psycopg2
from db import insert_data, query_data, delete_data, update_data, enter_data, upload_csv
from db import get_records_by_pattern, insert_or_update_user, insert_many_users, query_data_with_pagination, delete_data_by_username_or_phone


conn = psycopg2.connect("postgres://salman:C27w35dr7yZuPeSyg5HSL9C52txPjBU4@dpg-coipqan79t8c738lbhug-a.frankfurt-postgres.render.com/phonebook_and_snake", sslmode='require')
cur = conn.cursor()



userlist = [
    ("No", "No", "7017017012"), 
    ("New", "User", "0987654721"),
    ("User", "Neww", "1431231234"),
    ("Hello", "World", "3213993214")
]

# insert_many_users(userlist)

# get_records_by_pattern("Te")
# insert_or_update_user("New", "User", "12345678")

# update_data(id=10, first_name="Updatedname")

insert_many_users(userlist)

# upload_csv("./numbers.csv")
query_data()