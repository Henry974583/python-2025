import io
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
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Septemper', 'October', 'November', 'December']
    
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
    MORSE_ALAPHABET = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--','-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••','•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••', '---••', '----•', '-----']
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
            morse_letter = MORSE_ALAPHABET[letter_index]
            final_string += morse_letter + ' '
        else:
            final_string += ' '
        
    print('\n' + final_string)
    


def phone_converter():
    #accepts no arguments
    #takes input from user that is only in telephone format
    #it then coverts the telephone number if it has letters in it
    
    #variables and list
    again = True
    final_string = ""
    NUMBER_ALPHABET = ["2", "2", "2", "3", "3", "3", "4", "4", "4", "5", "5", "5", "6", "6", "6", "7", "7", "7", "8", "8", "8", "9", "9", "9", "9"]
    ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

   #loop for if they make a mistake
    while again == True:
        #ask for input
        number = input("Enter a telephone number in the form of XXX-XXX-XXXX: ")
        #split to a list
        number_list = number.split("-")
        #verify it follows every rule
        if len(number_list) == 3:
            if len(number_list[0]) == 3 and len(number_list[1]) == 3 and len(number_list[2]) == 4:
                for row in number_list:
                    #get each letter
                    for letter in row:
                        if letter.lower() in ALPHABET:
                            #translate them
                            letter = letter.lower()
                            letters_index = ALPHABET.index(letter)
                            number = NUMBER_ALPHABET[letters_index]
                            #add them to final string
                            final_string += number
                        else:
                            final_string += letter
                    if row != number_list[2]:
                        #add a spacer
                        final_string += "-"
                #print final number and set again to false
                print(f"Here is your converted telephone number: {final_string}")
                again = False
def avg_num_words():
    #accetps no arguments
    #it open file text.txt
    #and checks how many words are in it
    #how many sentences
    #and the average number of words per sentence
    
    #variables
    outfile = open('text.txt', 'r')
    sentences = 0
    words = 0
    
    #count for each line
    for line in outfile:
        #create the line
        line = line.rstrip('\n')
        #split it
        line_list = line.split(' ')
        words += len(line_list)
        sentences += 1
        
    average = words / sentences
    #print
    print(f'The file text.txt has {words} words')
    print(f'There are {sentences} total sentences.')
    print(f'The average number of words per sentence is {average}')
def igpay_atinlay():
    #accepts no arguements
    #it ask the user for a sentence in english
    #and converts it to pig latin
    
    #vairable
    final_string = ''
    #input
    string = input('Enter a message to convert to pig latin: ')
    my_list = string.split(' ')
    
    for word in my_list:
        #reset the period and check for one
        period = False
        if '.' in word:
            #replace period with nothing
            word = word.replace('.', '')
            period = True
            
        #get the first letter
        first_letter = word[0]
        
        #add to the string
        word += first_letter
        
        #remove letter at the start
        word = word[1:]
        
        #add the letter ay to the begining of the word
        word += 'AY'
        
        if period == True:
            word += '.'
            
        #add to the final string
        final_string += word + ' '
        
    print(final_string.upper())
    
def pb_main():
    #accepts no arguments
    #runs the powerball
    #and calls other functions accordolying
    
    #call frequency
    #Get the frequency and pb_frequency lists
    frequency, pb_freq = pb_frequency()
    
    #get the most common numbers
    most_common_freq, most_common_pb = pb_most_common(frequency, pb_freq)
    minimum_freq, minimum_pb_freq = pb_least_common(frequency, pb_freq)
    
    #sort each list
    most_common_freq.sort()
    most_common_pb.sort()
    minimum_freq.sort()
    minimum_pb_freq.sort()
    
    #print out the numbers
    print("The most common lottery numbers are:")
    for num in most_common_freq:
        print(num)
    print()
    
    print("The most common powerball numbers are:")
    for num in most_common_pb:
        print(num)
    print()
    
    print("The least common lottery numbers are:")
    for num in minimum_freq:
        print(num)
    print()
    
    print("The least common powerball numbers are:")
    for num in minimum_pb_freq:
        print(num)

