
def count_t(): #program 8-1
    #accepts no arguments
    #it prompts the user for a word
    #and iterates through each letter
    #counting the number of upper and lower case t's
    #it outputs the total number of times it appeared in the word
    
    #input and counter
    word = str(input('Enter a word: '))
    iteration = 0
    
 
     #loop
    for letter in word:
        if letter  == "T" or letter == 't':
            iteration += 1
            
    print('The letter T or t appears', iteration, 'times in the word: ', word)
    
    
def concatenate(): #progarm 8-2
    #accepts no arguments
    #it concatentates and prints the two string
    #carmen adn sandiego
    
    #assing a string to a variable
    my_string = 'Where in the world is Carmen '
    
    #print it
    print(my_string)
    
    #concatentates it
    my_string += 'Sandiego'
    
    #print it for the final time
    print(my_string)
    
def get_login_name(first, last, idnumber): #prgoram 8-3
    #accepts 3 arguments first last and idnumber
    #it creates separate substings of the first 3 letters of both
    #the first name and last name and the last 3 characters of idnumber
    #it concatenates the strings in the order of first, last, id
    #and returns the genrated login
    
    part1 = first[0:3]
    part2 = last[0:3]
    part3 = idnumber[-3:]
    
    #add them all togother
    login_name = part1 + part2 + part3
    
    #return
    return login_name
    
def generate_login(): #program 8-4
    #get login accepts no arguments
    #it prompts the user for a first name, last name and id number
    #it passes the values to login.get_login_name()
    #and recives the the new user login
    
    #get names and ids
    first = str(input('Enter your first name: '))
    last = str(input('Enter your last name: '))
    idnumber = str(input('Enter your id number: '))
    
    #call function
    login_name = get_login_name(first, last, idnumber)
    
    #header and info
    print('Your system login name is:')
    print(login_name)
    
    
def string_test(): #program 8-5
    #accepts no arguments
    #it takes input from the user in form of a string
    #and performs a variiety test on the string
    
    #input
    string = input('Enter a string to be tested: ')
    
    #testing
    if string.isalum():
        print('The string only contains alphanumeric charcters.')
    if string.isdigit():
        print('The string only contains digits.')
    if string.isalpha():
        print('The string only contains alpha characters.')
    if string.isspace():
        print('The string only contains whitespaces.')
    if string.islower():
        print('The string is all lower case.')
    if string.isupper():
        print('The string is all upper case.')
        
    print()
    print("your string conveted to all uppercase is: ", string.upper())
    print('Your string converted to all lowercas is: ', string.lower())
    
def valid_password(password): #program 8-6
    #accepts a string for password
    #it test the follwoing conditoins
    #is password at least 7 characters
    #does password have at least one lowercase letter
    #does password have at least one digit (numeric)
    #if the password meets all conditions is_valid is true
    #valid_password retrunis valid
    
    length = False
    upper = False
    lower = False
    digit = False
    
    if len(password) >= 7:#if more or equal to 7 characters
        length = True
        
        #loop
        for ch in password:
            #check if each indidual characters is upper case
            if ch.isupper():#if character has upper case upper = True
                upper = True
            #checks to see if each character is lower case
            if ch.islower():#if character has lower case lower = true
                lower = True
            #checks for numbers to see if their is any in each character
            if ch.isdigit(): #if character has number digit = true
                digit = True
                
    #test
    if length and upper and lower and digit:
        valid = True
    else:
        valid = False
        
    return valid

def validate_password(): #program 8-7
    #accepts no arguments
    #it prompts the user for a password
    #and passes the password to login.valid_password
    #to loop while the password is invalid

    password = input('Please enter your password')
    
    valid_password(password)
    valid = valid_password(password)
    if valid == True:
        print('Password accepted')
    if valid == False:
        print('try again')
        validate_password()
        
def repetition(): #program 8-8
    #accepts no arguments
    #it myltipis z by range 1-10
    #then multiples z by rangbe 8-0-1
    
    #print
    for count in range(1,10):
        print('z' * count)
    for count in range(8, 0, -1):
        print('z' * count)
        