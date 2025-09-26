def day_converter():
    #day_converter() accepts no arguemetns
    #displays the dys of the week from english to spanish
    
    day_spanish = str(input('Enter the day of the week: '))
    #find and display the day of the week i n spanish
    if day_spanish == 'lunes':
        print('1')
    elif day_spanish == 'martes':
        print('2')
    elif day_spanish == 'miercoles':
        print('3')
    elif day_spanish == 'jueves':
        print('4')
    elif day_spanish == 'viernes':
        print('5')
    elif day_spanish == 'sabado':
        print ('6')
    elif day_spanish == 'domingo':
        print('7')
    else:
        print('please type a valid day')
    
def roman_numerals():
    #roman_numerals() accepts no arguements
    #user inputs a number 1-10 and turns it into a roman numeral
    
    number = str(input('Enter a number: '))
    #find adn display what they number is in romannumerals
    if number == '1':
        print('I')
    elif number == '2':
        print('II')
    elif number == '3':
        print('III')
    elif number == '4':
        print('IV')
    elif number == '5':
        print('V')
    elif number == '6':
        print('VI')
    elif number == '7':
        print('VII')
    elif number == '8':
        print('VIII')
    elif number == '9':
        print('IX')
    elif number == '10':
        print('x')
    else:
        print('please type a number 1-10')
        
def color_mixer():
    #color_mixer() accepts no arguments
    #ask the user for two primary colors mixes them adn tells them the output
    
    color_one = str(input('Enter your first color: '))
    color_two = str(input('Enter your second color: '))
    #answer if you need color purple
    if color_one == 'blue' and color_two == 'red' or color_one == 'red' and color_two == 'blue':
        print('purple')
        #answer if you need the color orange
    elif color_one == 'yellow' and color_two == 'red' or color_one == 'red' and color_two == 'yellow':
        print('orange')
        #answer if you need the color green
    elif color_one == 'yellow' and color_two == 'blue' or color_one == 'blue' and color_two == 'yellow':
        print('green')
    else:
        #if not a valid color
        print('please put a valid color')

def hot_dog():
    import math
    #hot_dog() accepts no arguments
    #calculates the mininum number of buns and hot dogs needed for a cookout
    #ask for the number of people    
    people = int(input('How many people will their be? '))
    #calculate minium hot dog packages
    min_hotdogs = math.ceil(people / 10)
    #calculate minium bun packages
    min_buns = math.ceil(people / 8)
    #calculate leftover hotdogs
    leftover_hotdogs = min_hotdogs * 10 - people
    #calculate leftover buns
    leftover_buns = min_buns * 8 - people
    #display info
    print('Min number of hot dogs packages needed:', format(min_hotdogs,'.0f') )
    print('Min number of bun packages needed:', min_buns)
    print('leftover hotdogs:' , leftover_hotdogs)
    print('leftover buns:' , leftover_buns)
    
def time_calculator():
    #time_calculator() accepts no arguments
    #asks the user for a amount of seconds and displays the time in simpliest form
    
    time = int(input('Please enter the number of seconds: '))
    
    if time < 60:
        print('that is', time, 'seconds')
    
    elif time >= 86400:
        #find the days, and the leftover hours, minutes, and seconds,
        days = time // 86400
        hours = time // 3600 % 24
        minutes = time // 60 % 60
        seconds = time % 60
        # display the info
        print('days:', days)
        print('hours:', hours)
        print('minutes:', minutes)
        print('seconds:', seconds)
    #find leftover hours minutes and secodns
    elif time >= 3600:
        #find the hours, and the leftover minutes and seconds
        hours = time // 3600
        minutes = time // 60 % 60
        seconds = time % 60
        print('hour:', hours)
        print('minutes:', minutes)
        print('seconds:', seconds)
    # find leftover seconds and minutes
    elif time > 60:
        #display the left over seconds
        minutes = time // 60
        seconds = time % 60
        print('minutes:', minutes)
        print('seconds:', seconds)
        
def leap_year():
    #leap_year() accepts no arguements
    #thsi program promts the user for a year and and displays the number of days in febuary that year'
    year = int(input('Please enter the year: '))
    #if not divisible by 100 and 4 its a leap year
    if not year % 100 and not year % 4:
        print(year, 'is a leap year. There are 29 days in the month of febuary')
        #if not divisible by 4 it is a leap year
    elif not year % 4:
        print(year, 'is a leap year. There are 29 days in the month of febuary.')
        #if anything else it is not a leap year
    else:
        print('is not a leap year. There are 28 days in the month of febuary.')
    
