#program 10-16: prickel_cellphone.py

import pickle
import cellphone

def main():
    #recieves no arguments
    #it opens a file called cellphones.dat
    #and loops until the user enters a n to continue
    #each iteratoin of the loop the user is prompted
    #to enter phone data; manufacturere, modekl, and retail price
    #an object is created using the CellPhone calss in cellphone.py
    #with the attributes manufact, model, and retail_price
    #the object is pickled to the file cellphones.dat
    
    #open fie
    outfile = open('cellphones.dat', 'wb')

    counter = 0
    go_again = 'y'
    while go_again == 'y':
        
        
        #inputs
        manu = str(input('Enter the phone manufacturer: '))
        model = str(input('Enter the phone model: '))
        price = float(input('Enter the retial price: '))
        
        info = cellphone.Cellphone(manu, model, price)
        #set them to the class
        info.set_manufact(manu)
        info.set_model(model)
        info.set_retail_price(price)
        
        #pickle them
        outfile.dump(info.get_manufact())
        outfile.dump.(get_model())
        outfile.dump(info.get_retial_price())
        
        
        
main()
        
        

