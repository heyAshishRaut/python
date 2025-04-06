"""
SQLite
"""



import sqlite3

con = sqlite3.connect("DATABASE.db")

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    )
''')


def listVideos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def addVideo(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()


def updateVideo(newName, newTime, videoID):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (newName, newTime, videoID))
    con.commit()


def deleteVideo(videoID):
    cursor.execute("DELETE FROM videos where id = ?", (videoID))
    con.commit()


def main():
    while True:
        print("Youtube Manager - SQLite")

        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the app")

        choice = input("Enter choice - ")

        if choice == "1":
            listVideos()

        elif choice == "2":
            name = input("Enter name - ")
            time = input("Enter time - ")
            addVideo(name, time)

        elif choice == "3":
            videoID = input("Enter ID - ")
            name = input("Enter name - ")
            time = input("Enter time - ")
            updateVideo(name, time, videoID)

        elif choice == "4":
            videoID = input("Enter ID - ")
            deleteVideo(videoID)

        elif choice == "5":
            break

        else:
            print("Invalid option")

    con.close()


if __name__ == "__main__":
    main()