def pb_most_common(frequency, pb_freq):
    #accepts no arguments
    #it determines the 10 most common numbers
    #and orders them by frequency
    
    #initalize variables
    maximum = 0
    maximums = []
    pb_maximums = []
    frequency_copy = []
    pb_freq_copy = []
    
    #copy frequencies
    for num in frequency:
        frequency_copy.append(num)
    
    for num in pb_freq:
        pb_freq_copy.append(num)
    
    #get the maxium list
    for num in range(0, 10):
        for num in frequency_copy:
            if num > maximum:
                maximum = num
            if maximum == 0:
                break
        maximum_index = frequency_copy.index(maximum)
        frequency_copy[maximum_index] = 0
        
        maximums.append(maximum_index + 1)
        
        maximum = 0
    
    #get powerball maximum list
    for num in range(0,10):
        for num in pb_freq_copy:
            if num > maximum:
                maximum = num
            if maximum == 0:
                break
        maximum_index = pb_freq_copy.index(maximum)
        pb_freq_copy[maximum_index] = 0
        
        pb_maximums.append(maximum_index + 1)
        
        maximum = 0
    
    #return them
    return maximums, pb_maximums

def pb_least_common(frequency, pb_freq):
    #accepts no arguments
    #determines the 10 least common numbers
    #and orders them by frequency
    
    #variables
    minimum = 100
    minimums = []
    pb_minimums = []
    frequency_copy = []
    pb_freq_copy = []
    
    #copy frequencies
    for num in frequency:
        frequency_copy.append(num)
    for num in pb_freq:
        pb_freq_copy.append(num)
    
    #get minimums
    for num in range(0,10):
        for num in frequency_copy:
            if num < minimum:
                minimum = num    
        index = frequency_copy.index(minimum)
        frequency_copy[index] = 100
        
        minimums.append(index + 1)
        minimum = 100
    
    #get minimum powerballs
    for num in range(0,10):
        for num in pb_freq_copy:
            if num < minimum:
                minimum = num        
        index = pb_freq_copy.index(minimum)
        pb_freq_copy[index] = 100
        
        pb_minimums.append(index + 1)
        minimum = 100
    
    #return
    return minimums, pb_minimums

def pb_frequency():
    #accepts no arguemts
    #determines how much each numbers 1-69 was drawn
    #and each powerball was drawn
    NUMBERS = []
    frequency = []
    PB_NUMBERS = []
    pb_freq = []
    
    #generate the lists
    for num in range(0, 69):
        NUMBERS.append(num)
        frequency.append(0)
    
    for num in range(0, 25 + 1):
        PB_NUMBERS.append(num)
        pb_freq.append(0)
    
    
    #open the file
    outfile = open("pbnumbers.txt", "r")
    
    #make each lien a list
    for line in outfile:
        line_list = line.split(" ")
        line_list[5] = line_list[5].rstrip("\n")
        
        
        for number in range(0,4+1):
            num = int(line_list[number])
            num_index = NUMBERS.index(num - 1)
            frequency[int(num_index)] += 1
        #add pb frequency to pb list
        num = int(line_list[5])
        num_index = NUMBERS.index(num -1)
        pb_freq[int(num_index)] += 1
    
    #return the frequency lists
    return frequency, pb_freq

def gas_price():
    #accepts no arguments
    #finds the average price per year
    #and outputs 4 things
    #average price per year
    #highest and lowest price
    #list of prices from lowest to highest
    #and list of prices highest to lowest
    
    gas = open("GasPrices.txt", "r")
    
    # preset counter and total
    total = 0.0
    counter = 0
    # split up the line, making it into lists
    line = gas.readline()
    line_list = line.split("-")
    line_list[2] = line_list[2].split(":")
    line_list[2][1] = line_list[2][1].rstrip("\n")
    
    # set price and date variables
    price = line_list[2][1]
    date = line_list[2][0]
    
    # add the price to the total, and add onto counter, setting old date for loop
    total += float(price)
    counter += 1
    old_date = date
    
    # read each line in the file and split it
    for line in gas:
        line_list = line.split("-")
        line_list[2] = line_list[2].split(":")
        line_list[2][1] = line_list[2][1].rstrip("\n")
        
        # set price and date
        price = line_list[2][1]
        date = line_list[2][0]
        
        # check if the date matches
        if date == old_date:
            total += float(price)
            counter += 1
        else:
            # get the average and reset the old date and counter.
            average = total / counter
            print(f"The average price in {old_date} was ${average:.2f}.")
            
            total = float(price)
            counter = 1
            old_date = date
    # print final prices
    print(f"The average price in {old_date} was ${average:.2f}.")
    gas.close()