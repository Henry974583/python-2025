import random
import string

#this is writing to the file for encoded
file = open('storage_file.txt', 'w')
file.write('Hello, world')
file.close()
def menu():
    #no arguments
    #it ask the user for a input
    #runs the program for another and
    #loops it if they want another program
    
    go = 'y'
    while go == 'y':
        #print header
        print('1) file encryption')
        print('2) file decryption')
        print('3) unique words')
        print('4) world series winners')
        print('5) blackjack simulation')
        print()
    
        #ask for input
        choice = int(input('What program: '))
        
        #run program according to input
        if choice == 1:
            encryption()
        elif choice == 2:
            decryption()
        elif choice == 3:
            unique_words()
        elif choice == 4:
            world_series()
        elif choice == 5:
            card_dealer_main()
            
        go = str(input('Run another program (y/n)? '))
        print()
    if go == 'n':
        print('goodbye')
        
def encryption():
    #accepts no arguments
    #it opens a file and reads
    #next it encryptys it and
    #writes it to a file
    
    #create key and open files
    key = {'a': 'y', 'b': 's', 'c': 'K', 'd': '{', 'e': '1', 'f': 'Q', 'g': 'q', 'h': '*', 'i': 'L', 'j': ')', 'k': '#', 'l': '[', 'm': '8', 'n': 'D', 'o': ',', 'p': 'f', 'q': '^', 'r': '7', 's': '`', 't': 'x', 'u': '_', 'v': '0', 'w': 'M', 'x': 'u', 'y': '.', 'z': 'T', 'A': 'Y', 'B': '>', 'C': '$', 'D': 'j', 'E': 'F', 'F': 'O', 'G': 'I', 'H': 'A', 'I': 'l', 'J': 'P', 'K': 'p', 'L': 'n', 'M': 'c', 'N': 'X', 'O': '!', 'P': 'C', 'Q': '5', 'R': 'k', 'S': 'S', 'T': 'E', 'U': 'm', 'V': 't', 'W': '3', 'X': 'U', 'Y': '}', 'Z': 'H', '!': 'g', '#': '-', '$': 'e', '%': '%', '&': 'o', '(': ';', ')': '~', '*': 'd', '+': 'N', ',': '&', '-': 'z', '.': '(', '/': 'W', ':': 'v', ';': 'h', '<': 'i', '=': '2', '>': 'V', '?': 'R', '@': '@', '[': 'a', ']': 'r', '^': '4', '_': 'Z', '`': '9', '{': '=', '|': ']', '}': '|', '~': 'G', '0': 'J', '1': 'w', '2': '6', '3': '/', '4': 'B', '5': ':', '6': '+', '7': '<', '8': 'b', '9': '?', " ": " ", "\n" : "\n"}
    file = open("storage_file.txt", "r")
    encoded_file = open("encoded_file.txt", "w")

    #encode
    for line in file:
        encoded_line = ''
        
        for letter in line:
            encoded_line += key[letter]
            
        encoded_file.write(encoded_line)
    #close files
    file.close()
    encoded_file.close()
    print('Encrypted storage.txt to encoded_file.txt')
