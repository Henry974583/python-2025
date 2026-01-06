def file_write(): #program 6-1
    #accetps no arguements
    #it opens the file lotr.txt
    #and write the name of three lotr characters
    
    #open file
    outfile = open('lotr.txt', 'w')
    
    #write the names    
    outfile.write("Gandolf\n")
    outfile.write('Frodof\n')
    outfile.write('Aragon\n')
    
    #close file
    outfile.close()
    
def file_read(): #program 6-2
    #file accepts no arguemtns
    #it oepsn lotr.text and reads the text to a file object
    #it then prinths the file cotnets
    
    #open file
    infile = open('lotr.txt', 'r')
    
    #read cotents
    file_cotents = infile.read()
    
    #close file
    infile.close()
    
    print(file_cotents)
    
def line_read(): #program 6-3
    #accepts no arguemtns
    #reads the cotents of the file one line at a time
    #outputes the the cotents
    
    #open file
    infile = open('lotr.txt', 'r')
    
    #read file cotents
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    #close file
    infile.close()
    
    #print outputs
    print(line1)
    print(line2)
    print(line3)
    
def write_names(): #program 6-4
    #accepts no arguments
    #it promtps the user for the names of three friends
    #and assigns each name to a unique variable
    #it opens friends.txt and writes each name to the file
    #on it's own line in the file
    
    #print header
    print('Please enter the names of three friends.')
    
    #get inputs
    friend1 = input('Friend 1: ')
    friend2 = input('Friend 2: ')
    friend3 = input('Friend 3: ')
    
    #open file
    
    myfile = open('friends.txt', 'a')
    
    #write the three names
    myfile.write(friend1 + '\n')
    myfile.write(friend2 + '\n')
    myfile.write(friend3 + '\n')
    
    #close file
    myfile.close()

def strip_newline(): #program 6-5
    #accepts no arguements
    #it opens the file lotr.txt and reads each line
    #it strips the newline '\n' characters from each line
    #and prints the liens
    
    #open file
    file = open('lotr.txt', 'r')
   
   #read the lines file
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    
    #strip the \n caracters
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    #close file
    file.close()
    
    #print the stripped strings
    print(line1)
    print(line2)
    print(line3)
    
def write_numbers(): #program 6-6
    #accepts no arguments
    #it takes input from the user in the form of three integers
    #it opens the file numbers.txt
    #and writes three numbers to files as strings
    
    #open the file
    infile = open('numbers.txt', 'w')
    
    #get inputs
    num1 = int(input('Please enter a number: '))
    num2 = int(input('Please enter a number: '))
    num3 = int(input('Pleaes enter a number: '))
    
    #write the file down
    infile.write(str(num1 + '\n'))
    infile.write(str(num2 + '\n'))
    infile.write(str(num3 + '\n'))
       
    #close file and goodbye message
    infile.close()
    print()
    print('Your numbers have been written to numbers.txt.')
    
def read_numbers(): #program 6-7
    #accepts no arguments
    #it opens the file numbers.txt and reads in each line
    #converting each from a  string to an integer
    #it totals and outputs the three numbers and their total
    
    #open file
    outfile = open('numbers.txt', 'r')
    
    #convernt line from string to integer
    num1 = int(outfile.readline())
    num2 = int(outfile.readline())
    num3 = int(outfile.readline())
    
    #find total
    total = num1 + num2 + num3
    
    #print info
    print('Here is your problem: ', num1,'+', num2,'+', num3,'=', total)
    
def write_sales(): #program 6-8
    #accepts no arguments
    #it prompts the user for the number of days for to input sales
    #for each iteration it wirtes the sale to the file sales.txt
    #after all days have been processed
    #it closes the file and outputs a mesage
    
    #how many days
    days_num = int(input('How many days do you want to enter sales for? '))
    
    #open file
    sales_file = open('sales.txt', 'w')
    
    #loop for number of days
    for days in range(1, days_num  + 1):
        sales = float(input('Enter the sales for day #' + str(days) + ': '))
        
        #write the files
        sales_file.write(str(sales) + '\n')
        
    #close file and output message
    sales_file.close()
    print('All data has been saved to sales.txt')
        
def read_sales(): #program 6-9
    #read sales accepts o arguements
    #it opens and reads from sales.txt
    #it loops until it reaches the end of the file
    #each iteration of the loop will output the maount
    #and read the next line
    
    #open file
    sales_file = open('sales.txt', 'r')
    
    #read the first line to prime the sentinel
    line = sales_file.readline()
    
    #loop while line is not blank
    while line != '':
        #convert
        amount = float(line)
        
        #print
        print(format(amount, ',.2f'))
        
        #get a new line
        line = sales_file.readline()
        
    #close file
    sales_file.close()
    
