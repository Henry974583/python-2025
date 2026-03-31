#program 10-8: account_test.py
#import
import bankaccount

def main(): #program  10-8
    #accepts no arguments
    #it takes input fromt he user for a starting balance
    #it uses the BankAccount class in bankaccount.py to create
    #an object savings passing the starting balance
    #it takes input from the user for a paycheck
    #it displays the current balance using the get_balance() method
    #It takes input form the user for a withdrawl and uses the withdraw() method
    #and outputs the final balance
    
    
    starting_balance = float(input('Enter your starting balance: '))
    
    bank_account = bankaccount.BankAccount(starting_balance)
    
    #paycheck
    
    paycheck = float(input('Enter the amount of your paycheck to deposit'))
    bank_account.deposit(paycheck)
    #withdraws
    print()
    #print(
    print(bank_account.get_balance())
    
    #withdraw amount
    withdraw_ammount = float(input('How much would you like to withdraw: '))
    bank_account.withdraw(withdraw_ammount)
    
    print('Withdraw succesful')
    
    #new balance
    print(bank_account.get_balance())
    
    

main()