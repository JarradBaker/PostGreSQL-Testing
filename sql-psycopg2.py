import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Album"')

# query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 4 - select only the "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5 - select only the albums with "ArtistId" #51 from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "AlbumId" = %s', [51])

# query 6 - select all tracks from "Track" table where the composer is "Queen"
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# query 7 - query the database using a different (existing) composer
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Sykes"])

# query 8 - query the database using "test" as the composer
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])


# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
