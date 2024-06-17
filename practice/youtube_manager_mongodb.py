# import pymongo
# pymongo.MongoClient(MONGODB_URI+"ytmanager")

from pymongo import MongoClient

client = MongoClient(MONGODB_URI+"")

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def main():
    while True:
        

if __name__ == "__main__":
        main()