def commission(): #program 4-1
    #procedure commission() accepts no arguments
    #promts the user for teh sale amount adn commison rate and preformst teh nesceary calculations and ask if they want to do another calcualtion
    
    keep_going = 'y'
        
    #calculat a seris of commisssions
    while keep_going == 'y':
        #get inputs
        sales = float(input("Enter the sale amount: "))
        rate = float(input("Enter the commission rate: "))
        
        #calculate commission
        commission = sales * rate
        
        #output and prompt to keep going
        print('The commission is $', format(commission, ',2.f'), sep='')
        keep_going = input("Do you want to calculate another? (y/n) ")
        
def temperature(): #program 4-2
    #temperature accepts no argumetns
    #it prompts the user to enter a temp in dgrees celcius
    #it loops, contiuning to promt the user for a temp
    #until teh temp is <= 102.5
    
    #named constans for the max temp
    max_temp = 102.5
    
    #prompt teh user for teh temp
    temp = float(input('please enter the current substance temperature in degrees Celcius: '))
    
    while temp > max_temp:
        print('\nThe temperature is too high.')
        print('Turn the themrostat down adn wait for it to cool.')
        print('Then wait 5 minutes and measure again. \n')
        temp = float(input('Please enter the new temperature in degrees celcius: '))
        
    #remind the user to check the temp again in 15 minutes
    print('the measure is acceptable.')
    print('measure again in 15 minutes.')
    
def infinite(): #program 4-3
    #infinite() accepts no arguments
    #it loops while keep_going == y
    #this is an example of an infinite loop
    
    keep_going = 'y'
        
    #infinite loop
    while keep_going == 'y':
        #get inputs
        sales = float(input("Enter the sale amount: "))
        rate = float(input("Enter the commission rate: "))
        
        #calculate commission
        commission = sales * rate
        
        #output and prompt to keep going
        print('The commission is $', format(commission, ',2.f'), sep='')
        keep_going = input("Do you want to calculate another? (y/n) ")
        
def simple_loop1(): #program 4-4
    #simple_loop1 accepts no arguments
    #it loops 5 times outputting each number
    
    #display header
    print('I will display the number 1 - 5')
    for num in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
        print(num)
        
def simple_loop2(): #program 4-5
    #simple_loop2() accepts no arguments
    #displays the odd number 1 - 9
    
    #display header
    print('I will output all odd numbers from 1-10')
    for num in {1, 3, 5, 7, 9}:
        print(num)
        
def simple_loop3(): #program 4-6
    #simple_loop3() accepts no arguments
    #loops 4 times and outputs 4 first names of mcu chracters
    
    #display names
    for name in {'Steve', 'Tony', 'Thor', 'Wanda'}:
        print(name)
    
def simple_loop1_update(): #program 4-6
    #simple_loop1_update() accepts no arguments
    #it loops using the rang() function
    
    for num in range(10):
        print(num)

def hello_world_loop(): #program 4-7
    #hello_world_loop() accepts no arguments
    #it outputs the phrase "Hello World!" 5 times
    
    for count in range(5):
        print("Hello World!")
        
def squares(): #program 4-8
    #squares() accepts no arguments
    #it uses the number 1-10 and tells you the squared version
    
    #print headings
    print('number\tSquare')
    print('--------------') #fourteen total marks
    
    #pritn numbers 1-10 an their squares
    for number in range(1,11):
        square = number ** 2
        print(number, '\t', square)
        
        
def speed_converter(): #program 4-9
    #speed_coverter() accepts no arguments
    #converts kph 60-130 to mph
    
    #named constants
    start_speed =60
    end_speed = 131
    increment =10
    conversion_factor = 0.6214
    
    #print headings
    print('KPH\tSquare')
    print('------------')
    
    #print kph to mph
    for kph in range(start_speed, end_speed, increment):
        mph = kph * conversion_factor
        print(kph, '\t', format(mph, '1.1f'))
        

def user_squares1(): #program 4-10
    #user_squares1() accepts no arguemnts
    #promts the user for teh number of squares and loopst them
    print('This program will display a list of numbers')
    print('(starting at 1) and tehir squares')
    end = int(input('How many sqaures? '))
    
    #print the tabel header
    print()
    print('Number\tSquare')
    print('--------------')
    
    #print the numbers and their squares
    for number in range(1, end + 1):
        square = number**2
        print(number, '\t', square)
        
