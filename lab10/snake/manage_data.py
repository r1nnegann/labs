import psycopg2

conn = psycopg2.connect("postgres://salman:C27w35dr7yZuPeSyg5HSL9C52txPjBU4@dpg-coipqan79t8c738lbhug-a.frankfurt-postgres.render.com/phonebook_and_snake", sslmode='require')
cur = conn.cursor()


def get_all_data():
    cur.execute("SELECT * FROM snakegame ORDER BY user_score DESC")
    rows = cur.fetchall()
    for row in rows:
        print(f"Username = {row[0]} Score = {row[1]} Level = {row[2]}")

get_all_data()
