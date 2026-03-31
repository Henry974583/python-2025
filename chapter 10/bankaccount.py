#the bankaccount class simulatesa a bank account

class BankAccount: #program 10-7
    
    #the __init__ method accepts an argument for the account's balance
    #if is assigned to the __balance attribute
    
        def __init__(self, bal):
            self.__balance = bal
        
        #the deposit method makes a deposit into the account
        
        def deposit(self, amount):
            self.__balance += amount
            
        #the withdraw method makes a withdrawl from the account
            
        def withdraw(self, amount):
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                print('Error insufficient funds')
                
        #the get_balance emthod returns the account balance
            
        def get_balance(self):
            return self.__balance