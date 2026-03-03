def birthday_main():
    # birthday main recieves no arguments
    # it presets a variable for the dictionary, then gets user choice
    
    # preset birthdays
    birthdays = dict()
    
    # get choice and find option
    choice = get_menu_choice()
    while choice != 5:
        if choice == 1:
            look_up(birthdays)
        elif choice == 2:
            add_bday(birthdays)
        elif choice == 3:
            change_bday(birthdays)
        elif choice == 4:
            delete_bday(birthdays)
        # recall the choice
        choice = get_menu_choice()
    
    print("Goodbye.")
    
def get_menu_choice():
    # get menu choice recieves no arguments
    # it gets the users menu choice
    # and returns it
    
    # preset variables
    go = True
    choice = ''
    
    # print headers
    print("\nFriends and their birthdays\n---------------------------\n1. Lookup\n2. Add a new birthday\n3. Change a birthday\n4. Delete a birthday\n5. Quit")
    
    # while they mess up, ask for another choice
    while True:
        try:
            # get choice
            choice = int(input("\nEnter a menu choice: "))
            
            # verify its an option
            if choice < 1 or choice > 5:
                print("Use only numbers on the list.")
            else:
                return choice
            
        except:
            print("Numbers only")
            
def look_up(birthdays):
    # look up recieves an argument for birthdays
    # it looks to see if the birthday is in the dictionary
    
    # find the person
    person = input("\nWho would you like to search for: ")
    
    # check if the list is empty
    if birthdays == {}:
        # print the error
        print("\nThere are no birthdays to search!")
    else:
        # get the date, and error if there is one
        date = birthdays.get(person, "Not found.")
        print(date)
        
def add_bday(birthdays):
    # add birthday recieves an argument for the dictionary of birthdays
    # it adds the users birthday and name into the dictionary
    # if there is already one, it outputs an errotr message.
    
    # ask for the name and birthday
    name = input("\nEnter a name: ")
    birthday = input("Enter a birthday: ")
    
    # check if their name is in the list
    if name in birthdays:
        # print error
        print("\nName already being used.")
    else:
        # add a birthday
        birthdays[name] = birthday
    

def change_bday(birthdays):
    # change bday recieves an argument for the dictionary if birthdays
    # it checks to see if the name is in the dictionary
    # then changes it to what the user wants.
    
    # get the person to change and a new birthday
    person = input("\nEnter a name to change the birthday for: ")
    birthday = input("Enter a new birthday: ")
    
    # check if theyre in and change it
    if person in birthdays:
        birthdays[person] = birthday
        print(f"\nBirthday changed for {person}.")
    else:
        # print error
        print(f"\n{person} not found.")

def delete_bday(birthdays):
    # delete birthday recieves an argument for the dictionary of bithdays
    # it deletes the person from the dictionary
    
    # ask for the person
    person = input("\nEnter a name to delete: ")
    
    # check if theyre in there and delete it
    if person in birthdays:
        del birthdays[person]
        print(f"\n{person} deleted.")
    else:
        # print error
        print(f"\n{person} not found.")

birthday_main()