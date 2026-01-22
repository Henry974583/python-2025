import random
import os
def lottery(): #exercise 2
    #accepts no arguments
    #it generates a list of random numbers
    #and prints them
    
    #list
    numbers = []
    #header
    print('Generating lotto numbers...')
    print('Here are your lotto number')
    #generate the numbers
    for lotto in range (7):
        number = random.randint(0, 9)
        #append it
        numbers.append(number)
        
    #print the numbers
    for lottery in numbers:
        print(lottery)
        
def rainfall(): #exercise 3
    #accepts no arguments
    #it ask for data once per a month
    #it then adds it to a list
    #lastly it finds the MIN, MAX, Total, and average
    
    #lists
    data = []
    months = ["January: ", "February: ", 'March: ', 'April: ', "May: ", 'June: ', 'July: ', 'Aufust: ', 'September: ', 'October: ', 'November: ', 'December: ']
    
    #loop for info
    for month in months:
        #INPUT
        inches = int(input((month)))
        #append
        data.append(inches)
        
    #math
    most = max(data)
    least = min(data)
    total = sum(data)
    average = total / len(data)
    print()
    #statments to find the what month had the most
    
    if most == data[0]:
        print('January had the most with', most, 'inches of rainfall.')
    elif most == data[1]:
        print('Febuary had the most with', most, 'inches of rainfall.')
    elif most == data[2]:
        print('March had the most with', most, 'inches of rainfall.')
    elif most == data[3]:
        print('April had the most with', most, 'inches of rainfall.')
    elif most == data[4]:
        print('May had the most with', most, 'inches of rainfall.')
    elif most == data[5]:
        print('June had the most with', most, 'inches of rainfall.')
    elif most == data[6]:
        print('July had the most with', most, 'inches of rainfall.')
    elif most == data[7]:
        print('August had the most with', most, 'inches of rainfall.')
    elif most == data[8]:
        print('September had the most with', most, 'inches of rainfall.')
    elif most == data[9]:
        print('October had the most with', most, 'inches of rainfall.')
    elif most == data[10]:
        print('November had the most with', most, 'inches of rainfall.')
    elif most == data[11]:
        print('December had the most with', most, 'inches of rainfall.')
        
    #find the least
    if least == data[0]:
        print('January had the least with', least, 'inches of rainfall.')
    elif least == data[1]:
        print('Febuary had the least with', least, 'inches of rainfall.')
    elif least == data[2]:
        print('March had the least with', least, 'inches of rainfall.')
    elif least == data[3]:
        print('April had the least with', least, 'inches of rainfall.')
    elif least == data[4]:
        print('May had the least with', least, 'inches of rainfall.')
    elif least == data[5]:
        print('June had the least with', least, 'inches of rainfall.')
    elif least == data[6]:
        print('July had the least with', least, 'inches of rainfall.')
    elif least == data[7]:
        print('August had the least with', least, 'inches of rainfall.')
    elif least == data[8]:
        print('September had the least with', least, 'inches of rainfall.')
    elif least == data[9]:
        print('October had the least with', least, 'inches of rainfall.')
    elif least == data[10]:
        print('November had the least with', least, 'inches of rainfall.')
    elif least == data[11]:
        print('December had the least with', least, 'inches of rainfall.')
        
    #print the total and average
    print('Total rain for the year:', total, 'inches')
    print('Average rain per month:', average, 'inches')
    
def charge_accts(): #exercise 5
    #accepts no argument
    #asks for a number
    #and checks if it in a list
    #it also checks that they are valid numbers
    #open file and variables
    account = []
    go = 'y'
    infile = open('charge_accounts.txt', 'r')
    
    
    if go == 'y':
        account_number = input('type a account number ')
        
    while account_number.isdigit() == False:
        account_number = input('Enter and account number(numerics only) ')
        
    on_list == isValid(account_number)
    
    if on_list == 'valid':
        print('the account number is valid')
    else:
        print('The account is invalid')
        
    go = input('Go again? ')
    
    if go == 'y':
        charge_accts()
    
def isValid(account_number):
    for acc in infile:
        acc = r.strip('\n')
        accounts.append(acc)
        
    infile.close()
    
    if account_number not in accounts:
        return on_list == 'invalid'
    else:
        return on_list == 'valid'
    
def drivers_exam(): #exercise 4
    #no arguments
    #it reads from a file
    again = 'y'
    total = 20
    while again.lower() == 'y':
        #promt the user
        test_file = input('Please enter the name of the file ')
        
        if not os.path.exist(test_file):
            print(test_file, ' not found.')
        else:
            #start answer key
            answer_key = open('driver_test_key.txt', 'r')
            
            #open test file
            test_answers = open(test_file, 'r')
            
        #lists
            answers = []
            user_answers = []
            
            #create the list
            for line in answer_key:
                line = line.rstip('\n')
                user_answers.append(line)
                
            for line in test_answers:
                lin = line.rstrip('\n')
                user_answers.append(line)
                
            #wrong index
                
            wrong_index = []
            counter = -1
            correct = 0
            
            for ans in answer:
                counter += 1
                if ans == user_answers[counter]:
                    correct +=1
                else:
                    wrong_index.append(counter + 1)
                    
            print('Test complete')
            
            print('your answerd', correct, 'questions correctly out of total', total)
            
            missed = total - correct
            
            print('You missed', missed, 'the minium you could miss to pass was 5')
            
            if missed > 5:
                print('You did not pass')
            else:
                print('You passed')
                
            if missed == 0:
                print()
            else:
                print('Here ar the questions you missed', wrong_index)
                

def tic_tac_toe():
    #plays the game
    board = [['-', '-', '-',],
             ['-', '-', '-',],
             ['-', '-', '-',]]
    #print board
    for b in board:
        print(b)
        
    row = random.randint(0, 2)
    collum = random.randint(0, 2)
    board.remove[row][collum]
    board.append[row][collum]
    
    for b in board:
        print(b)
    
            