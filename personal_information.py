#Make an array using the dictionary format
#Ask user for input inside a loop where they will be asked if they want to input another entry, which they could only answer with "Yes" and "No"
#Ask user to input information again when, "Yes"
#Find and print the oldest

informations = {}

while True:
    input_name = input("Enter name: ")

    while True:
        try:
            input_age = int(input("Enter age: "))
            break
        except:
            print("Enter a valid age ")
            
    informations[input_name] = None

    add_name = input("Would you like to add more names? (Y/N) ").upper()
    if add_name == 'Y':
        continue
    elif add_name == 'N':
        print("Here are the names and ages you entered: ", list(informations.keys()))
        break
    else:
        print("Invalid input")