import math
import random
import my_graphics
import turtle
def menu(): #used to organise
    print('           MENU')
    print('1) Sales Tax Program Mod')
    print('2) Calories')
    print('3) Stadium Seating')
    print('4) Paint Estimator')
    print('5) Math quiz')
    print('6) Time Loop')
    print('7) Rock Paper Scissors')
    user_choice = int(input('Please select the program'))
    #call functions
    if user_choice == 1:
        sales_tax()
    if user_choice == 2:
        calories()
    if user_choice == 3:
        stadium_seating()
    if user_choice == 4:
        paint_estimator()
    if user_choice == 5:
        math_quiz()
    if user_choice == 6:
        time_loop(seconds)
    if user_choice == 7:
        game()
    #validation
    else:
        user_choice = int(input('Please select a valid program'))
def sales_tax():
    item_price = float(input('Enter the sale amount: '))
    #validation
    if item_price <= 0:
        item_price = float(input('please enter a valid number'))
    state_tax = statetax(item_price)
    
    country_tax = countrytax(item_price)
    
    total_tax = totaltax(item_price, state_tax, country_tax)
    
    total_sale = totalsale(total_tax, item_price)
    
    display(item_price, state_tax, country_tax, total_tax, total_sale)
    
def statetax(item_price):
    state_tax = (item_price * 0.05)
    print(state_tax)
    return state_tax

def countrytax(item_price):
    
    country_tax = (item_price * 0.025)
    return country_tax

def totaltax(item_price, state_tax, country_tax):
    total_tax = (state_tax + country_tax)
    return total_tax

def totalsale(total_tax, item_price):
    total_sale = (total_tax + item_price)
    return total_sale

def display(item_price, state_tax, country_tax, total_tax, total_sale):
    
    #variables
    
    
    print('Your purchase price was: \t$', (format(item_price,'7.2f')))
    print('Your state tax amount is: \t$', (format(state_tax,'7.2f')))
    print('Your country tax amount is: \t$',(format(country_tax,'7.2f')))
    print('Your total tax is: \t\t$', (format(total_tax,'7.2f')))
    print('Your total sale is: \t\t$', (format(total_sale,'7.2f')))
    
def calories(): #exercise 6
    #accepts no arguemtns
    #it calls for 2 functions
    
    #call funtions
    fat_c = fat()
    
    carbs_c = carbs()
    
    print()
    print('Here is your calorie intake for the day.')
    print('You consumed', carbs_c, 'worth of carbs today. nice work')
    print('You consumed', fat_c, 'worth of fat today. nice work')
def fat():
    #fucntion for fat
    fat_g = float(input('How many grams of fat did you consume? '))
    #validation
    if fat_g <= 0:
        fat_g = float(input('Please type a valid number'))
    fat_c = fat_g * 9
    return fat_c
    
def carbs():
    #function for carbs
    #validation
    carbs_g = float(input('How many grams of carbs did you consume? '))
    if carbs_g <= 0:
        carbs_g = float(input('Please enter a valid number'))
    carbs_c = carbs_g * 4
    return carbs_c

def stadium_seating():#exercise 7
    #it accepts no arguments
    #it calls 3 functions
    #and finds the total income from ticket sales
    
    a_cost = class_a()
    b_cost = class_b()
    c_cost = class_c()
    
    #find total
    total = a_cost + b_cost + c_cost
    
    #print results
    print('The total income sales form tickets is: $', total)

    pass
def class_a():
    #accepts no arguments
    #finds the amount of tickets sold
    
    #inputs
    tickets_a = float(input('Enter the number of Class A tickets sold: '))
    #validate
    if tickets_a < 0:
        tickets_a = float(input('Please enter a valid number of A tickets sold: '))
    a_cost = tickets_a * 20
    return a_cost

def class_b():
    #accepts no arguements
    #finds the amuont of tickets sold
    
    #inputs
    tickets_b = float(input('Enter the number of Class B tickets sold: '))
    #validate
    if tickets_b < 0:
        tickets_b = float(input('Please enter a valid number of B tickets sold: '))
    b_cost = tickets_b * 15
    return b_cost

def class_c():
    #accepts no arguements
    #find the amoutn of tickets solde
    
    #inputs
    tickets_c = float(input('Enter the nubmer of Class C tickets sold: '))
    #validate
    if tickets_c < 0:
        ticktets_c = float(input('Please enter a valid number of C tickets sold: '))
    c_cost = tickets_c * 10
    return c_cost


def area_find():

    #inputs
    area = float(input('Please enter the total sqaure feet to be painted: '))
    #validate
    if area < 0:
        area = float(input('Please type a valid are to paint'))
    return area

