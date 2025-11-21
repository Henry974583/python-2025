import io
def line_numbers(): #exercise 3
    #accepts no arguemtns
    #it opens file steps.txt
    #and reads them
    #finally it prints them and assgins them a day

   #counter
    counter = 0
    try:
        #open file
        infile = open('steps.txt', 'r')
        
        #start loop
        for steps in infile:
            #read line
            linenumber = infile.readline()
            #strip the line
            linenumber = linenumber.rstrip()
            #increase counter
            counter += 1
            #print
            print(counter, ':\t', linenumber)
        #in case of error
    except IOError:
        print('Error: File not found')
        

def line_counter(): #excercise 4
    #accepts no arguments
    #it ask the user for a file name
    #and opens it
    #it then counts how many lines are in the file
    #and outputs how many are there
    
    #variables
    counter = 0
    
    #Inputs
    filename = input('Enter the file name to read: ')
    try:
        infile = open(filename, 'r')
        
        #count how many lines of text their are
        for names in infile:
            counter += 1
            
        #print
        print(filename, 'contains', counter, 'lines')
        
    except IOError:
        print('Error: File not found')