def decryption():
    #accepts no arguments
    #it reads a file
    #and decrypts it
    #print it
    
    #key and open files
    key = {'a': 'y', 'b': 's', 'c': 'K', 'd': '{', 'e': '1', 'f': 'Q', 'g': 'q', 'h': '*', 'i': 'L', 'j': ')', 'k': '#', 'l': '[', 'm': '8', 'n': 'D', 'o': ',', 'p': 'f', 'q': '^', 'r': '7', 's': '`', 't': 'x', 'u': '_', 'v': '0', 'w': 'M', 'x': 'u', 'y': '.', 'z': 'T', 'A': 'Y', 'B': '>', 'C': '$', 'D': 'j', 'E': 'F', 'F': 'O', 'G': 'I', 'H': 'A', 'I': 'l', 'J': 'P', 'K': 'p', 'L': 'n', 'M': 'c', 'N': 'X', 'O': '!', 'P': 'C', 'Q': '5', 'R': 'k', 'S': 'S', 'T': 'E', 'U': 'm', 'V': 't', 'W': '3', 'X': 'U', 'Y': '}', 'Z': 'H', '!': 'g', '#': '-', '$': 'e', '%': '%', '&': 'o', '(': ';', ')': '~', '*': 'd', '+': 'N', ',': '&', '-': 'z', '.': '(', '/': 'W', ':': 'v', ';': 'h', '<': 'i', '=': '2', '>': 'V', '?': 'R', '@': '@', '[': 'a', ']': 'r', '^': '4', '_': 'Z', '`': '9', '{': '=', '|': ']', '}': '|', '~': 'G', '0': 'J', '1': 'w', '2': '6', '3': '/', '4': 'B', '5': ':', '6': '+', '7': '<', '8': 'b', '9': '?', " ": " ", "\n" : "\n"}
    decoded_file = open('decoded_file.txt', 'w')
    encoded_file = open('encoded_file.txt', 'r')
    reversed_key = {}
    
    #reverse the key
    for item in key:
        temp_item = key[item]
        
        reversed_key[temp_item] = item
        
    #decode the file
    for line in encoded_file:
        decoded_line = ''
        
        for letter in line:
            decoded_line += reversed_key[letter]
            
        decoded_file.write(decoded_line)
        
    #close the files
    decoded_file.close()
    encoded_file.close()
    print('The decrypted encoded_file.txt to decoded_file.txt')
def unique_words():
    #accepts arguments
    #it uses text file text.txt
    #it display a list of all unique words in the file
    
    #open the file
    file = open('text.txt', 'r')
    #begin the set
    unique = set([])
    
    
    #begin the loop
    for line in file:
        #this will iterate over the word not the line
        for word in line.split(' '):
            while word not in unique:
                unique.add(word)
                
    #itterate over the set to display unique words nicely
    print('The following words are unique in this text file')
    for unique_word in unique:
        print(unique_word)
    

def world_series():
    #world series recieves no arguments
    #it counts the number of wins per team in each year
    #then it tallies them up
    #and asks the user for the year and it will say the year they won
    #and how many times they've one
    
    #initialize variables
    STARTING_YEAR = 1903
    ENDING_YEAR = 2008
    year_counter = STARTING_YEAR
    selected_team = "none"
    winners = dict()
    file = open("WorldSeries.txt", "r")
    bad = True
    
    
    #read the file to create
    for line in file:
        #rstrip the line
        line = line.rstrip("\n")
        #make sure the world series was played that year
        if "World Series Not Played in" not in line:
            #check if it is already in the dictionary, if so add 1
            if line in winners:
                wins = winners[line]
                wins += 1
                winners[line] = wins
            #if not, set the wins to 1
            else:
                winners[line] = 1
    
    #while user inputs a bad input
    while bad == True:
        try:
            #ask for input
            year = int(input(f"Enter a year to find the winner of (YEARS {STARTING_YEAR} TO {ENDING_YEAR} ARE VALID): "))
            
            #validate it
            if year > ENDING_YEAR or year < STARTING_YEAR:
                print(f"Enter a team between valid years of {STARTING_YEAR} and {ENDING_YEAR}.")
            else:
                #set it to be a good input
                bad = False
        except:
            #output error
            print("Enter only numbers.")
            
            
    #close and reopen file to start reading from beginning
    file.close()
    file = open("WorldSeries.txt", "r")
    
    #read each line and check if it is the right year
    for line in file:
        if int(year_counter) == int(year):
            #print it was not played that year
            if "World Series Not Played in" in line:
                line = line.rstrip("\n")
                print(f"The {line}.")
                break
            
            #print the team that won and their win times.
            else:
                selected_team = line.rstrip("\n")
                times_team_won = winners[selected_team]
        
                print(f"The team {selected_team}, has won {times_team_won} time starting in {STARTING_YEAR}, ending in {ENDING_YEAR}.")
                break
        else:
            #add to year counter to keep track of year if it was not correct.
            year_counter += 1

