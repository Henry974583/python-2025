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
    
    if valid

def date_converter():
    #accepts no arguments
    #takes input of a date
    #validates all inputs are correct
    #and outputs the date
    pass
    
def morse_code_translator():
    #accepts no arguemts
    #takes input from user
    #and converts it to morse code
    #it also validates for only alphabetical numbers
    pass

def phone_converter():
    #accepts no arguments
    #takes input from user that is only in telephone format
    #it then coverts the telephone number if it has letters in it
    pass

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