def sir_fix_alot():
    #sir_fix_alot() accepts no arguemtns
    #this program tells the user methods to fix a wifi trouble shoot
    
    print('reboot computer and try to connect')
    answer_1 = input('did that fix the problem? ')
    answer_1 = answer_1.lower()
    #see if the user needs more help
    if answer_1 == 'yes':
        print('netfix and chill')
        #soluiton 2
    else:
        print('reboot router and try to connect')
        answer_2 = input('did that fix the problem? ')
        answer_2 = answer_2.lower()
        if answer_2 == 'yes':
            print('netflix and chill')
        else:
            #solution 3
            print('verify cables are firmly attached')
            answer_3 = input('did that fix the problem? ')
            answer_3 = answer_3.lower()
            if answer_3 == 'yes':
                print('netflix and chill')
            else:
                #solution 4
                print('move router to better location')
                answer_4 = input('did that fix the problem? ')
                answer_4 = answer_4.lower()
                if answer_4 == 'yes':
                    print('netflix and chill')
                else:
                    #get a new router
                    print('get a new router')
                    
def can_we_just_eat():
    #can_we_just_eat() accpets no arrguemetns
    #this program prompts the user for any dietary restriciotns and give the list of restraunt choices
    vegan = input('Is anyone in your party a vegan? (yes/no)' )
    vegetarian = input('Is anyone in your party a vegetarian? (yes/no)' )
    gluten_free = input('Is anyone in your party gluten intolerant? (yes/no)' )
    #find where they can eat at
    if vegan == 'no' and vegetarian == 'no' and gluten_free == 'no':
        print('Here ar your restaurant choices:')
        print('Corner Cafe')
        print('Chefs Kitchen')
        print('Meain Street Pizza Company')
        print('Mamas Fine Italian')
        print('Joes Gourmet Burgers')
    elif vegan == 'yes' and vegetarian == 'no' and gluten_free == 'no':
        print('Here ar your restaurant choices:')
        print('Corner Cafe')
        print('The Chefs Kitchen')
        print('Mamas fine itlaian')
        print('Main Street Pizza Company')
    elif vegan == 'yes' and vegetarian =='yes' and gluten_free =='no' or gluten_free == 'yes':
        print('Here ar your restaurant choices:')
        print('Corner Cafe')
        print('The chefs Kitchen')
    elif vegan == 'no' and vegetarian == 'yes' and gluten_free =='no':
        print('Here are your restaurant choices: ')
        print('Main Street Pizza Company')
        print('Corner Cafe')
        print('Mamas fine itlaian')
        print('The Chefs Kitchen')
    elif vegan == 'no' and  vegetarian =='no' and gluten_free == 'yes':
        print('Here are you restaurant choices: ')
        print('Main Street Pizza Company')
        print('Corner Cafe')
        print('The Chefs Kitchen')
    elif vegan == 'no' and vegetarian == 'yes' and gluten_free == 'yes':
        print('Here are you restaurant choices: ')
        print('Main Street Pizza Company')
        print('Corner Cafe')
        print('The Chefs Kitchen')
   
def hit_the_target():
    #hit_the_target() accepts no arguments
    # this program creates a target and ask the user for inputs of how they throw the dart
    import turtle
    #named constants
    screen_width = 600  #screen width
    screen_height = 600 #screen height
    target_lleft_x = 200 #targets lower left corner x
    target_lleft_y = 250 #targets lower left corner y
    target_width = 25 #targets width
    force_factor = 30 # arbitrary force factor
    projectile_speed = 1 #projectiles animation speed
    north = 90 #angle of the north direction
    south = 270 #angle of south direction
    east = 0 #angle of east direction
    west = 180 #angle of west direction
    
    #ask user for the projectile angle and force
    projectile_angle = int(input('Enter the projectiles angle: '))
    projectile_force = int(input('Enter the launch force (1-10): '))
    
    #draw the target
    turtle.penup()
    turtle.goto(100,250)
    turtle.pendown()
    turtle.goto(200,250)
    turtle.goto(200,350)
    turtle.goto(100,350)
    turtle.goto(100,250)
    turtle.penup()
    
    #change the force to a y value
    projectile_force_y = projectile_force * 100
    #showing where the projectile hit
    turtle.goto(0,0)
    turtle.pendown()
    turtle.goto(projectile_angle,projectile_force_y)
    #tell the user their results and hints
    if projectile_angle >= 101 and projectile_angle <= 199 and projectile_force_y >= 250 and projectile_force_y <= 350:
        print('you hit the target')
    elif projectile_angle >= 200:
        print('you missed the target')
        print ('maybe you need to lower your angle')
    elif projectile_angle <= 100:
        print('you missed the target')
        print('maybe you need to raise your angle')
    elif projectile_force_y >= 351:
        print('you missed the target')
        print('maybe you need to use less force')
    elif projectile_force_y <= 249:
        print('you missed the target')
        print('maybe you need to use more force')
    turtle.done()
    
    
