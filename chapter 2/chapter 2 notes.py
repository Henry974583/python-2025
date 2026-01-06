# chapter 2 pratice programs
def comment_example():
    # comment example accepts no arguments
    # it demonstrates how to write a function docstring
    # it returns nothing, but outputs a simple message
    print ("hello world!")
    
def program2_1(): #apostrophe output
    print ('kate austen')
    print ('123 full circle drive')
    print ('asheville, NC 28899')
    
def program2_4():
    print('your assignment is to read "hamlet" by tomorrow.')
    
def program2_7(): #variable demo 1
    #this program demonstrates a variable
    room = 503
    print('I am staying in room number')
    print(room)
    
def program2_8(): #variable demo 2
    #create two variables: top_speed and distance
    top_speed = 160
    distance = 300
    
    #display the values referenced by the variables
    print('the top speed is')
    print(top_speed)
    print('The distance traveled is')
    
def program2_9(): #variable demo 3
    #this program demonstrates outputting a variable
    room = 503
    print ('I am staying in room number', room)
    
def program2_10(): #variable demo 4
    #this program demonstrates outputting a variable
    #assign a vaule to the dollars variable
    dollars = 2.75
    print('I have' , dollars, 'in my account.')

    #reassign dollars so it references a different value
    dollars = 99.95
    print('I have' , dollars, 'in my account.')
    
def program2_11(): #string variable
    #create variables to feference two strings.
    first_name = "kathryn"
    last_name = "marino"
    
    #Display the values referenced by the variables
    print (first_name, last_name)
    
def program2_12(): #string input
    #Get the user's first name
    first_name = input('Enter your first name: Henry ')
    
    #Get the user's last name
    last_name = input('Enter your last name: Baier ')
    
    #Print a greeting to the user
    print('Hello', first_name, last_name)
    
def program2_13(): #input
    #Get the user's name, age, and income
    name = input('What is your name? ')
    age = int(input('What is your age? '))
    income = float(input('What is your income? '))
    
    #display the data.
    print('Here is the data you entered:')
    print('Name:', name)
    print('age:', age)
    print('Income:', income)
    
def program2_14(): #simple math
    #Assign a value to the salary variable
    salary = 2500.0
    
    #Assign a value to the bonus variable
    bonus = 1200.00
    
    #Calculate the total pay = salary + bonus
    pay = salary + bonus
    
    #Display the pay
    print('Your pay is', pay)
    

def sale_price():
    #this program gets an item's original price and
    #calculates the sale price, with a 20% discount
    
    #Get the item's original price
    original_price = float(input("enter the item's original price: "))
    
    #calculate the amount of the discount
    discount = original_price * 0.2
    
    #Calculate the sale price
    sale_price = original_price - discount
    
    #Display the sale price
    print('The sale price is', sale_price)
    
def get_average():
    #Get three test scores and assign them to variables
    #test1, test2, and test3
    #output the average
    
    test1 = float(input('Enter the first test score'))
    test2 = float(input('Enter the second test score'))
    test3 = float(input('Enter the third test score'))
    
    #Calculate the average of the three scores
    #assign the result to the variable average
    
    average = (test1 + test2 + test3) / 3.0
    
    #output the average
    print('The average score is:', average)
    
