import sqlite3

# Підключення до БД
connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS Animals (ID INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Type TEXT);""")

cur.execute("INSERT INTO Animals (Name, Type) VALUES ('Лев', 'Ссавець');")
cur.execute("INSERT INTO Animals (Name, Type) VALUES ('Крокодил', 'Плазун');")
cur.execute("INSERT INTO Animals (Name, Type) VALUES ('Орел', 'Птах');")
cur.execute("INSERT INTO Animals (Name, Type) VALUES ('Морська черепаха', 'Плазун');")
cur.execute("INSERT INTO Animals (Name, Type) VALUES ('Мавпа', 'Ссавець');")

cur.execute("SELECT ID, Name, Type FROM Animals;")
before_update = cur.fetchall()
print("База даних до змін:")
print(before_update)

cur.execute("UPDATE Animals SET Name='Сокіл' WHERE Name='Орел';")

cur.execute("SELECT ID, Name, Type FROM Animals;")
after_update = cur.fetchall()
print("\nБаза даних після змін:")
print(after_update)

cur.execute("SELECT ID, Name, Type FROM Animals WHERE Type='Ссавець';")
mammals = cur.fetchall()
print("\nСсавці:")
print(mammals)

connection.commit()
connection.close()