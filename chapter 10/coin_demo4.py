#program 10-6 conin_deom4
#import coin
import coin

def main(): #program 10-6
    #accepts no a arguements
    #it creates an object my_coin using the COin class in coin.py
    #it uses the get_sideup() method in the coin class to display the starting state
    #it loops 10 times, tossing the coin with the toss() method
    #and displaying the side again with get_sideup() method
    
    my_coin = coin.Coin()
    toss = 1
    print('This side is up: ', my_coin.get_sideup())
    print('Tossing the coin ten times...')
    
    for toss in range(0,11):
        my_coin.toss()
        print('Toss', toss,':', my_coin.get_sideup())
        toss += 1
        
        
main()