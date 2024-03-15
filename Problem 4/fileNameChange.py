def fileNameChange():
    try:
        file_name = input("Enter the file name: ")  
        with open(file_name, 'r') as file:
            photo_names = file.readlines()
        
        for photo_name in photo_names:
            modified_name = photo_name.strip().replace("_photo.jpg", "_info.txt")
            print(modified_name)

    except FileNotFoundError:
        print("File not found. Please make sure the file exists and try again.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    fileNameChange()
