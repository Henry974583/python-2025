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
            world_series_winners()
        elif choice == 5:
            blackjack()
            
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
    

def world_series_winners():
    #it accepts no arguments
    #it open file WorldSeriesWinners.txt
    #it ask the user for a team name to search for
    #and prints how many times they won that year
    
    #open the file
    file = open('WorldSeries.txt', 'r')
    
    #input to ask for team and what year to search
    search = str(input('Enter a team to search for: '))
    year = int(input('Enter the year to search for: '))
    #if statement to make sure the year is valid
    if year == 1904 or year == 1994:
             print('no world series in year', year)
             print('Try again')
    else:
        #counter to make the program know what year it was on
        key = {}
        final_team = ''
        #begin for loop
        for line in file:
            
            #split the name
            names = line.split(' ')
            
        
            for team in names:
                
            
            
def blackjack():
    #it accepts no arguments
    #and calls other functions to run a game of black jack
    pass
menu()
