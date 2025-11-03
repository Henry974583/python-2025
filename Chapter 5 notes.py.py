import math
import my_graphics
import turtle
def message(): #program 5-1
    #it accepts no arguemtns
    #it prints "I am iron man"
    print('I am Iron Man.')
    
def main_5_2(): #program 5-2
    #it accepts no argumetns
    #it outputs words
        
    print('I am inevitable')
    message() #iron man line
    print('Only one way to win...')
    
def acme_dryer(): #program 5-3
    #it accepts no arguemtnts
    #displays the steps need to take apart a dryer
    
    num_steps = int(input('Hello welcome to acme dryer what step are you on? type zero to close '))
    
    while num_steps <= 0:
        num_steps = int(input('Please tye a number 1-5'))
        
    if num_steps == 0:
        print('Goodbye')
    if num_steps == 1:
        step1()
    if num_steps == 2:
        step2()
    if num_steps == 3:
        step3()
    if num_steps == 4:
        step4()
    if num_steps == 5:
        step5()
def step1():
    #step 1 of acme dryer

    print('Unplug the dryer and move it away form the wall') #step intsruticon
    
    acme_dryer()
    
def step2():
    #step 2 fo acme dryer
    print('remvoe the six screws from the back of the dryer') #step insturctions
    
    acme_dryer()

def step3():
    #step 3 of acme dryer
    print('Remove the back panel') #step instuctions
    
    acme_dryer()
    
def step4():
    #step 4 of acme dryer
    print('Pull the top of the dryer straight up')
    
    acme_dryer()
def step5():
    #step 5 of acme dryer
    print('Pull the front of the dryer off')
    
    acme_dryer()
    
def bad_scope(): #program 5-4
    #bad local accepts no arguments
    #it calls procedure get_name() to get soemone's name
    #then outputs a message using that name
    #NOTE: The scope of the vairable "name" in get_name will not
    #allow this funciton to acces that variable
    
    get_name()
    print('Hello', name) #this will throw and exception
    
def get_name():
    #get name accepts no arguemtns
    #it prompts the user to get their name
    
    name = input('Enter you name: ')
    
def bird_calculator(): #program 5-5
    #accepts no argumetns
    #it calls the funciton texas()
    #then calls teh function kansas
    
    texas()
    
    kansas()
    
def texas():
    #accepts no arguments
    bird = 5000
    print('There are', texas_bird, 'birds in Texas.')
    
def kansas():
    #accepts no arguemtns
    bird = 8000
    print('Therea are', kansas_bird, 'birds in Kansas.')
    
def pass_arg(): #program 5-6
    #pass args accepts no arguments
    #it assigns value = 5
    #it calss show_double, passing value
    
    value = 5
    show_double(value)
    
def show_double(number):
    #show double accepts a value for number
    #it calculates that number *2 and prints the result
    
    result = number * 2
    print(number, '* 2 =', result)
    
def volume_conversion(): #program 5-7
    #volume conversion accepts no arguemtns
    #it calls intro() to display a greeting
    #it prompts the user for the number of cups
    #it calls cups_to_ounces, passing the value for cups
    
    intro()
    
    cups = int(input('Please enter the number of cups to convert to ounces: '))
    
    cups_to_ounces(cups)
def intro():
    #intro accepts no arguemtns
    #it displays a greeting message describing the program
    #and the conversion rate of cups to ounces
    
    print('Welcome to the cups to fluid ounces vonversion program.')
    print('For you reference, 1 cup = 8 fluid ounces.')
    
def cups_to_ounces(cups):
    #cups_to_onces accepts a value for cups
    #it converts the number of  cups the the number of ounces
    #and outputs the result
    ounces = cups * 8
    
    print(cups, 'cup(s) is equal to', ounces, 'fluid ounces')
    
def show_sum(): #program 5-8
    #show sum accepts no arguemtns
    #it outputs a message "The sum of 12 and 45 is"
    #it calls sum_of_numbers(num1, num2) passing the values 12 adn 45
    
    #variables
    num1 = 12
    num2 = 45
    
    
    
    print('The sum of 12 and 45 is ', end='')
    sum_of_numbers(12, 45)
    
def sum_of_numbers(num1, num2):
    
    total = num1 + num2
    print(total)
    
def get_name(): #program 5-9
    #get name accept no arguemtns
    #it prompts the user for thier first then last name
    #it calls revers_name(firs, last) passing values
    #for first and lase
    
    #get inputs
    first = str(input('Please enter your first name: '))
    last = str(input('Please enter your last name: '))
    
    #call reverse
    reverse_name(first, last)
    
