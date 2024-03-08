def fileNameChange():
    file_name = input().strip()
    with open(file_name, 'r') as file:
        photo_names = file.readlines()
    for photo_name in photo_names:
        modified_name = photo_name.strip().replace("_photo.jpg", "_info.txt")
        print(modified_name)

if __name__ == '__main__':
    fileNameChange()