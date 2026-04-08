#program 10-19
import pickle
import contacts

def main():
    #accepts no arguments
    #calss load_contacts to get dictonary
    #calls functions based off of menu
    #and saves the contacts
    
    load_contacts()
    
    
    get_menu_choice()
    
    
def load_contacts():
    pass
def get_menu_choice():
    #accepts no arguments
    #it prints menu and decides what to run of that
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit')
    print()
    mycontacts = {}
    #input
    choice = int(input('Enter your selection: '))
    print()
    #if statments to run the right program
    if choice == 1:
        look_up(mycontacts)
        get_menu_choice()
    elif choice == 2:
        add(mycontacts)
        get_menu_choice()
    elif choice == 3:
        change(mycontacts)
        get_menu_choice()
    elif choice == 4:
        delete(mycontacts)
        get_menu_choice()
    elif choice == 5:
        print()
        print('goodbye')
        
    
def look_up(mycontacts):
    #accepts my contacts
    #prompts the user for a name to search for
    #and display the info associated with them
    
    for key in mycontacts.values():
        pritn(key)
    
def add(mycontacts):
    #accepts my contacts
    #prompts user for inputs
    #and adds them to a dictionary
    
    #inputs
    name = str(input('Name: '))
    phone = str(input('Phone: '))
    email = str(input('Email: '))
    
    #add them to dictionary
    mycontacts['Name'] = name
    mycontacts['Phone'] = phone
    mycontacts['Email'] = email
    
    return mycontacts
    
def change(mycontacts):
    pass
def delete(mycontacts):
    pass
def save_contacts(mycontacts):
    pass
main()