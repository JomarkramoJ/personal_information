#Make an array using the dictionary format
#Ask user for input inside a loop where they will be asked if they want to input another entry, which they could only answer with "Yes" and "No"
#Ask user to input information again when, "Yes"
#Find and print the oldest

name = {}
age = {}

while True:
    input_name = input("Enter name: ")
    name[input_name] = None

    add_name = input("Would you like to add more names? (Y/N) ").upper()
    if add_name == 'Y':
        continue
    elif add_name == 'N':
        print("Here are the names you entered: ", list(name.keys()))
        break
    else:
        print("Invalid input")

input_age = input("Enter age: ")