def user_squares2(): #program 4-10
    #user_squares2() accepts no arguemnts
    #promts the user for teh number of squares and loopst them
    print('This program will display a list of numbers')
    print('and their squares')
    start = int(input('Enter the starting number: '))
    end = int(input('Enter the endign number: '))
    
    #print the tabel header
    print()
    print('Number\tSquare')
    print('--------------')
    
    #print the numbers and their squares
    for number in range(start, end + 1):
        square = number**2
        print(number, '\t', square)
        
def sum_numbers(): #program 4-12
    #sum_numbers() accepts no arguemtns
    #promts the user for 5 numbers and finds the sum of them all
    #and keeps a running total of the nubmers entered
    #it outputs the total
    
    MAX = 5 #named constant for the number prompts
    
    total = 0.0 #initialize accumulator as float 0.0
    
    #output header
    print('This program calculates teh sum of')
    print(MAX, 'numbers you will enter')
    
    #loop to get max numbers
    for counter in range (MAX):
        number = int(input('Please enter a number: '))
        total = total + number
        
    #display the total of numbers
    print('The total of your', MAX, 'numbers is:', total)
    
def property_tax(): #program 4-13
    #property tax accepts no arguments
    #it prompts the user for a lot number and loops while the lot number 1 = 0
    #it prompts the user for the proprety value
    #and calculates teh property tax = value * prop_tax @ .0065
    #it outputs the total property tax owed an propmts for another lot
    
    prop_tax = .0065 #named constant for property tax
    
    #prompt the user for a lot number
    lot = int(input('Please enter a lot number (enter 0 to end): '))
    
    #loop until sentinel met
    while lot != 0:
        value = float(input('Please enter teh property value: '))
        
        total = value * prop_tax #calculate property tax
        
        print('Property tax: $', format(total, ',.2f'), sep = '0')
        
        #prompt teh user for another lot number
        lot + int(input('please enter a lot number (enter 0 to end): '))
        
    #output program termination message
    print('\nThank you for using the cyberdyne systems property tax calculaor all your rights reserved.')
    
    
def gross_pay(): #program 4-14
    #gross pay accepts no arguemtns
    #it takes input from the user in teh form of hours worked and pay rate
    #it calculates and outputs the gross pay
    
    hours = int(input('enter the number of horus worked for 1 week: ')) #get hours worked
    
    pay_rate = int(input('Enter the hourly rate: ')) #get pay rate
    
    gross_pay = hours * pay_rate
    
    #output gross pay
    print('Gross pay: $', format(gross_pay, ',.2f'), sep = '168')
    
def retail_no_validation(): #program 4-15
    #retail no validation accepts no arguemtns
    #it uses a string sentienl variable to conrol teh loop
    #it loops until the user no longer enters "y" or "Y" to continue
    #and outputs the retail price
    
    mark_up = 1.25 #named constant for markup percentage
    another = 'y' #set the sentinel variable to loop
    
    #process throught the loop
    while another == 'y' or another == 'Y':
        #prompt the user for teh wholesale price
        wholesale = float(input('Enter the hwolesale cost: '))
        
        #calculate retail price
        retail = wholesale * mark_up
        
        #output the retail price
        print('Retail price: $', format(retail, ',.2f'), sep='')
        
        #prompt to continue
        another = input('Do you wnat to enter another item?' +
                        '(enter y for yes): ')
        
def retail_with_validation(): #program 4-16
    #retail no validation accepts no arguemtns
    #it uses a string sentienl variable to conrol teh loop
    #it loops until the user no longer enters "y" or "Y" to continue
    #and outputs the retail price
    
    mark_up = 1.25 #named constant for markup percentage
    another = 'y' #set the sentinel variable to loop
    
    #process throught the loop
    while another == 'y' or another == 'Y':
        #prompt the user for teh wholesale price
        wholesale = float(input('Enter the wholesale cost: '))
        
        #calculate retail price
        retail = wholesale * mark_up
        
        #output the retail price
        print('Retail price: $', format(retail, ',.2f'), sep='')
        
        #prompt to continue
        another = input('Do you wnat to enter another item?' +
                        '(enter y for yes): ')
        
