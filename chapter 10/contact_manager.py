#program 10-19
import pickle
import contacts
LOOK_UP =1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'
def main():
    #accepts no arguments
    #calss load_contacts to get dictonary
    #calls functions based off of menu
    #and saves the contacts
    
    mycontacts = load_contacts()
    
    #prime the loop
    selection = 0
    
    #process menu choice until chooses quit
    while selection != QUIT:
        #input
        selection = get_menu_choice()
    
        #procces menu selection
        if selection == LOOK_UP:
            look_up(mycontacts)
        elif selection == ADD:
            add(mycontacts)
        elif selection == CHANGE:
            change(mycontacts)
        elif selection == DELETE:
            delete(mycontacts)
        else:
            print('GOODBYE')
            
    save_contacts(mycontacts)
    
def load_contacts():
    #accepts no arguments
    #it opens the FILENAME and upickles the data
    #returns the dictonary
    
    try:
        #open file as binary
        infile = open(FILENAME, 'rb')
        
        #unpickle
        contact_dct = pickle.load(infile)
        
        #close the file
        infile.close()
        
    except:
        #file nout found
        contact_dct = {}
        
    return contact_dct
def get_menu_choice():
    #accepts no arguments
    #it prints menu and decides what to run of that
    
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit')
    print()
    
    try:
        selection = int(input('Enter your selection: '))
        
        #validate selection
        while selection < LOOK_UP or selection > QUIT:
            print('Please only choose a valid option from the menu')
            
    except:
        print("Please only choose a valid selectoin form the menu.")
        get_menu_choice()
        
    #do it better way
    return selection
def look_up(mycontacts):
    #accepts my contacts
    #prompts the user for a name to search for
    #and display the info associated with them
    
    #search input
    name = input('Enter a naem to look up: ')
    
    #look them up
    print()
    print(mycontacts.get(name, 'That name is not found.'))
          
def add(mycontacts):
    #accepts my contacts
    #prompts user for inputs
    #and adds them to a dictionary
    
    #inputs
    name = str(input('Name: '))
    phone = str(input('Phone: '))
    email = str(input('Email: '))
    
    entry = contacts.Contact(name, phone, email)
    
    #if the names not already in the dictonary add it
    if name not in mycontacts:
        mycontacts[name] = entry
        print('The entry has been added to the contact list.')
        
    else:
        print('That name already exists in the contact list.')
    
def change(mycontacts):
    #accepts my contacts
    #it promtps the user fo th ename of the contact to modify
    #if that name is inn the dictonary prompt the user for a new phone and email
    #and update the attributes for that object
    
    #get input from the user for name
    print()
    name = input('Enter a name to look up: ')
    
    #verify
    if name in mycontacts:
        #get a new phone and email
        print()
        phone = input('Enter a new phone number: ')
        email = input('Enter a new email: ')
        
        #create a new object with new info
        entry = contact.Contact(name, phone, email)
    
        #update the dictionary
        mycontacts[name] = entry
        print('Information updated.')
    
    else:
        print('That name was not found')
        print('-----------------------')
        
def delete(mycontacts):
    #accepts my contacts dictonary
    #it promtps the user for a name to delete
    #if that name is in the dictionary delete it
    
    #input for name
    name = input('Enter a name to look up: ')
    
    if name in mycontacts:
        del mycontacts[name]
        print('Entry deleted')
    else:
        print('That name was not found')
    
def save_contacts(mycontacts):
    #save contacts accepts dictonary mycontacts
    #it pickles the dictonarh to contacts.dat
    
    #open the file as binary write
    outfile = open(FILENAME, 'wb')
    
    #pickle dictonary and save
    pickle.dump(mycontacts, outfile)
    
    #close file
    outfile.close()
    
if __name__ == '__main__':
    main()
