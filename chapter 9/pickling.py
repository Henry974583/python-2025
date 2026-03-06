import pickle

def write_main(): # 9-4
    # pickle_main accepts no arguments
    # it opens the file info.dat for binary writing
    # it loops and calls save_data to prompt the user for information
    # to add user data to ta dictionary
    # and then prompts the user to continue
    
    # prime the loop
    again = 'y'
    
    # open the file for binary writing
    outfile = open("info.dat", "wb")
    
    # loop to get data until the user wants to stop
    while again.lower() == "y":
        # get and save data
        save_data(outfile)
        
        again = input("Enter more data (y/n): ")
        
    # data entry finished, close the file
    outfile.close()
    
def read_main(): #9-5
    # read main accepts no arguments
    # it opens info.data s a binary read file
    # loops to the end of the file and unpickles the data
    
    # prime the loop
    end_of_file = False
    
    # open file
    infile = open("info.dat", "rb")
    
    # loop to the end of the file
    while not end_of_file:
        try:
            # unpickle and display the next object
            person = pickle.load(infile)
            display_data(person)
        except EOFError:
            # end of file error reached, change the loop flag
            end_of_file = True
    
    # all data read, close the file
    infile.close()
    
def display_data(person):
    # display data accepts a person as a dictionary unpickled from the file
    # it displays the information for that person
    
    print("Name: ", person['name'])
    print("Age: ", person['age'])
    print("Weight: ", person['weight'])
    print()
    
def save_data(file):
    # save-data accepts file as an argument
    # it creates an empty dictionary and prompts the user for information
    # to add keys/values for name, age, and weight
    # it pickles the data to write to info.dat
    
    # create an empty dictionary
    person = {}
    
    # get data for name, age, weight, and pickle the data
    person['name'] = input("Name: ")
    person['age'] = int(input("Age: "))
    person['weight'] = float(input("Weight: "))
    
    # pickle the dictionary
    pickle.dump(person, file)