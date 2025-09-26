def personal_info():
#personal_info() accepts no arguments
#this program displays your personal information
#outputs name, adress, city, state, zip, cell number, projected college major

    print('Name: Henry Baier')
    print('Adress: 118 S forestview ct Wichita, KS 67235')
    print('Number: 316-708-9020')
    print('Projected College Major: Forensics science')
    
def total_purchase():
#total_purchase() accepts no arguments
#this program finds the subtotal, tax and total, of 5 itesms prices
    
    item_1 = float(input('Please enter a price for your first item: '))
    item_2 = float(input('Please enter a price for your second item: '))
    item_3 = float(input('Please enter a  price for your third item: '))
    item_4 = float(input('Please enter a price for your fourth item: '))
    item_5 = float(input('Please enter a price for your fith item: '))
    
    #calculate the subtotal
    sub_total = (item_1 + item_2 + item_3 + item_4 + item_5)
    #calculate the tax
    tax = (sub_total * 0.07)
    #calulate the total
    total = (sub_total + tax)
    #display the cost of the items
    print('Subtotal:\t$',(format(sub_total,"7.2f")))
    print('Tax:\t\t$',(format(tax,"7.2f")))
    print('Total:\t\t$',(format(total,"7.2f")))
    
def distance_traveled():
#distance_travled() accpets no arguments
#this program find how many miles you will travel in a set amount of hours using your mph
    speed = float(input('How fast are you driving? '))
   
    #calculate how far they will tarvelin the set time
    six_hours = (speed * 6)
    ten_hours = (speed * 10)
    fiftenn_hours = (speed * 15)
    
    #display the information
    print('At 60 miles per hour you will travel', format(six_hours,'.0f'), "miles in 6 hours.")
    print('At 60 miles per hour you will travel', format(ten_hours,'.0f'), "miles in 10 hours.")
    print('At 60 miles per hour you will travel', format(fiftenn_hours,'.0f'), "miles in 15 hours.")

def sales_tax():
#sales_tax() accepts no arguments
#this program displays the amount of the purchase, the state sale tax, the ocuntry sales tax, the total sales,
    item_price = float(input('Enter the sale amount: '))
    state_tax = (item_price * 0.05)
    country_tax = (item_price * 0.025)
    total_tax = (state_tax + country_tax)
    total_sale = (total_tax + item_price)
    print('Your purchase price was: \t$', (format(item_price,'7.2f')))
    print('Your state tax amount is: \t$', (format(state_tax,'7.2f')))
    print('Your country tax amount is: \t$',(format(country_tax,'7.2f')))
    print('Your total tax is: \t\t$', (format(total_tax,'7.2f')))
    print('Your total sale is: \t\t$', (format(total_sale,'7.2f')))
    
def tip_tax_total():
#tip_tax_total() accpets no arguments
#this program calculates how much you would need to tip based on a precnetage and the total bill
    sale_amount = float(input('Please enter the sale amount: '))
    tip_amount = (sale_amount * 0.018)
    sales_tax = (sale_amount * 0.07)
    total_bill = (sale_amount + tip_amount + sales_tax)
    print('The sale was: \t\t\t$', (format(sale_amount, '7.2f')))
    print('The tip amount is: \t\t$', (format(tip_amount, '7.2f')))
    print('The sales tax amount is: \t$', (format(sales_tax, '7.2f')))
    print('The total bill is: \t\t$', (format(total_bill, '7.2f')))
    
def temp_converter():
#temp_converter() accpets no arguments
#this program uses equations to convert degrees to celsius
    degrees_celsius = float(input('Please enter the degrees Celsius: '))
    degrees_fahrenheit = (1.8 * degrees_celsius + 32)
    print(format (degrees_celsius, '.0f'), 'degrees celsius is', degrees_fahrenheit,'degrees fahrenheit.')

def cookie_monster():
#cookie_monster() accepts no arguments
#this program aks the user how many cookies they want and tells them the ingredients and hou much they need
    cookie_amount = float(input('How many cookies do you want to make? '))
    oz_sugar = (cookie_amount * 0.5)
    oz_butter = (cookie_amount * 0.3333)
    oz_flour = (cookie_amount * 0.9166)
    cups_sugar = ( oz_sugar // 8)
    cups_butter = (oz_butter // 8)
    cups_flour = (oz_flour // 8)
    oz_sugar = oz_sugar % 8
    oz_butter = oz_butter % 8
    oz_flour = oz_flour % 8
    print('For', format(cookie_amount, '.0f'), 'cookies you will need:')
    print(format(cups_sugar, '.0f'), 'cup(s)', format (oz_sugar, '.0f'), 'ounces of sugar.')
    print(format(cups_butter, '.0f'), 'cup(s)', format (oz_butter, '.0f'), 'ounces of butter.')
    print(format(cups_flour, '.0f'), 'cup(s)', format (oz_flour, '.0f'), 'ounces of flour.')
    
def class_demographics():
#class_demographics() accpets no arguments
#this program the program displays the precent of male and females in your class
    number_females = float(input('Enter the number of females: '))
    number_males = float(input('Enter the number of males: '))
    total_students = number_females + number_males
    female_precent = number_females / total_students * 100
    male_precent = number_males / total_students * 100
    print('The class consists of', format(female_precent, '.0f'), '% females and', format(male_precent, '.0f'), '% males.')
    
import turtle
def compas():
#this program makes a compass
    turtle.setup(0,0)
    turtle.penup()
    turtle.hideturtle()
#make north, northeast, and northwest
    turtle.pensize(5)
    turtle.pendown()
    turtle.goto(0,100)
    turtle.penup()
    turtle.goto(0,110)
    turtle.write('N', font=('Arial', 16))
    turtle.goto(0,0)
    turtle.pensize(3)
    turtle.pendown()
    turtle.goto(-50,50)
    turtle.goto(0,0)
    turtle.goto(50,50)
    turtle.goto(0,0)
    turtle.penup()
#make east
    turtle.pensize(5)
    turtle.pendown()
    turtle.goto(100,0)
    turtle.penup()
    turtle.goto(110,0)
    turtle.write('E', font=('Arial', 16))
    turtle.goto(0,0)
#make south, southeast, and southwest
    turtle.pensize(5)
    turtle.pendown()
    turtle.goto(0,-100)
    turtle.penup()
    turtle.goto(0,-130)
    turtle.write('S', font=('Arial', 16))
    turtle.goto(0,0)
    turtle.pensize(3)
    turtle.pendown()
    turtle.goto(-50,-50)
    turtle.goto(0,0)
    turtle.goto(50,-50)
    turtle.goto(0,0)
    turtle.penup()
#make west
    turtle.pensize(5)
    turtle.pendown()
    turtle.goto(-100,0)
    turtle.penup()
    turtle.goto(-120,0)
    turtle.write('W', font=('Arial', 16))
    turtle.done()
    
import turtle
def five_rings():
#this program makes 5 rings with diffrent colors
    turtle.setup(0,0)
    turtle.penup()
    turtle.hideturtle()
#ring one blue
    turtle.goto(500,40)
    turtle.pensize(5)
    turtle.pencolor('light blue')
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
#ring two yellow
    turtle.goto(650,-40)
    turtle.pensize(5)
    turtle.pencolor('yellow')
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
#ring three black
    turtle.goto(800,40)
    turtle.pensize(5)
    turtle.pencolor('black')
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
#ring four green
    turtle.goto(950,-40)
    turtle.pensize(5)
    turtle.pencolor('green')
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
#ring five red
    turtle.goto(1100,40)
    turtle.pensize(5)
    turtle.pencolor('red')
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.done()
    