def cost_find():
    #inputs
    cost = float(input('Please enter the cost per a gallon of paint'))
    #validate
    if cost < 0:
        cost = float(input('Please type a valid cost'))
    return cost
    
def paint_estimator(): #exercise 8
    #accepts no arguements
    #calls other functions
    #recives inputs from the users to fidn how much will be painted and how much each gallon of paint is
    area = area_find()
    cost = cost_find()
    
    #headers
    print()
    print('The cost breakdown to paint', format(area, '.2f'), 'sqaure feet is:')
    print('-------------------------------------------------------------------')
    #calcualtions
    
    gallons = 112 // area

    paint_cost = gallons * cost
    hours = gallons * 8
    hours_cost = hours * 35
    total = hours_cost + paint_cost
    
    #print info
    print('Total cost of paint: $', paint_cost)
    print('Total labor cost: $', hours_cost)
    print('Total cost of the job is: $', total)


def get_numbers():
    #no arguemtns
    #genrates to random numbers
    
    #varaibles
    MIN = 1
    MAX = 200
    
    #generating numbers
    num_1 = random.randint(MIN, MAX)
    num_2 = random.randint(MIN, MAX)
    
    return num_1, num_2

def math_quiz(): #exercise 11
    #no arguemtns
    #calls get_numbers for random values to add
    #outputs the problem and prompts if they want to continue

    #call function

    num_1, num_2 = get_numbers()
    anwser = num_1 + num_2
    
    #hears and info
    print('Solve:')
    print()
    print('\t\t ', num_1)
    print('+\t\t ', num_2)
    print()
    user = int(input('Anwser: '))
    #validate anwser
    if user == anwser:
        print('Correct')
        yes_no = str(input('do you want another problem? '))
    if user != anwser:
        print('Incorrect')
        yes_no = str(input('do you want another problem? '))
    
    #loop
    if yes_no == 'y':
        math_quiz()
    if yes_no == 'n':
        print('goodbye')
        
seconds = 10
def time_loop(seconds):
    #no arugemnts
    #ask for a input
    #then calls falling_distance and displays the info
    
    for time in range(1, seconds + 1):
        distance = falling_distance(time)
        print(time, '\t\t', distance)
def falling_distance(time):
    #recives tiem
    #calculates the distance fallend using math
    
    distance = .5 * 9.8 * time **2
    
    return distance

def game():#exercise 21
    #no argumetns
    #calls multiple functions
    #outputs a greeting
    #outputs each players weapons
    #outputs a prompt to continue
    
    player = player_choice()
    
    computer = comp_choice()
    
    winner(player, computer)
    
def comp_choice():
    #no arguemtns
    #chooses a random intger from 1-5
    #returns the intger
    #constants
    rock = 1
    paper = 2
    scissors = 3
    lizard = 4
    spock = 5
    #input
    computer = random.randint(1, 5)
    return computer

def player_choice():
    #no arguemtns
    #prompts the user for their weapon
    #returns their weapon
    #constants
    rock = 1
    paper = 2
    scissors = 3
    lizard = 4
    spock = 5
    #input
    player = str(input('Type your weapon of choice (rock, paper, scissors, lizard, spock): '))
    return player

