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
    #list append accepts no arguments
    #it creates and empty list
    #and loop to append the list with input from th euser
    #then prompts to contiune
    
    #variables
    names = []
    
    #obtain name to add
    new_name = str(input('Enter a name: '))
    
    #add the name to the list
    names.append(new_name)
    
    #ask to go again
    choice = str(input('Add another name? (y to continue)'))
    print()
    while choice == 'y':
         #obtain name to add
        new_name = str(input('Enter a name: '))
    
        #add the name to the list
        names.append(new_name)
    
        #ask to go again
        choice = str(input('Add another name? (y to continue)'))
        print()
    #if they stop
    if choice == 'n':
        print('you entered the following names')
        for new_name in names:
            print(new_name)

def list_index(): #program 7-4
    #list index accepts no arguments
    #it creates a list of three food items
    #and prompt the user to replace on of the items
    #it searches the list for the index of the item
    #and prompts the user with a replacment food
    
    #vairables and list
    index = 0
    food_list = ['Burger', 'Pizza', 'Hotdog']
    
    #prompt user what to search for
    search = str(input('Enter the item to search for: '))
    
    #if item is found
    if search in food_list:
        #remove the item
        food_list.remove(search)
        #item found now input new item
        new_item = str(input('item found enter new item: '))
        
        #insert new item
        food_list.insert(0, new_item)
        #new list needs to be printed
        print('Here is the list: ',food_list)
        
    #if the item is not found
    if search not in food_list:
        print('Item not found')
        print('Here is the list: ', food_list)
        
def list_insert(): #program 7-5
    #list insert accepts no arguments
    #it prints hte original list of three names
    #it inserts a name in a list of names
    #at a specific index and prints the new list
    
    #list
    names = ['Bruce', 'Steve', 'Tony']
    
    #print current list
    print(names)
    
    #insert name
    names.insert(2, 'Sam')
    #print new list
    print(names)
    
    
def list_remove(): #program 7-6
    #list remove accepts no arguments
    #it creates a list of three food items
    #it removes the item from the list
    #or outputs a message if doesnt exist
    
    #vairables and list
    food_items = ["Burger", 'Pizza', 'Hotdog']
    found = False
    #print list
    print('Here is the list', food_items)
    
    #input for item to remove
    replace_item = str(input('Enter the item you want to remove '))
        
    #when found
    if replace_item in food_items:
        food_items.remove(replace_item)
        print('Here is the list', food_items)
        found = True
    
    else:
        print('Item not found')
        
def list_total(): #program 7-8
    #list total accepts no arguments
    #it creates a list of numbers [2, 4, 6, 8, 10]
    #and loops to accumulate the total of all the number
    #In the list
    
    #variables and list
    accumulator = 0
    numberlist = [2, 4, 6, 8, 10]
    
    #math
    total = sum(numberlist)

    #info print
    print('the average of the numbers', numberlist, 'is', total)
    
    
def list_avg(): #program 7-9
    #list avg accepts no arguments
    #it creates a list of numbers [2.5, 7.3, 6.5, 4.0, 5.2]
    #and calculates the average of the numbers using len
    
    #vairables and list
    numberlist = [2.5, 7.3, 6.5, 4.0, 5.2]
    
    #find average
    list_average = len(numberlist)
    print(list_average)
    
    #print info
    print('The average of the numbers', numberlist, 'is', list_average)