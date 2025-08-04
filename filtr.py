import sqlite3

def serch_by_artist(cursor):
    name = input("Введіть ім'я виконавця: ").strip()
    cursor.execute("" \
        "SELECT Album.Title " \
        "FROM Album " \
        "JOIN Artist ON Album.ArtistId = Artist.ArtistId " \
        "WHERE Artist.Name LIKE ? "
        "", (f"%{name}%",))
    
    results = cursor.fetchall()
    for row in results:
        print("-", row[0])

def search_by_genre(cursor):
    genre = input("Введіть жанр: ").strip()
    cursor.execute("" \
        "SELECT Track.Name " \
        "FROM Track " \
        "JOIN Genre ON Track.GenreId = Genre.GenreId " \
        "WHERE Genre.Name LIKE ? " \
        "", (f"%{genre}%",))
    result = cursor.fetchall()
    for row in result:
        print("-", row[0])

def main():
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    cursor = conn.cursor()

    while True:
        print("\n Меню пошуку: ")
        print("1. Пошук альбомів за виконавцем")
        print("2. Пошук альбомів за жанром")
        print("3. Вийти")
        choice =input("Ваш вибір: ")

        if choice == "1":
            serch_by_artist(cursor)
        elif choice == "2":
            search_by_genre(cursor)
        elif choice == "3":
            break
        else:
            print("Невідома команда")

    conn.close()

if __name__ == "__main__":
    main()

