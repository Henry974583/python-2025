import random
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
    total = sum(numberlist)
    divide = len(numberlist)
    list_average = total / divide
    
    #print info
    print('The average of the numbers', numberlist, 'is', list_average)
    
    
def list_function(): #program 7-10
    #list function accepts no arguments
    #it creates a list [2, 4, 6, 8, 10]
    #it passes the list to get_total
    #it prints the returned total
    
    #list
    numbers = [2, 4, 6, 8, 10]

    #call function
    total = get_total(numbers)
    
    #print info
    print('The total of', numbers, 'is:', total)
def get_total(numbers):
    #get accepts a list of numbers
    #it calulates and returs the total
    
    #find sum
    total = sum(numbers)
    
    #returns
    return total
    
def list_return(): #program 7-11
    #list return accepts no arguments
    #it calss get_values to create a list reference
    #and outputs the numbers in the list
    numbers = get_values()
    
    print('You entered the numbers:', numbers)

def get_values():
    #get values accepts no arguments
    #it creates and empty aggregator
    #and loops, prompting the user to enter a value
    #and appending the value to the list
    #and to if they want add another value
    #it returns the reference to the list

    #variables
    keep_going = True
    numbers = []
    
    #input to get numbers
    while keep_going == True:
        number = int(input('Input a number: '))
        
        #append
        numbers.append(number)
        
        #ask if they want to keep going
        keep_going = str(input('Do you want to add another number? (y/n) '))
        
        #loop
        if keep_going == 'y':
            keep_going = True
            
        #no loop just return
        if keep_going == 'n':
            keep_going = False
            return numbers
        
def test_calc(): #program 7-12
    #accepts no arguments
    #it ask the user for test scores and writes them to a list
    #it then finds the lowest score
    #and removes it from the list
    #finaly it finds the average
    
    #variables and list
    keep_going = 'y'
    scores = []
    
    #input to get numbers
    while keep_going == 'y':
        number = int(input('Enter a score: '))
        #do they want to contiune
        keep_going = str(input('Enter another score? (y/n)'))
        #add number to list
        scores.append(number)
    #when we stop
    if keep_going == 'n':
        #find the lowest score and print it
        lowest_score = min(scores)
        print('Dropping the lowest score of', lowest_score)
        
    #remove the final score
        scores.remove(lowest_score)
        
    #find the sum and then divide to find average
    total = sum(scores)
    divide = len(scores)
    average = total / divide
       
    #print the info
    print('The average score, with', lowest_score, 'dropped from the scores, is:', average)
    
def list_writelines(): #program 7-13
    #list writelines accepts no arguments
    #it writes the entire contents of a list
    #to the file cities.txt
    
    cities = ['Kansas City ', 'Lawrence ', 'Wichita ', 'Manhattan ']
    
    try:
        #open file
        outfile = open('cities.txt', 'w')
        
        #write the list to the file
        outfile.writelines(cities)
        
        #close the file
        print('All data written to cities.txt')
        outfile.close()
        
    except exception as err:
        print(err)
        
def list_write(): #program 7-14
    #list writelines accepts no arguments
    #it writes the entier contents of a list
    #to the file cities.txt
    
    cities = ['Kansas City ', 'Lawrence ', 'Wichita ', 'Manhattan ']
    
  
    #open the file
    outfile = open('cities.txt', 'w')
    
    for city in cities:
        
        #write the list to the file
        outfile.write(city + '\n')
        
        #close the file
        print('All data written to cities.txt')
        outfile.close()
            

def list_read(): #program 7-15
    #list read accepts no arguments
    #it reads from cities.txt and aggregates the data
    #to the list cities, stripping the /n from each
    
    try:
        #open
        infile = open('cities.txt', 'r')
        
        #read
        cities = infile.readlines()
        
        #close
        infile.close()
        
    except:
        print('Error reading from the file.')
        
    #variables
    index = 0
        
    #strip ht enew line and reassing it to the list
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
    print('Here is the information read from cities.txt')
    print(cities)
    
    
def list_write_numbers(): #program 7-16
    #list write numbers accepts no arguments
    #it saves a list of integers [1, 2, 3, 4, 5, 6, 7]
    #to the file numberlist.txt
    
    #create list
    numbers = [1, 2, 3, 4, 5, 6, 7]
    
    #open
    outfile = open('numberlist.txt', 'w')
    
    #loop to write the numbers to the list
    for number in numbers:
        outfile.write(str(number) + '\n')
        
    #close file
    outfile.close()
    print('All numbers saved to numberlist.txt')
    
def list_read_numbers(): #program 7-17
    #list read numbers accepts no arguments
    #it reads integers from the file numberslist.txt
    #and aggregates them to a list
    
    #list
    numbers = []
    
    try:
        #open
        infile = open('numberlist.txt', 'r')
        
        #loop
        for num in infile:
            numbers.append(int(num.rstrip('\n')))
            
            infile.close()
            
    except Exception as err:
        print(err)
    print('Here is the lsit created from numberlist.txt:')
    print(numbers)
    
def random_numbers(): #pogram 7-18
    #random numbers accepts no argumetns
    #it creates a 2D list with a maxium row index of 3
    #and a maximum column index of 2
    #it uses nested loops to fill the 2D list wiht a random number
    #from 1-100
    
    #variables
    ROWS = 3
    COLS = 4
    
    values =[[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    
    #loop
    for row in range(ROWS):
        for col in range(COLS):
            values[row][col] = random.randint(1, 100)
            
    #output
    print(values)