def reverse_name(first, last):
    #reverse name accepts strings for first and last
    #it outputs the name in reverse order: last, first
    
    #reverse
    print('Your name reversed is:', last, first)
    
def get_value(): #program 5-10
    #get value accepts no arguemnts
    #it assigns value = 99 and passes value to change_me
    #it outputs a message showing the value of value in this function
    value = 99
    
    print('I just assigned the varialbe value: ', value)
    print()
    
    change_me(value)
    print()
    
    print('The vlaue in funciton get_vlaue is still: ', value)
def change_me(value):
    #change me acecpts an interger for vlaue
    #it reassign the vlaue to 0
    #and outputs a message with the nuew value in this function
    value = 0
    
    print('The value in the funciton change_me has been changed to: ', value)
    
def set_args(): #program 5-11
    #set args accept no argumetns
    #it calls show_interpest passing princape, rate, and peridos as keywords
    
    show_interest(rate=0.01, periods=10, principal=10000.0)
    
def show_interest(rate, periods, principal):
    #show interest accept arguments for rate, periods and principal
    #it clauclates interest = principa*rate*periods
    #and outputs the results
    
    interest = principal * rate * periods
    print('The simple interest will be $', format(interest, ',.2f'), sep='')
    
    
my_value = 10 #global value

def show_value(): #program 5-13
    #show value receives no arguments
    #it prints the value of gloval my_value
    
    print("The value of the global variable my_value is", my_value)
    
#create a global variable
number = 0
def change_global(): #program 5-14
    #cange_global accept no arguments
    #It cahnge the value of the global variable number
    #then calls global_variables_are_bad to print the variable
    
    global number
    number = int(input('What do you wna to change the global to? '))
    global_variables_are_bad()
    
def global_variables_are_bad():
    #global ariables are bad accepts no arguemnts
    #it prints the value of the global variable number

    print('The value of the global variable number was changed in ', end='')
    print('change_global to the value of: ', number)
    
#gloabal constant for program 5-15
contribution_rate = 0.05

def pay_me(): #program 5-15
    #pay me accepts no arguemtns
    #It prompts the user for gross pay and amount of bonuses
    #it calls show_pay, passing gross
    #and show_bonus, passing bounus
    gross = int(input('Please enter the amount for gross pay: '))
    bonus = int(input('Please enter the amount of bonuses: '))
    print()
    
    show_pay(gross)
    
    show_bonus(bonus)
def show_pay(gross):
    #show pay accept a float for gross
    #it caluclates teh contribution = gross * the global constant
    #it outputs the conribution for gross pay
    
    gross_pay = gross * contribution_rate
    print('Contribution for gross pay: $', format(gross_pay, ',.2f'), sep='')

def show_bonus(bonus):
    #show_bonus accept a float for bonus
    #it calcualtates the contribution = bonus * contribution_rate
    #it outputs the contribtuion for bounsus
    
    bonuses = bonus * contribution_rate
    print('Contribution for bonuses: $', format(bonuses, ',.2f'), sep='')
    
import random #this only needs to be done once and it is usable in every function

def random_numbers(): #program 5-16
    #random_numbers accept no arguemtns
    #it generatea a random integer from 1-10
    #output the number to the user
    
    number = random.randint(1, 10)
    print('The random number is: ', number)
    
def random_numbers2(): #program 5-17
    #random number 2 accepts no arguemtns
    #it loops 5 times assigning a random integer from 1-100 to number
    #it outputs the random integer for each iteration
    
    
    for numbers in range(5):
        number = random.randint(1, 100)
        print(number)
        
def random_numers3(): #program 5-18
    #random number 3 accepts no arguemtns
    #it loops 5 times assigning a random integer from 1-100 to number
    #it outputs the random integer for each iteration
    
    for numbers in range(5):
        print(random.randint(1, 100))
        
def dice(): #program 5-19
    #dice accepts no arguments
    #it loops until the user enters "n" pr "N" to stop
    #each iteration prints two random 6-sided die rolls
    #it prompts the user to roll agian (y/n)
    
    #roll dice
    print('Rolling your dice...')
    #find random number
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    #display resutls
    print('Your two rolls are: ', dice1, 'and', dice2)
    print()
    #ask if to go again
    go_on = str(input('Try your luck again? (y/n) '))

    while go_on == 'Y' or go_on == 'y':
        print('Rolling your dice...')
        print('Your two rolls are: ', end='')
        print(random.randint(1, 6), 'and', random.randint(1, 6), '\n')
        go_on = str(input('Try your luck again? (y/n)'))
        
