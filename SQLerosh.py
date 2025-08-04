import sqlite3


conn = sqlite3.connect("Chinook_Sqlite.sqlite")
cursor = conn.cursor()

#cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#tables = cursor.fetchall()
#for table in tables:
#    print(table[0])

#cursor.execute("SELECT Album.Title, Artist.Name FROM Album JOIN Artist ON Album.ArtistId = Artist.ArtistId WHERE Album.Title LIKE 'A%'")
#albums = cursor.fetchall()
#with open("A_albums.csv", "w", newline='', encoding="utf-8") as file:
#        writer = csv.writer(file)
#        writer.writerow(["Альбоми на А"])
#
#        for album in albums:
#              print(album)


# cursor.execute("" \
#       "SELECT Artist.Name, COUNT(Album.AlbumId) AS AlbumCount "\
#       "FROM Artist " \
#       "JOIN Album ON Artist.ArtistId = Album.ArtistId " \
#       "GROUP BY Artist.Name " \
#       "ORDER BY AlbumCount DESC " \
#       "LIMIT 10; " \
#       "")

# albums = cursor.fetchall()

# for artist, count in albums:
#     print(f"Artist: {artist} — Albums: {count}")


cursor.execute("" \
      "SELECT genre.NAME, COUNT(Track.TrackId) AS TrackCount " \
      "FROM Genre " \
      "JOIN Track ON Genre.GenreId = Track.GenreId " \
      "GROUP BY Genre.Name " \
      "ORDER BY TrackCount DESC;")
tracks = cursor.fetchall()

for track, count in tracks:
    print(f"Genre:{track} - {count}")