# import pymongo
# pymongo.MongoClient(MONGODB_URI+"ytmanager")

from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(MONGODB_URI+"ytmanager", tlsAllowInvalidCertificates=True) # not a good way to handle SSL certificate issue

db = client["ytmanager"]
video_collection = db["videos"]

def list_videos():
    for video in video_collection.find():
            print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(new_video_name, new_video_duration):
    video_collection.insert_one({new_video_name, new_video_duration})

def update_video(video_id, new_video_name, new_video_duration):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"video_name": new_video_name, "video_duration": new_video_duration}}
    )

def delete_video(video_id):
   video_collection.delete_one({'_id': ObjectId(video_id)})

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