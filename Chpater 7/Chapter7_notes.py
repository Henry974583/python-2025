def example1():
    number = input('Enter a number: ')
    #validate input as an intger
    while not number.isdigit():        
        number = int(number)
        print(f'{number} successfully converted to an integer.')

def sales_list(): #program 7-1
    #sales list accepts no arguments
    #it creates a list NUM_DAYS long
    #and loops to accept input from the user
    #adding that input to the list
    
    #vairables
    NUM_DAYS = 5
    index = 0
    sales = [0] * NUM_DAYS
    
    #print header
    print('Enter the sales for each day')
    
    #loop
    while index < NUM_DAYS:
        print('Day #', index + 1, ':', sep='', end='')
        sales[index] = float(input())
        
        #increment
        index += 1
        
    #loop
    print('\nHere are the values you entered:\n')
    for sale in sales:
        print(sale)
        
def in_list(): #program 7-2
    #in list accepts no arguments
    #it creates a list of part numbers
    #v45, v65, vf750m vfr1100, vtx1300
    #and prompts the user for a string to search for
    #and prints if the list contains the search for a string
    
    #variables and list
    items = ['v45', 'v65', 'vf750', 'vfr1100', 'vfr1300']
    found = False
    
    #input
    item_name = str(input('Please enter a item'))
    
    if item_name in items:
        print('Part', item_name, 'was found in the list of part numbers')
    else:
        print('Part', item_name, 'Was not found')
        
def list_append(): #program 7-3