def card_dealer_main(): #program 9-1
    #card dealer main accepts no arguments
    #it calls create_deck to generate a deck of cards
    #and takes input from the user for the number of cards to deal
    #it then calls deal_cards to deal the number of cards to the user
    
    print("\nNew Game.")
    deck = create_deck()
    deal_cards(deck)
    
def create_deck():
    #create deck accepts no arguments
    #it geneerates a dictionary with the name of the card a the key
    #and the point value of the card as the value
    #and returns the dictionary of cards
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

def deal_cards(deck):
    #deal cards accepts deck as a dictionary and number as an integer
    #it verifies number isn't greater than the deck size
    #if it is, it sets the number to the length to the deck size to not
    #exceed the maximum index
    #it randomly selects and removes a key/value from the deck
    #it prints the card and calculates the value of the players hands
    #it prints out each players hand as they move and their total points
    
    #set player hands to 0
    plr_1_scor = 0
    plr_2_scor = 0
    
    go = True
    #deal them a card
    try:
        while go == True:
            #pull player 1 cards first
            
             #get 2 random card for player 1 and add to score
            for num in range(2):
                rand_card = random.choice(list(deck))
                value = deck.pop(rand_card)
                if "Ace" in rand_card:
                    if plr_1_scor + 11 > 21:
                        value = 1
                    else:
                        value = 11
                plr_1_scor += int(value)
            
            #get 2 random cards for player 2 and add to score
            for num in range(2):
                rand_card = random.choice(list(deck))
                value = deck.pop(rand_card)
                
                #check if it is an ace and if so lower score 
                if "Ace" in rand_card:
                    if plr_2_scor + 11 > 21:
                        value = 1
                    else:
                        value = 11
                plr_2_scor += int(value)
            
            #check if anyone lost or it was a draw off the bat
            if plr_1_scor > 21 and plr_2_scor > 21:
                print("It's a draw! Both players tied off the bat.")
            elif plr_1_scor > 21:
                print("Player 1 lost off the bat.")
            elif plr_2_scor > 21:
                print("Player 2 lost off the bat.")

            #check if their hand is 21 or greater and print who won
            while plr_1_scor < 21 or plr_2_scor < 21:
                #get player 1 another card
                rand_card = random.choice(list(deck))
                value = deck.pop(rand_card)
                if "Ace" in rand_card:
                    if plr_1_scor + 11 > 21:
                        value = 1
                    else:
                        value = 11
                plr_1_scor += int(value)
                
                #check if player 1 wins that
                if plr_1_scor == 21:
                    print(f"Player 1 wins! Their deck exactly hit 21. Player 2's score was {plr_2_scor}.")
                    plr_1_scor = 0
                    plr_2_scor = 0
                    break
                elif plr_1_scor > 21:
                    print(f"Player 2 wins! Player 1's score exceeded 21. Their score was {plr_1_scor}.")
                    plr_1_scor = 0
                    plr_2_scor = 0
                    break
                
                #get player another card
                rand_card = random.choice(list(deck))
                value = deck.pop(rand_card)
                if "Ace" in rand_card:
                    if plr_2_scor + 11 > 21:
                        value = 1
                    else:
                        value = 11
                plr_2_scor += int(value)
        
                #check if player 2 wins that
                if plr_2_scor == 21:
                    print(f"Player 2 wins! Their deck hit exactly 21. Player 1's score was {plr_1_score}.")
                    plr_1_scor = 0
                    plr_2_scor = 0
                    break
                elif plr_2_scor > 21:
                    print(f"Player 1 wins! Player 2's score exceeded 21. Their score was {plr_2_scor}.")
                    plr_1_scor = 0
                    plr_2_scor = 0
                    break
    except Exception as err:
        print("Deck ran out of cards!")
 
            
            
        
                
            
            

menu()
