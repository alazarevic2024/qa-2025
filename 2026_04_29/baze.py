import mysql.connector as conn
import json

connection = conn.connect(
    host="localhost",
    user="root",
    password="", #uneti svoj password
    database="sakila"
)
print("KONEKCIJA ")
kursor = connection.cursor()
kursor.execute("select title, release_year from film limit 10;")
filmovi = kursor.fetchall()

print("Filmovi u ponudi:")
for title, release__year in filmovi:
    print(f"Naziv: {title}, Godina: {release__year}")

json_podaci = json.dumps(filmovi, indent=4)
print(json_podaci)

connection.close()