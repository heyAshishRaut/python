from pymongo import MongoClient
from bson import ObjectId



client = MongoClient("MONGODB_STRING"
, tlsAllowInvalidCertificates = True) #  It allows connections even if the SSL certificate is invalid or self-signed.

db = client["PYTHON_PROJECT"]
videoCollection = db["video"]

def listVideos():
    for video in videoCollection.find():
        print(f"{video["_id"]}, Name - {video["name"]}, and Time - {video["time"]}")

def addVideo(name, time):
    videoCollection.insert_one({"name" : name, "time" : time})

def updateVideo(videoID, name, time):
    videoCollection.update_one({"_id" : ObjectId(videoID)},
        {"$set" : {"name" : name, "time" : time}}
    )

def deleteVideo(videoID):
    videoCollection.delete_one({"_id" : ObjectId(videoID)})

def main():
    while True:
        print("Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")
        choice = input("Enter your choice - ")

        if choice == "1":
            listVideos()

        elif choice == "2":
            name = input("Enter name - ")
            time = input("Enter time - ")
            addVideo(name, time)
        
        elif choice == "3":
            videoID = input("Enter video ID - ")
            name = input("Enter name - ")
            time = input("Enter time - ")
            updateVideo(videoID, name, time)

        elif choice == "4":
            videoID = input("Enter video ID - ")
            deleteVideo(videoID)

        elif choice == "5":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()