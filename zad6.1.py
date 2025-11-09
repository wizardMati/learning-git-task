import sqlite3

DB_NAME = "car.db"

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marka TEXT,
    model TEXT,
    kolor TEXT,
    rok_wydania INTEGER,
    cena INTEGER
)
""")

conn.commit()
conn.close()


def car_add(marka, model, kolor, rok_wydania, cena):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO cars (marka, model, kolor, rok_wydania, cena) VALUES (?, ?, ?, ?, ?)",
              (marka, model, kolor, rok_wydania, cena))
    conn.commit()
    conn.close()


def show_car():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM cars")
    cars = c.fetchall()
    conn.close()
    print("\nLista aut:")
    for row in cars:
        print(row)


def update_car(id, nowa_cena):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE cars SET cena=? WHERE id=?", (nowa_cena, id))
    conn.commit()
    conn.close()


def delete_car(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM cars WHERE id=?", (id,))
    conn.commit()
    conn.close()


car_add("Toyota", "Corolla", "niebieski", 2015, 120000)
car_add("BMW", "E46", "czarny", 2003, 15000)
car_add("Audi", "A4", "srebrny", 2010, 21000)

show_car()

update_car(2, 10000)
print("\nDane po aktualizacji ceny BMW:")
show_car()

delete_car(2)
print("\nLista aut po usunięciu BMW:")
show_car()

