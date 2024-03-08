#Nhi Tran

def wordInRange():

    file_path = input().strip()
    lower_bound = input().strip()
    upper_bound = input().strip()
 
    with open(file_path, 'r') as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    for word in words:
        if lower_bound <= word <= upper_bound:
            print(f'{word} - in range')
        else:
            print(f'{word} - not in range')

if __name__ == '__main__':
    wordInRange()