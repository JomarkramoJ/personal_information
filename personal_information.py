#Make an array using the dictionary format
informations = {}

def is_valid_name(input_string):
    if any(char.isdigit() for char in input_string):
        return False
    return True

#Ask user input for name and age
while True:
    while True:
        input_name = input("Enter name: ")
        if is_valid_name(input_name):
            break
        else:
            print("Invalid Name, Please don't include numbers")
    while True:
        try:
            input_age = int(input("Enter age: "))
            if input_age >= 123 and input_age <= 130:
                print("You now have the world record of being the oldest ever to live according to google")
                break
            elif input_age >= 0 and input_age <= 130:
                break
            else:
                print("invalid age")
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
    oldest_age = max(informations.values())
    oldest = [name for name, age in informations.items() if age == oldest_age]
    if len(oldest) > 1:
        print(f"The oldest people in the list are: {', '.join(oldest)}, all aged {oldest_age} years old.")
    else:
        print(f"The oldest is: {''.join(oldest)} which is {oldest_age} years old")