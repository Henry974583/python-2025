#program 10-13
import cellphone

def main():
    #it calls cellphone
    #and asks the user for the phone manufactuer
    #model number
    #annd price
    #and shows them what data they entered
    
    print('Welcom to the galactic phone database.')
    manu = str(input('Enter the phone manufactuer: '))
    model = str(input('Enter the phone model number: '))
    price = float(input("enter the retial price for your", manu, ', model', model,': '))
    #call class
    info = cellphone.CellPhone()
    
    