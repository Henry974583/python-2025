import random
def card_dealer_main(): #program 9-1
    # card dealer main accepts no arguments
    # it calls create_deck to generate a deck of cards
    # and takes input from the user for the number of cards to deal
    # it then calls deal_cards to deal the number of cards to the user
    deck = create_deck()
    
    go = False
    while go == False:
        try:
            card_amnt = int(input("Enter the amount of cards to deal: "))
            if card_amnt > 0:
                if card_amnt <= len(deck):
                    go = True
                else:
                    print("No more than 52 cards. This uses a standard playing deck.")
            else:
                print("Has to be a number greater than 0.")
        except:
            go = False
    
    deck = create_deck()
    deal_cards(deck, card_amnt)
def create_deck():
    # create deck accepts no arguments
    # it geneerates a dictionary with the name of the card a the key
    # and the point value of the card as the value
    # and returns the dictionary of cards
    deck = {'Ace of Spades' : 1, '2 of Spades' : 2, '3 of Spades' : 3,
        '4 of Spades' : 4, '5 of Spades' : 5, '6 of Spades' : 6,
        '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9,
        '10 of Spades' : 10, 'Jack of Spades' : 10, 'Queen of Spades' : 10,
        'King of Spades' : 10,
        
        'Ace of Hearts' : 1, '2 of Hearts' : 2, '3 of Hearts' : 3,
        '4 of Hearts' : 4, '5 of Hearts' : 5, '6 of Hearts' : 6,
        '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9,
        '10 of Hearts' : 10, 'Jack of Hearts' : 10, 'Queen of Hearts' : 10,
        'King of Hearts' : 10,
        
        'Ace of Clubs' : 1, '2 of Clubs' : 2, '3 of Clubs' : 3,
        '4 of Clubs' : 4, '5 of Clubs' : 5, '6 of Clubs' : 6,
        '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9,
        '10 of Clubs' : 10, 'Jack of Clubs' : 10, 'Queen of Clubs' : 10,
        'King of Clubs' : 10,
        
        'Ace of Diamonds' : 1, '2 of Diamonds' : 2, '3 of Diamonds' : 3,
        '4 of Diamonds' : 4, '5 of Diamonds' : 5, '6 of Diamonds' : 6,
        '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9,
        '10 of Diamonds' : 10, 'Jack of Diamonds' : 10, 'Queen of Diamonds' : 10,
        'King of Diamonds' : 10}

    return deck

def deal_cards(deck, card_amnt):
    # deal cards accepts deck as a dictionary and number as an integer
    # it verifies number isn't greater than the deck size
    # if it is, it sets the number to the length to the deck size to not
    # exceed the maximum index
    # it randomly selects and removes a key/value from the deck
    # it prints the card and calculates the value of the hand
    # after all cards have been dealt, it outputs the total value of the hand
    
    # set hand to 0
    hand = 0
    print("\nHere is your hand: \n")
    # deal them a card
    for num in range(card_amnt):
        # get a random card
        card = random.choice(list(deck))
        # get the value of it, and
        value = deck.pop(card)
        hand += value
        print(card)
    
    print(f"\nThe value of your hand is {hand}.")

card_dealer_main()