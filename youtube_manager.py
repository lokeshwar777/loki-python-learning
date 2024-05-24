import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_videos():
    print('\n')
    print('*' * 77)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
            print(row)

def add_video(new_video_name, new_video_duration):
    cursor.execute("INSERT INTO videos (video_name, video_duration) VALUES (?, ?)", (new_video_name, new_video_duration))
    con.commit()

def update_video(video_id, new_video_name, new_video_duration):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (video_id, new_video_name, new_video_duration))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()

def main():

    while True:
        print("\nYoutube Manager \nChoose an option:")
        print("1. List a fav video")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice :")

        match(choice):
            case '1':
                list_videos()
                
            case '2':
                video_name = input("Enter video name: ")
                video_duration = input("Enter the duration: ")
                add_video(video_name, video_duration)
                
            case '3':
                video_id = int(input("Enter the video number to update: "))
                new_video_name = input("Enter the new video name: ")
                new_video_duration = input("Enter the new video duration: ")
                update_video(video_id, new_video_name, new_video_duration)
                
            case '4':
                video_id = int(input("Enter the video number to be deleted: "))
                delete_video(video_id)
                
            case '5':
                break

            case _:
                print("Invalid Choice")

    con.close()

if __name__ == "__main__":
    main()