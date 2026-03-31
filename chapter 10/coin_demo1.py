#program 10-2 - coin_demo1.py
import coin

def main():
    #accetps no arguments
    #it uses the coin class to create an object
    
    #create an object from the coin class
    my_coin = coin.Coin()
    
    #display
    print('This side is up: ', my_coin.get_sideup())
    
    #toss coin
    print('Tossing the coin...')
    my_coin.toss()
    
    #display the side of the coin
    print('THis side is up: ', my_coin.get_sideup())
    
main()
