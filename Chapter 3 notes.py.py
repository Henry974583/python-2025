def test_average():
# test_average() accepts no arguments
#this program ask the user for three test scores and then finds the average
    high_score = 95
    
#get the test scores
    score_1 = float(input('Enter the first score: '))
    score_2 = float(input('Enter the second score: '))
    score_3 = float(input('Enter the third score: '))
    
#find the average test score
    average = (score_1 + score_2 + score_3) / 3

#output the average
    print('The average score is: ', format(average, '.2f'))
    
#if the average is higher than the high score congrulate the user
    if average >= high_score:
        print('Congratulations!')
        print('That is a high score!')
        
def auto_repair_payroll():
#auto_repair_payroll() accepts no arguments
#it prompts the user for hours worked and pay rates
#it determines if the employe worked overtime
#and calculates and outputs the gross pay
    
    base_hours = 40 #base weekly hours
    ot_multiplier = 1.5 #overtime rate
    
    #get hours worked and pay rates from the user
    hours_worked = int(input('Enter the number of hours worked: '))
    pay_rate = int(input('Enter your houlry pay rate: '))
    
    #calulate gross pay
    if	hours_worked > base_hours:
        overtime_hours = hours_worked - base_hours #find hours worked over 40
        overtime_pay = overtime_hours * pay_rate * ot_multiplier
        
        #calculate wage for base pay + overtime
        gross_pay = base_hours * pay_rate + overtime_pay
    
    else: #no overtiem, calculate hours * rate
        gross_pay = hours_worked * pay_rate
    
    #output pay
    print('your gross pay is $', format(gross_pay, ',.2f'), sep='')
    
def password_verifier(): #program 3-3
    #password_verifier() accepts no arguments
    #it prompts the user for a password
    #it outputs a response depending if the password
    #is correct or incorrect. The password is 'prospero'

    #get the password
    password = input('Please enter the password: ')
    
    #check the password
    if password == 'prospero':
        print('Password accepted')
    else:
        print('Password is invalid')

def sort_names(): #program3-4
    #sort names accepts no argumetns
    #it prompt the user for two names in order first, last
    #it sort and output the names alphabetically
    
    #get the names from the user
    name1 = input('Enter the first name (last, first): ')
    name2 = input('Enter the second name (last, first): ')
    
    print('Here are the naems, sorted alphabetically.')
    
    #compare and output the names from greatest to least
    if name1 < name2:
        print(name1)
        print(name2)
    else:
        print(name2)
        print(name1)
        
def