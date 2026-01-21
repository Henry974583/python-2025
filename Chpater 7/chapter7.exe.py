import random
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
    accounts = []
    try:
       #input
        search = int(input('Enter an account number: '))
        #append
        accounts.append(search)
        #open the file
        infile = open('charge_accounts.txt', 'r')
        
        account_numbers = infile.readlines()
        
        for  in accounts
            print('succes')
            
    except:
        print('err')
        
        
    