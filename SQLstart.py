import sqlite3

libr = sqlite3.connect("library.db")
cursor = libr.cursor()

# Створили бібліотеку
cursor.execute("" \
"CREATE TABLE IF NOT EXISTS library (" \
"id INTEGER PRIMARY KEY, " \
"title TEXT," \
"author TEXT," \
"year INTEGER)")

libr.commit()

# Створили данні
cursor.execute("INSERT INTO library(id, title, author, year) VALUES (?, ?, ?, ?)", (12345, "1984", "George Orwell", 1949))
cursor.execute("INSERT INTO library(id, title, author, year) VALUES (?, ?, ?, ?)", (12346, "Sherlock Golms", "Artur C. Doil", 1800))
cursor.execute("INSERT INTO library(id, title, author, year) VALUES (?, ?, ?, ?)", (12347, "White Fang", "Jack London", 2010))

libr.commit()

# Вивели данні
cursor.execute("SELECT * FROM library")
books = cursor.fetchall()

for book in books:
    print(book)

# Оновили данні
cursor.execute("UPDATE library SET year = ? WHERE title = ?", (1950, "1984"))
libr.commit()

# Вивели оновлені данні
cursor.execute("SELECT * FROM library")
books = cursor.fetchall()

for book in books:
    print(book)

# Видалили данні
cursor.execute("DELETE FROM library WHERE id = ?", (12345,))
libr.commit()

# Вивели оновлені данні
cursor.execute("SELECT * FROM library")
books = cursor.fetchall()

for book in books:
    print(book)

# Вивели вибіркові данні
cursor.execute("SELECT * FROM library WHERE year = ?", (2010,))
books = cursor.fetchall()

for book in books:
    print(book)

libr.close()