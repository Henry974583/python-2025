def menu():
    #accepts no arguments
    #it ask user for input on what program
    #and runs it
    go_again = 'y'
    while go_again == 'y':
        #print header
        print('1) Sum of digits')
        print('2) Date converter')
        print('3) Morse code')
        print('4) Telephone number')
        print('5) Average number of word')
        print('6) Pig latin')
        print('7) Powerball')
        print('8) Gas price')
        print()
        #take input
        choice = int(input('What program do you want to run: '))
        print()
        #if statements
        if choice == 1:
            sum_of_digits()
            go_again = input('Run another progarm? (y/n) ')
            print()
        elif choice == 2:
            date_converter()
            go_again = input('Run another program? (y/n) ')
            print()
        elif choice == 3:
            morse_code_translator()
            go_again = input('Run another program? (y/n) ')
            print()
        elif choice == 4:
            phone_converter()
            go_again = input('Run another program? (y/n) ')
            print()
        elif choice == 5:
            avg_num_words()
            go_again = input('Run another program? (y/n) ')
            print()
        elif choice == 6:
            igpay_atinlay()
            go_again = input('Run another program? (y/n) ')
            print()
        elif choice == 7:
            pb_main()
            go_again = input('Run another program? (y/n) ')
            print()
        elif choice == 8:
            gas_price()
            go_again = input('Run another program? (y/n) ')
            print()
    
    #end loop
    if go_again == 'n':
        print('Goodbye')

def sum_of_digits():
    #accetps no arguments
    #takes input on a string of numbers
    #makes sure they only enter numbers
    #and outputs the total of the string
    
    #input
    string = str(input('Enter a string of digit numbers without spaces: '))
    
    #validate
    valid = string.isalnum()
    
    #if not valid
    while string.isdigit() != True:
        string = str(input('Enter a string of digit numbers only: '))
        
    total = 0
    
    for num in string:
        total += int(num)
        
    print('The total is', total)

def date_converter():
    #accepts no arguments
    #takes input of a date
    #validates all inputs are correct
    #and outputs the date
    
    again = True
    #confirm it follows all the formatting rules
    while again == True:
        date = input("Enter a date in the format mm/dd/yyyy: ")
        date_list = date.split("/")
        if len(date_list) == 3:
            if date_list[0].isdigit() == True and date_list[1].isdigit() == True and date_list[2].isdigit() == True:
                if int(date_list[0]) < 13 and int(date_list[1]) < 32:
                    if len(date_list[0]) == 2 and len(date_list[1]) == 2 and len(date_list[2]) == 4:
                        #set again boolean to false
                        again = False
                    else:
                        print("Make sure you follow the format.")
                else:
                    print("Make sure you follow the format.")
            else:
                print("Make sure you follow the format.")
        else:
            print("Make sure you follow the format.")
    
    #create the list of month
            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Septemper', 'October', 'November', 'December']
    
    #preset variables
    month_number = int(date_list[0])
    month = ''
    
    #find the month
    for month in MONTHS:
        month_index_number = MONTHS.index(month)
        if month_index_number + 1 == month_number:
            # save the real month
            real_month = month
    
    #print
    print(f"The date is: {real_month} {date_list[1]}, {date_list[2]}")
    
    
def morse_code_translator():
    #accepts no arguemts
    #takes input from user
    #and converts it to morse code
    #it also validates for only alphabetical numbers
    
    #assign list and variables
    alaphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    MORSE_ALPHABET = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--','-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••','•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••', '---••', '----•', '-----']
    valid = False
    bad = 0
    final_string = ''
    
    #loop for validation
    while valid == False:
        string = input('Enter a message to encode to morse cods: ')
        mylist = string.split(' ')
        
    
    #check that it is valid
        for word in string:
            if word.isalnum() == False:
                bad += 1
                
        if bad != 0:
            valid = False
            bad = 0
            
        else:
            valid = True
            
    #check each indvidual letter
    for letter in string:
        if letter in alaphabet:
            letter_index = alaphabet.index(letter)
            morse_letter = MORSE_ALPHABET[letter_index]
            final_string += morse_letter + ' '
        else:
            final_string += ' '
        
    print('\n' + final_string)
    


def phone_converter():
    #accepts no arguments
    #takes input from user that is only in telephone format
    #it then coverts the telephone number if it has letters in it
    
    #variables and list
    

def avg_num_words():
    #accetps no arguments
    #it open file text.txt
    #and checks how many words are in it
    #how many sentences
    #and the average number of words per sentence
    pass

def igpay_atinlay():
    #accepts no arguements
    #it ask the user for a sentence in english
    #and converts it to pig latin
    pass

def pb_main():
    #accepts no arguments
    #runs the powerball
    #and calls other functions accordolying
    pass

def pb_most_common():
    #accepts no arguments
    #it determines the 10 most common numbers
    #and orders them by frequency
    pass

def pb_least_common():
    #accepts no arguments
    #determines the 10 least common numbers
    #and orders them by frequency
    pass

def pb_frequency():
    #accepts no arguemts
    #determines how much each numbers 1-69 was drawn
    #and each powerball was drawn
    pass

def gas_price():
    #accepts no arguments
    #finds the average price per year
    #and outputs 4 things
    #average price per year
    #highest and lowest price
    #list of prices from lowest to highest
    #and list of prices highest to lowest
    pass

def list_gas_price():
    #accepts no arguments
    #it finds 3 things
    #the average
    #and average price per year
    #and returns them
    pass