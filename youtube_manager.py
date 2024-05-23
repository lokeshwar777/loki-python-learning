import json

fileName = 'youtube.txt'

def load_data():
    try:
        with open(fileName, 'r') as file:
            test = json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(fileName, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print('*' * 77)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['video_name']} {video['video_duration']}")
    print('\n')
    print('*' * 77)

def add_video(videos):
    video_name = input("Enter video name: ")
    video_duration = input("Enter the duration: ")
    videos.append({'video_name': video_name, 'video_duration': video_duration})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if (1 <= index <= len(videos)):
        new_video_name = input("Enter the new video name: ")
        new_video_duration = input("Enter the new video duration: ")
        videos[index-1] = {'video_name': new_video_name, 'video_duration': new_video_duration}
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if (1 <= index <= len(videos)):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

def main():

    videos = load_data()

    while True:
        print("\nYoutube Manager \nChoose an option:")
        print("1. List a fav video")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice :")
        print(videos)

        match(choice):
            case '1':
                list_all_videos(videos)
                
            case '2':
                add_video(videos)
                
            case '3':
                update_video(videos)
                
            case '4':
                delete_video(videos)
                
            case '5':
                break
            
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()