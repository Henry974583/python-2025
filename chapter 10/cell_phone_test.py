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
    price = float(input("enter the retial price for your:"))
    #call class
    info = cellphone.CellPhone()
    print()
    #assign manufactuer
    info.set_manufact(manu)
    #assing model
    info.set_model(model)
    #assign price
    info.set_price(price)
    
    print('Here is the data you entered:')
    print('Manufacturer:', info.get_manufact)
    print('Model:', info.get_model)
    print('Retail Price: $', info.get_retail_price)
    
main()

    
    
    