def program2_17(): #Time converter
    #get a number of seconds from the user
    total_seconds = float(input("Enter the number of seconds: "))
    
    #Get the number of hours
    hours = (total_seconds // 60) % 60
    
    #Get the remaining minutes
    minutes = (total_seconds // 60) % 60
    
    #get the number of reamaining seconds
    seconds = total_seconds % 60
    
    #output the results
    print('Here is the time in hours, minutes, and seconds: ')
    print('Hours:', hours)
    print('Minutes:', minutes)
    print('Seconds:', seconds)
    
def future_value():
    #get the desired futrue value, intrest rate, and years
    #calculate the amount that will have to be deposited
    #output the result
    
    #get the desired futre value
    desired_value = float(input('Enter the desired future value: '))
    
    #get the annual interst rate
    rate = float(input('Enter the desired interst rate: '))
    
    #get the number of years that the money will apperciate.
    years = int(input('Enter the number of years the money will grow: '))
    
    #calculate the amount needed to deposit
    present_value = desired_value /(1.0 + rate)**years
    
    #output the amount needed to deposit
    print('You will need to deposit $', format(present_value, '.2f'), sep='')
    
def program2_19(): #non formatted float
    #This program demonstrates how a floating-point
    #number is displayed with no formating
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    print('The monthlypayment is', monthly_payment)
    
def program2_20(): #formatted float
    #this program deomonestrates how a floating-point
    #number can be formatted.
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    print('The monthly payment is',
            format(monthly_payment, '.2f'))
    
def program2_21(): #currency display
    #this program demonstrates how a floating-point
    #number can be displayed as a currency
    monthly_pay = 5000.0
    annual_pay = monthly_pay * 12
    print('Your annual pay is $',
          format(annual_pay, ',.2f'),
          sep='')
    
def program2_22(): #colums justified field width
    #this program displays the following
    #floating-point numbers in a column
    #with their decimal points aligned
    num1 = 127.899
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999
    
    #display each number in a justified field of 7 spaces
    #with 2 decimal places
    print(format(num1, '7.2f'))
    print(format(num2, '7.2f'))
    print(format(num3, '7.2f'))
    print(format(num4, '7.2f'))
    print(format(num5, '7.2f'))
    print(format(num6, '7.2f'))
    
import turtle
def orion():
    #the function orion uses named constants to establish
    #each star location it's name, and to draw the
    #constellation using the turtle to draw
    
    #setup turtle
    turtle.setup(500, 600)
    turtle.penup()
    turtle.hideturtle()
    
    #used name costant for each star
    LEFT_SHOULDER_X = -70
    LEFT_SHOULDER_Y = 200
    turtle.goto(-70,200)
    turtle.dot()
    turtle.write('betelgeuse')
    turtle.pendown()
    turtle.goto(-40,-20)
    turtle.penup()
    
    RIGHT_SHOULDER_X = 80
    RIGHT_SHOULDER_Y = 100
    turtle.goto(80,100)
    turtle.dot()
    turtle.write('meissa')             #left shoulder - betelgeuse
     
    LEFT_BELSTAR_X = -40        #right shoudler - meissa
    LEFT_BELSTAR_Y = -20   #left belt - alnilak
    turtle.goto(-40,-20)
    turtle.dot()
    turtle.write('alnilak')             #mid belt - alnilam
     
    MIDDLE_BELSTAR_X = 0        #right belt - mintaka
    MIDDLE_BELSTAR_Y = 0
    turtle.pendown()     #left knee - saiph
    turtle.goto(0,0)
    turtle.dot()
    turtle.write('alnilam')
    turtle.penup()               #right knee - rigel
    
    RIGHT_BELSTAR_X = 40
    RIGHT_BELSTAR_Y = 20
    turtle.pendown()
    turtle.goto(40,20)
    turtle.dot()
    turtle.write('mintaka')
    turtle.penup()
    
    LEFT_KNEE_X = -40
    LEFT_KNEE_Y = -100
    turtle.goto(-90,-180)
    turtle.dot()
    turtle.write('saiph')
    turtle.pendown()
    turtle.goto(-40,-20)
    turtle.penup()
    
    RIGHT_KNEE_X = 120
    RIGHT_KNEE_Y = 140
    turtle.goto(120,-140)
    turtle.dot()
    turtle.write('rigel')
    turtle.pendown()
    turtle.goto(40,20)
    turtle.penup()
    turtle.goto(40,20)
    turtle.pendown()
    turtle.goto(80,100)
    turtle.penup()
    turtle.done()