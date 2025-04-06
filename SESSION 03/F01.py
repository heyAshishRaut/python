"""
Video's manager Project
"""



import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        return []


def saveDataHelper(vidoes):
    with open("youtube.text", "w") as file:
        json.dump(vidoes, file)


def listAllVideos(videos):
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. Video - {video["name"]}, Duration - {video["time"]}")


def addVideo(videos):
    name = input("Enter name - ")
    time = input("Enter time - ")
    videos.append({"name" : name, "time" : time})
    saveDataHelper(videos)


def updateVideo(videos):
    listAllVideos(videos)
    index = int(input("Enter video id"))
    if 1 <= index <= len(videos):
        name = input("Enter name - ")
        time = input("Enter time - ")
        videos[index - 1] = {"name" : name, "time" : time}
        saveDataHelper(videos)
    else:
        print("Invalid id")


def deleteVideo(videos):
    listAllVideos(videos)
    index = int(input("Enter video id"))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        saveDataHelper(videos)
    else:
        print("Invalid id")


def main():
    videos = load_data()
    while(True):
        print("Youtube Manager - Choose an option")

        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the app")

        choice = input("Enter choice - ")

        match choice:
            case "1":
                listAllVideos(videos)
            case "2":
                addVideo(videos)
            case "3":
                updateVideo(videos)
            case "4":
                deleteVideo(videos)
            case "5":
                break
            case "6":
                print("Invalid option")


if __name__ == "__main__":
    main()