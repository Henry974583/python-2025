#program 10-11
import coin

def main():
    #creates 3 unique instances of a coin toss
    #it outputs the initial value
    #toss the coin,
    #and outputs the new value
    
    my_coin = coin.Coin()
    
    #instances
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()
    #tossing
    print('Your three coins are facing...')
    coin1.toss()
    coin2.toss()
    coin3.toss()
    
    print('Coin 1 is:',coin1.get_sideup())
    print('Coin 2 is:', coin2.get_sideup())
    print('Coin 3 is:', coin3.get_sideup())
    print('I am tossing your three coins...')
    print()
    #tossing again
    coin1.toss()
    coin2.toss()
    coin3.toss()
    print('here are your coins again after tossing them...')
    print('Coin 1 is:', coin1.get_sideup())
    print('Coin 2 is:', coin2.get_sideup())
    print('Coin 3 is:', coin3.get_sideup())
    
main()