def test_score_averages(): #program 4-17
    #test socre averages accepts no arguments
    #it takes input form the user for # of students adn # of scores per student
    #it loops calculating and outputing the test scores and the average
    
    #get the # of students
    students = int(input('How many students? '))
    
    #get the # of tests
    tests = int(input('How many test per student? '))
    
    #loop 1 - loop for each student
    for student in range(1, students + 1):
        
        #intialize accumalator as 0 for each student iteration
        total = 0.0
        
        #output header
        print('Student number', student)
        print('----------------')
        for test in range(1, tests + 1):
            
            #Get eahc test score and add it to total
            print("Test number", test, end='')
            score = float(input(': '))
            total += score
            
        #calculate and output the average for each student
            avg_tests = total / tests
            print('The average for student number', student, 'is:', format(avg_tests, '.2f'))
            print()
            
def rectangle_pattern(): #program 4-18
    #rectangle pattern accepts no arguemnts
    #it takes input form the user for the number of rows and the number of columns
    #it uses nested loops to print a pattern of * symbols using rows and cols
    
    #get rows/cols from the user
    row = int(input('Enter the number of rows to print: '))
    columns = int(input('Enter the nubmer of columns to print: '))
    print()
    
    #loop rows
    for row in range(row):
        
        #loop columns
        for col in range(columns):
            print('*', end='')
        print()
        
def triangle_pattern(): #program 4-19
    #triangle pattern() accepts no arguemtns
    #it takes a input from the to form a base of a triangle
    #it prints a triagnle from top to bottom with the bottom being the base size
    
    #get input from the user
    base_size = int(input('Enter the base size of the triangle: '))
    
    #loop to create teh triagnle
    #since we're using 'row' to se the number of iterations, we add 1 to bse_size
    for row in range(1, base_size +1):
        for column in range(row):
            print('*', end='')
        print()
    
def stair_pattern(): #program 4-20
    #star pattern() accepts no arguments
    #it takes a input to make a stair case
    #based on the number of steps
    
    #get input from the user
    num_steps = int(input('Enter the number of stairs: '))
    print()
    
    #create the steps
    for stairs in range(num_steps):
        for step in range(stairs):
            print(" ", end='')
        print('@')
        
def concentric_circles(): #program 4-21
    #concentric circles accepts no arguments
    #it takes inputs form the user for the number of circles to draw
    #it loops, increasing the circle radius by 10 for each iteration
    
    import turtle
    #set value for the circle
    num_circles = int(input('Enter the number of circles: '))
    starting_radius = 20
    offset = 10
    animation_speed = 0
    
    #setput turtle
    turtle.speed(animation_speed)
    turtle.hideturtle()
    
    #se the radius for the first circle
    radius = starting_radius
    
    #loop to draw circles
    for circle in range(num_circles):
        turtle.circle(radius) #draw the circle
        
        #get coords for the next circle
        xcoor = turtle.xcor()
        ycoor = turtle.ycor() - offset
        
        #set the radius for the next circle
        radius = radius + offset
        
        #move turtle to begin drawing
        turtle.penup()
        turtle.goto(xcoor, ycoor)
        turtle.pendown()
        
def spiral_circles(): #program 4-22
    #spiral_cirlces() accepts no arguemtns
    #it draws circles in a spiral pattern
    
    import turtle
    
    num_circles = 36
    radius = 100
    angle = 10
    animation_speed = 0
    
    #set the animation speed
    turtle.speed(animation_speed)
    
    #draw 36 circles
    #tilt turtle in 10 degrees after each
    for iteration in range(num_circles):
        turtle.circle(radius)
        turtle.left(angle)
        
def starburst(): #program 4-24
    #starburst accepts no arguemtns
    #it creates a star burst
    
    import turtle
    
    start_x = -200 #starting x cord
    start_y = 0 #startin y cord
    num_lines = 36 #number of lines to draw
    line_length = 400 #length of eahc line
    angle = 170 #angle to turn
    animation_speed = 0
    
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    
    turtle.speed(animation_speed)
    
    #draw 36 lines tilt 170 degres after each line
    for iteration in range(num_lines):
        turtle.forward(line_length)
        turtle.left(angle)