def winner(player, computer):
    #recives computer and player
    #determines the winner
    #outputs who won
    
    
    #find computers weapon
    if computer == 1:
        computer_weapon = 'rock'
    if computer == 2:
        computer_weapon = 'paper'
    if computer == 3:
        computer_weapon = 'scissors'
    if computer == 4:
        computer_weapon = 'lizard'
    if computer == 5:
        computer_weapon = 'spock'
    
    #info
        
        print()
        print('You chose...', player)
        print()
        print('The computer chose...', computer_weapon)
        print()
        
    #find who won
        if player == 'rock' and computer_weapon == 'scissors':
            print('You won! \t\t rock crushes scissors')
        elif player == 'rock' and computer_weapon == 'lizard':
            print('You won! \t\t rock crushes lizard')
        elif player == 'rock' and computer_weapon == 'rock':
            print('Its a tie.')
        elif player == 'rock' and computer_weapon == 'spock':
            print('You lost! \t\t spock vaporizes rock')
        elif player == 'rock' and computer_weapon == 'paper':
            print('You lost! \t\t paper covers rock')
        elif player == 'paper' and computer_weapon == 'spock':
            print('You won! \t\t paper suffocates spock')
        elif player == 'paper' and computer_weapon == 'rock':
            print('You won! \t\t paper covers rock')
        elif player == 'paper' and computer_weapon == 'paper':
            print('Its a tie.')
        elif player == 'paper' and computer_weapon == 'scissors':
            print('You lost! \t\t scissors cuts paper')
        elif player == 'paper' and computer_weapon == 'lizard':
            print('You lost! \t\t lizard eats paper')
        elif player == 'scissors' and computer_weapon == 'paper':
            print('You won! \t\t scissors cuts paper')
        elif player == 'scissors' and computer_weapon == 'lizard':
            print('You won! \t\t scissors stabs lizard')
        elif player == 'scissors' and computer_weapon == 'scissors':
            print('Its a tie.')
        elif player == 'scissors' and computer_weapon == 'spock':
            print('You lost! \t\t spock vaporizes scissors')
        elif player == 'scissors' and computer_weapon == 'rock':
            print('You lost! \t\t rock crushes scissors')
        elif player == 'lizard' and computer_weapon == 'spock':
            print('You won! \t\t lizard eats spock')
        elif player == 'lizard' and computer_weapon == 'paper':
            print('You won! \t\t lizard eats paper')
        elif player == 'lizard' and computer_weapon == 'lizard':
            print('Its a tie.')
        elif player == 'lizard' and computer_weapon == 'scissors':
            print('You lose! \t\t scissors stabs lizard')
        elif player == 'lizard' and computer_weapon == 'rock':
            print('You lose! \t\t rock crushes lizard')
        elif player == 'spock' and computer_weapon == 'rock':
            print('You win! \t\t spock vaporises rock')
        elif player == 'spock' and computer_weapon == 'scissors':
            print('You win! \t\t spock vaporises scissors')
        elif player == 'spock' and computer_weapon == 'spock':
            print('Its a tie.')
        elif player == 'spock' and computer_weapon == 'lizard':
            print('You lose! \t\t lizard eats spock')
        elif player == 'spock' and computer_weapon == 'paper':
            print('You lose! \t\t paper suffocates spock')
        #loop
    loop = str(input('play again? '))
    if loop == 'y':
        game()
    if loop == 'n':
        print('goodbye')
        
def drawSnowman():
    #no arguements
    #calls functions acting as a main
    #outputs a snowman
    drawbase()
    
    drawmidsection()
    
    drawarms()
    
    drawhead()
    
    drawhat()
    
    drawface()
    
    turtle.done()
def drawbase():
    #no arguements
    #draws the base of a  snowman
    #outputs the bottom cirlce of the snowman
    
    turtle.pencolor('black')
    my_graphics.circle(0, -150, 150, 'lime')
    

def drawmidsection():
    #no arguements
    #draws the mid section of a snowman
    #outputs the second circle
    my_graphics.circle(0, 120, 125, 'lime')
    my_graphics.circle(0, 170, 25, 'black')
    my_graphics.circle(0, 130, 25, 'black')
    my_graphics.circle(0, 80, 25, 'black')
def drawarms():
    #no arguements
    #draws the arms of a snowman
    #outputs the arms
    my_graphics.line(-113, 170, -250, 110, 'Brown')
    my_graphics.line(-250, 110, -280, 10, 'Brown')
    my_graphics.line(-250, 110, -270, 160, 'Brown')
    my_graphics.line(113, 170, 250, 60, 'Brown')
    my_graphics.line(250, 60, 280, 130, 'Brown')
    my_graphics.line(250, 60, 220, 120, 'Brown')
    my_graphics.line(250, 60, 270, -40, 'Brown')
    turtle.pencolor('black')
    

def drawhead():
    #no arguements
    #draws the hed of the snowman
    #outputs his head
    my_graphics.circle(0, 330, 100, 'lime')
    

def drawhat():
    #no arguemtns
    #draws the hat of the snowman
    #outputs rectangles to make a top hat
    
    my_graphics.rectangle(-75, 430, 150, 40, 'purple')
    my_graphics.rectangle(27, 470, -150, -60, 'purple')
    

def drawface():
    #no arguemtns
    #draws the face of the snowman
    #draws a pipe for the snow man
    my_graphics.circle(-50, 375, 10, 'black')
    my_graphics.circle(50, 375, 10, 'black')
    my_graphics.line(-60, 290, 60, 290, 'black')
    my_graphics.line(40, 290, 150, 155, 'brown')
    my_graphics.square(150, 155, 10, 'brown')
    turtle.pensize(5)
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    
    turtle.pencolor('gray')
    for circle in range(3):
        for swirl in range(4):
            turtle.penup()
            turtle.goto(150, 155)
            turtle.pendown()
            turtle.right(5)
            turtle.forward(10)
            
        for swirl in range(8):
            turtle.left(45)
            turtle.forward(5)
    