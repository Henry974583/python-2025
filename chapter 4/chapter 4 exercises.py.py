def bug_collector(): #exercise 1
    #bug collector accepts no arguemtns
    #this program ask how amny bugs someone coleted in 5 days
    #then tells them the total amount of bugs they caught that week
    
    #welcome message
    print('Welcome to bug masters bug collection system.')
    
    MAX = 5 #max number of days in the week
    
    total = 0.0 #the acumlator base value
    
    #loop
    for counter in range(MAX):
        number = int(input('Please enter a number: '))
        total = total + number
        while number <= 0:
            number = int(input('please put a valid number'))
    #display the total
    print('You caught', format(total, ',.0f'), 'bugs.')
    
def distance_traveled(): #exercise 4
    #distance traveled accepts no arguemtns
    #this program paromts the user for the speed of a vechile
    #and how long it drove
    #to find and display the distance travled each hour
    mph = int(input('Enter the speed of the vechile in mph: '))
    hours = int(input('Enter how many hours the vechile drove: '))
    
    while mph <= 0:
        int(input('Please enter a valid speed: '))
        
    while hours <= 0:
        int(input('Please enter a valid time: '))
    
    #find distance
    distance = mph * hours
    end = hours
    #print the header
    print()
    print('Hour\tDistance')
    print('-----------------')
    
    #print the distance and hours
    for number in range(1, hours + 1):
        distance = mph*number
        print(number, '\t', distance)
        
def population(): #exercise 13
    #population accepts no arguments
    #this program promts the suer for the starting population
    #teh precent growth of the population
    #and the number of days to simulate it for
    
    #get the inputs
    start_pop = int(input('Enter the starting population: '))
    growth = int(input('Enter the percent of daily growth: '))
    time = int(input('Enter the amount of days to simulate: '))
    total_growth = 0.0
    #pritn headers
    print()
    print('Day\t\tPopulation')
    print('---------------------------')
    
    #validate starting pop
    while start_pop <= 0:
        start_pop = int(input('Enter a valid starting population: '))
    #valdiate growth
    while growth <= 0:
        growth = int(input('enter a valid daily growth'))
    #validate time
    while time <= 0:
        time = int(input('Enter a valid ammount of days'))
        
    print('1 \t\t', start_pop)
    
    #loop
    for day in range(2, time + 1):
        precent = growth / 100
        new_pop = start_pop + start_pop * precent
        start = new_pop
    
        print(day, '\t\t', new_pop)
    
        
def reverse_triangle(): #exercise 14
    #reverse triangle accepts no arguemtns
    #it ask the suer for the base of a triangle and builds it
    #in reverse
    
    #find the base of the triangel
    base_size = int(input('Enter the base of the triangle '))
    
    while base_size <= 0:
        base_size = int(input('Please enter a valid number: '))
    
    #loop to make a reverse triangle
    for row in range(base_size + 1, 0, -1):
        for column in range(row):
            print('*', end='')
        print()
        
def stair_pattern2(): #exercise 15
    #propmts the user for the number of stairs
    #and makes steps based on their input
    
    #get the number of steps
    stair_steps = int(input('Enter the number of stairs: '))
    #validate steps
    while stair_steps <= 0:
        stairs = int(input('please enter a valid number'))
    #loop
    for staris in range(stair_steps):
        print('@', end='')
        for step in range(staris):
            print(' ', end='')
        print('@')
        
def repeating_squares(): # exercise 16
    #reptating squares() accepts no arguemtns
    #prompts the user for a amount of sqaures to make and draws them in diffrent collors
    import random
    import turtle
    #find the number of sqaures to make
    num_sqaures = int(input('How many squares do you want to draw: '))

    #variables
    startX = 300
    startY = -300
    seperator = 10
    screenheight = 900
    screenwidth = 900
    distance = 10
    interger =10

    #turtle set up
    
    turtle.clearscreen()
    turtle.setup(screenheight, screenwidth)
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.colormode(255)
    turtle.pendown()
    turtle.speed(500)
    #verfication
    while num_sqaures <= 0:
        num_sqaures = int(input('please enter a valid number: '))
  
  
    #loop
    for squares in range(num_sqaures):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        
        turtle.pencolor(color1, color2, color3)
        
        turtle.setheading(90)
        turtle.forward(distance)
        turtle.left(90)
        turtle.forward(distance)
        turtle.left(90)
        turtle.forward(distance)
        turtle.left(90)
        turtle.forward(distance)
        distance = distance + interger
        
def hypnotic_pattern():
    #hypnotic pattern accepts no arguemtns
    #it ask for a nubmer of patterns and draws them
    import turtle
    import random
    
    #variables
    startX = 0
    startY = 0
    distance = 3
    interger = 3
    
    turtle.speed(1000)
    
    #turtle setup
    turtle.clearscreen()
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown
    turtle.setheading(90)
    turtle.colormode(255)
    
    patterns = int(input('Enter a amount of patterns: '))
    while patterns <= 0:
        patterns = int(input('Enter a valid number: '))
        
    for pattern in range(patterns):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        
        turtle.pencolor(color1, color2, color3)
        
        for roatation in range(4):
            turtle.pendown()
            distance = distance + (interger * 2)
            turtle.forward(distance)
            turtle.left(90)