import sqlite3

def connect():
    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, title text, publisher text, year integer, UPC integer)")
    connection.commit()
    connection.close()

def insert(title, publisher, year, upc):
    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO game VALUES (NULL, ?, ?, ?, ?)", (title, publisher, year, upc))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM game")
    rows = cursor.fetchall()
    connection.close()
    return rows

def search(title="", publisher="", year="", upc=""):
    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM game WHERE title=? OR publisher=? or year=? or upc=?",(title, publisher, year, upc))
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(id):
    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM game WHERE id=?", (id,))
    connection.commit()
    connection.close()

def update(id, title,publisher, year, upc):
    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE game SET title=?, publisher=?, year=?, upc=? WHERE id=?", (title, publisher, year, upc, id))
    connection.commit()
    connection.close()

connect()