def coin_toss(): #program 5-20
    #coin toss accepts no arguments
    #it sets three named constants for heads, tails, and tosses
    #it loops for 10 tosses using a random integer from 1 or 2 to determine
    #if the coin flip resultied in heads or tails
    
    HEADS = 1
    TAILS = 2
    TOSSES = 10
    
    #loop for tosses, determining heads or tails
    for toss in range(TOSSES):
        coin = random.randint(1,2)
        if coin == HEADS:
            print('Heads!')
        else:
            print("Tails!")
            
def total_ages(): #program 5-21
    #total ages accepts no arguemtns
    #it prompts the user for two ages and passes those values to calculate_ages()
    #it uses the return value to print the total ages
    
    #get input from the user
    age1 = int(input('Please enter your age: ' ))
    age2 = int(input('Please enter the age of your best friend: '))
    
    #call calculate ages, passing age1 and age2 and assign the reutn value to the total
    total = calculate_ages(age1, age2)
    
    #output the result
    print("\nTogehter you are", total, 'years old.')
    
def calculate_ages(age1, age2):
    #calculate ages receives values for age1 and age2
    #it add the two ages together
    #and returns the result

    #calculate the total age
    total_ages = age1 + age2
    
    #return the value
    return total_age
    
#declare global constant for program 5-22
discount_percent = 0.20

def sale_price(): #Progarm 5-22
    #sale price accept no arguemtns
    #it calls get regular price to get input form the user
    #it calcualtes teh sale price by taking the regular price and subtracting the
    #return result of discount()
    #it outputs the sale prince
    
    reg_price = get_regular_price()
    
    sale = reg_price - discount(reg_price)
    
    print('The slae price is: $', format(sale, ',.2f'), sep='')
def get_regular_price():
    #get reuglar price accept no arguemtns
    #it prompts the user to input the item's regular price
    #and returns that value
    
    price = float(input('Please enter the reglar price of the item: '))
    return price

def discount(price):
    #discount accepts an arguemtn for the float price
    #it returns the discount price @ 20% off using
    pass

def commission_rate(): #program 5-23
    #commission rate accepts no argumetns
    #it calls get_sales adn get_advanced_pay
    #It calls determine_comm_rate passing sales
    #it caluclat ehe pay and outputs the pay
    #it determines if the pay is negative and outputs if the salesperson
    #the amount the salesperson must reimburst the company
    #the global constant discount_percent
    
    sale_amount = get_sales()
    
    advanced_pay = get_advanced_pay()
    
    comm_rate = determine_comm_rate(sale_amount)
    
    pay = ((sale_amount * comm_rate) - advanced_pay) + sale_amount
    
    print('\nThe total pay with commission is $', format(pay, ',.2f'), sep='')
    
    if pay < 0:
        print('\nThe salesperson must reimburse the company', pay * -1, sep='')
def get_sales():
    #get sales accepts no arguements
    #it prompts the uesr to input the toal monthly sales
    #and returns the monthly sales
    sale_amount = int(input('Please enter the amount of sales for the month: '))
    return sale_amount

def get_advanced_pay():
    #get advanced pay accepts no arguments
    #it prompts the suer to enter any advanced pay, or 0 for none
    #it returns advanced pay
    advanced_pay = float(input('Please enter any advanced pay you recived (0 for none): '))
    return advanced_pay

def determine_comm_rate(sale_amount):
    #determies comm rate accepts a float for sales
    #it calcualtes the commission rate for sales
    #and returns the calculated rate
    if sale_amount < 10000:
        rate = 0.10
    elif sale_amount < 14999:
        rate = 0.12
    elif sale_amount < 17999:
        rate = 0.14
    elif sale_amount < 21999:
        rate = 0.16
    elif sale_amount < 22000:
        rate = 0.18
        
def square_root(): #program 5-24
    #accept no arguemnts
    #prompts the user for a number
    #it then caluclates the sqaure root using math module
    #output a message with the sqaure root of th number
    
    import math
    #user input accepted as a float
    num = float(input("Please enter a value to find the square root: "))
    
    #calculations
    sqaure = math.sqrt(num)
    
    print('The sqaure root of', num, 'is:', sqaure)
    
def hypotenuse(): #program 5-25
    #accepts no arguments
    #propts the user for the length of two sides A and B
    #then it clculates the hypotenuse using the math module
    #finnaly it outputs the info
    
    #find the sides
    side_a = float(input("Enter the length of side A: "))
    side_b = float(input('Enter the length of side B: '))
    
    #caluclate the lenth of the hyptoneuse using math.module
    hypotenuse = math.hypot(side_a, side_b)
    
    #display info
    print('The length of the hypotenus is: ', hypotenuse)
def graphic_fun(): #program 5-33
    #draws a pattern usign functions
    #set variables
    square(x, y, width, color) 
    