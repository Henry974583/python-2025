import io
import random
def line_numbers(): #exercise 3
    #accepts no arguemtns
    #it opens file steps.txt
    #and reads them
    #finally it prints them and assgins them a day

   #counter
    counter = 0
    try:
        #open file
        infile = open('steps.txt', 'r')
        
        #start loop
        for steps in infile:
            #read line
            linenumber = infile.readline()
            #strip the line
            linenumber = linenumber.rstrip()
            #increase counter
            counter += 1
            #print
            print(counter, ':\t', linenumber)
        
        #close the file
        infile.close()
        #in case of error
    except IOError:
        print('Error: File not found')
        

def line_counter(): #excercise 4
    #accepts no arguments
    #it ask the user for a file name
    #and opens it
    #it then counts how many lines are in the file
    #and outputs how many are there
    
    #variables
    counter = 0
    
    #Inputs
    filename = input('Enter the file name to read: ')
    try:
        infile = open(filename, 'r')
        
        #count how many lines of text their are
        for names in infile:
            counter += 1
            
        #print
        print(filename, 'contains', counter, 'lines')
        
        #close file
        infile.close()
        #eceptions
    except IOError:
        print('Error: No such file or directory: ', filename)
        
def average_of_numbers(): #excercise 6
    #accepts no arguements
    #opens numbers.txt
    #it finds the number of items in a file
    #and adds them all to find the average
    
    #variable
    counter = 0
    total = 0
    try:
        #inputs
        filename = input('Enter the file name to read: ')
        #open file
        infile = open(filename, 'r')
        
        #read the lines and add to find total
        for numbers in infile:
            numbers = int(numbers)
            total = numbers + total
            counter += 1
        
        #find the average
        average = total // counter
        
        #close file
        infile.close()
        
        #print info
        print('There were', counter, 'items with and average value of', average)
        
    #If file not found
    except IOError:
        print('Error: file named', filename, 'not found')
        
def ran_num_writer(): #excecise 7
    #accepts no arguments
    #it opens ran_numbers.txt
    #ask a input for number of numbers to generate
    #and writes them
    
    #variables
    MIN = 1
    MAX = 500
    
    try:
        #open file
        infile = open('ran_numbers.txt', 'w')
        
        #inputs
        iterations = int(input('How many numbers do you want to generate? '))
        
        #validation
        while iterations < 0:
            iterations = int(input("Please type a valid number "))
        #loop for number of iterations
        for numbers in range(iterations):
            num = random.randint(MIN, MAX)
            
            #write the numbers in the file
            infile.write(str(num) + '\n')
        
        #close the file
        infile.close()
    
        print('All numbers wiritten to ran_numbers_list')
    
    #errors
    except IOError:
        print('Error: file not found')
    except ValueError:
        print('Error: invalid number')
        
def ran_num_reader(): #excercise 8
    #accepts no arguments
    #it opens ran_numbers.txt
    #and read it
    #it then displays the numbers and how many of them their are
    #lastly it also displays the total
    try: 
        #open file
        infile = open('ran_numbers.txt', 'r')
        
        #variables
        items = 0
        total = 0
        
        #read line
        num = infile.readline()
        num = num.rstrip()
        
        #print the first number
        print(num)
        #read the lines and display them
        while num != '':
            items += 1
            total = int(num) + total
            num = infile.readline()
            num = num.rstrip('\n')
            print(num)
            
        #find the total and number of items
        print('The total of the', items, 'random numbers is:', total)
        
    #if file not found
    except IOError:
        print('Error: file not found')
        
def golf_main(): #exercise 10
    #accepts no arguments
    #calls other functions
    
    golf_menu()
    
def golf_menu():
    #accepts no arguments
    #displays a menu
    #asks the user for a choice
    #and returns it
    
    #print display hello message
    print('Welcome to Hole In Twelve golf management system.')
    print('Please choose from the following commands...')
    print()
    
    #print the menu
    print('1) Read golf data')
    print('2) Append golf data')
    print('3) Exit')
    print()
    
    #get the players input
    choice = int(input("Menu choice: "))
    
    #statments to choose where to go
    if choice == 1:
        golf_read()
    elif choice == 2:
        golf_write()
    elif choice == 3:
        print('Goodbye')
    else:
        choice = int(input('Error select a vaild option'))
        
    
def golf_write():
    #accepts no arguments
    #open file golf_record.txt
    #and writes down a score presented by the user and their name
    #it then saves it to the file and closes it
    
    try:
        #open file
        outfile = open('golf_record.txt', 'w')
        
        #get inputs
        name = input("Golfer's name: ")
        score = input('Score: ')
        
        outfile.write(name + '\n')
        outfile.write(score + '\n')
        
        #ask if they want to add another
        choice = input('Add anohter golfer (y/n)' )
        
        #if they add another
        if choice == 'y':
            name = input("Golfer's name: ")
            score = input('Score: ')
            
            outfile.write(name + '\n')
            outfile.write(score + '\n')
            
            choice = input('Ann another golfer (y/n) ')
        
        #if they dont want too add another
        if choice == 'n':
            print('Golf data written to golf_record.txt')
            
            #error
        else:
            choice = input('Please enter a valid letter')
            
        #close the file
        outfile.close()
    except IOError:
        print('Error cant find file')
    
def golf_read():
    #accepts no arguments
    #opesn file golf_record.txt
    #and reads the file
    #it then displays all the info read
    #and closes the file
    
    try:
        #open the file
        outfile = open('golf_record.txt', 'r')
        
        #variable
        name = outfile.readline()
        #loop to get the records
        while name != '':
            score = outfile.readline()
            
            #strip the new line
            name = name.rstrip('\n')
            score = score.rstrip('\n')
            
            #output to the user
            print(name)
            print(score)
            print()
            #read a new name
            name = outfile.readline()
        
        #close the file
        outfile.close()

    #errors
    except IOError:
        print('Error cant find file')
        
        
def web_page_generator(): #exercise 11
    #acceps no arguementss
    #it ask the user for a name
    #and a description
    #saves it to a file
    try:
        #user name and description
        name = input('Please enter a name ')
        descripiton = input('Write a short desciption of yourself ')
        
        #open the file
        webpage = open(name+'.html','w')
        
        #write in the file
        webpage.write('<html>')
        webpage.write('<head>')
        webpage.write('</head>')
        webpage.write('<body>')
        webpage.write('<center>')
        webpage.write('<h1>'+ name+ '</hq>')
        webpage.write('</center>')
        webpage.write('<hr/>')
        webpage.write(descripiton)
        webpage.write('<hr/>')
        webpage.write('</body>')
        webpage.write('</html>')
    except IOError:
        print('Error file not found')
        
def avg_steps(): #exercise 12
    #accepts no arguments
    #reads from steps.txt
    #and averages the number of steps taken each month
    #it then displays all the info in what month it is in
    
    #variables
    total = 0
    index = 0
    DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    #open file
    outfile = open('steps.txt', 'r')
    
    #for months in days
    for days in DAYS_PER_MONTH:
        for day in range(days):
            line = outfile.readline()
            line = line.rstrip('\n')
            #print
            line = int(line)
            total += line
        average = int(total) / int(DAYS_PER_MONTH) * int(index)
        print( MONTHS, average, 'steps')
        index +=1
        total = 0