def read_sales2(): #program 6-10
    #accepts no arguments
    #it opens and reads form sales.txt
    #it loops for each line in the file
    #and outputs the line
    
    #open file
    sale_file = open('sales.txt', 'r')
    
    
    for line in sale_file:
        
        #convert to a float
        amount = float(line)
        
        #output the line
        print(format(amount, ',.2f'))
        
    #close the file
    sale_file.close()
    
def write_video_times(): #program 6-11
    #accepts no arguments
    #it takes inputs for how many vidoes are in the project
    #and asks for the length of the video
    
    #inputs
    videos_num = int(input('How many videos are in the project? '))
    
    #open file
    video = open('video_times.txt', 'w')
    
    #loops for number of video times
    for videos in range(1, videos_num + 1):
        video_length = int(input('Video #' + str(videos) + ': '))
       
        #write files
        video.write(str(video_length) + '\n')
        
    #close file and output message
    video.close()
    print('All tiems have been written to video_tiems.txt.')
    
def read_video_times(): #program 6-23
    #accepts no arguments
    #it adds up the video times using loops
    #then it outputs the info
    
    #open file
    outfile = open('video_times.txt', 'r')
    
    #intalize counter and total
    counter = 1
    total = 0
    
    #loop to keep a runing total, outputting the video and its time
    for time in outfile:
        
        length = float(time.rstip('\n'))
        print('Video #' + str(counter) + ' time:', length, 'seconds')
        counter += 1
        total += length
        
    #output total
    print('The total running time of all videos is: ', total, 'seconds.')
    
def save_emp_records(): #program 6-13
    #save emp records accepts no arguments
    #it prompts the user for the number of employee records
    #it opens a file employees.txt and saves
    #the records Name, ID #, adn department to the file
    #it outputs a finished message with the filename
    
    #how many employees
    employee_num = int(input('How many employee records do you want to enter? '))
    
    #open file
    employee_file = open('employees.txt', 'w')
    
    #loop
    for employee_info in range(1, employee_num + 1):
        name = str(input('Name: '))
        ID = str(input('ID Number: '))
        dept = str(input('Department: '))
        print()
        
        employee_file.write(name + '\n')
        employee_file.write(ID + '\n')
        employee_file.write(dept + '\n')
        
    #close file
    employee_file.close()
    print('All records were saved to employees.txt')
    
def read_emp_records(): #program 6-14
    #reead emp records accetps no arguments
    #it opens the file employees.txt
    #and loops for each line the file
    #outputting the record for employe name, ID #, adn dept
    employee_info = open('employees.txt', 'r')
    
    #variables
    count = 1
    name = employee_info.readline()
    
    #loop for each record
    while name != '':
        ID = employee_info.readline()
        dept = employee_info.readline()
        
        #strip newline
        name = name.rstrip('\n')
        ID = ID.rstrip('\n')
        dept = dept.rstrip('\n')
        
        #output to user
        print('\nRecord for employee #' + str(count))
        print('Name: ', name)
        print('ID: ', ID)
        print('Department', dept)
        print()
        name = emp_file.readline()
        count += 1
    #close file
    employee_info.close()
    print(print('\n' + str(count-1), 'records retrieved.'))
        
        
    #skipping to program 6-22
    
def gross_pay1(): #program 6-22
    #gross pay 1 accepts no arguments
    #it prompts the user for hours woorked and hourly pay
    #it calculates the gross pay = hours * rate and outputs the result
    
    #inputs
    hours = int(input('Enter the number of hours worked: '))
    rate = float(input('Enter the pay rate'))
    
    pay = hours * rate
    
    print('Gross pay: $', format(pay, ',.2f'), sep = '')
    
    #skip to program 6-24
    
def display_file1(): #program 6-24
    #dispaly file 1 acceepts no arguments
    #takes input form the user for a filename to open
    
    #inputs
    filename = input('Enter filename to open: ')
    
    #open the file adn read teh cotents
    inflile = open(filename, 'r')
    
    #outputs
    print(cotents)
    infile.close()
    
def display_file2(): #program 6-25
    #display file 1 accepts no arguments
    #takes input from the user for a filename to open
    #and reads the cotents of the file
    
    #inputs
    filename = input('Enter file name to open: ')
    
    try:
        #open the file and
        infile = open(filename, 'r')
        
        #print
        print(cotents)
        infile.close()
        
    except IOError:
        print('File does not exist')
        
