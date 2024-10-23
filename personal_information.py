#Make an array using the dictionary format
informations = {}

#Ask user input for name and age
while True:
    input_name = input("Enter name: ")
    if not input_name.isalpha():
        print("Please enter a valid name")
        continue

    while True:
        try:
            input_age = int(input("Enter age: "))
            break
        except:
            print("Enter a valid age ")
            
    informations[input_name] = input_age

#Ask user for input inside a loop where they will be asked if they want to input another entry, which they could only answer with "Yes" and "No"
    while True:
        add_name = input("Would you like to add more names? (Y/N) ").upper()
        if add_name == 'Y':
            break
        elif add_name == 'N':
            print("Here are the names and ages you entered: ", informations)
            break
        else:
            print("Invalid input")
            
    if add_name == 'N':
        break

#Find and print the oldest
if informations:
    oldest = max(informations, key=informations.get)
    print(f"The oldest is: {oldest} which is {input_age} years old")