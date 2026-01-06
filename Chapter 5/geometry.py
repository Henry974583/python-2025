#this program allows the user to choose various
#geometry calculations from a menu. this program
#imports the circle and rectangle modules
import cirle
import rectangle

#costans for the menu choices
area_circle_choice = 1
circumference_choice = 2
area_rectangle_choice = 3
perimeter_rectangle_choice = 4
quit_choice = 5

#the main function
def main():
    #the choice variable conrols the loop
    #and holds the user menu choice
    choice = 0
    display_menu()
    
        #display the menu
        
    
    #get the user choice
    choice = int(input("Enter your choice: "))
    
    #perform the selected action
    if choice == area_circle_choice:
        radius = float(input("Enter the circle's radius: "))
        print('The area is', cirle.area(radius))
    elif choice == circumference_choice:
        radius = float(input('Enter the circles radius: '))
        print('The circumference is', \
              cirle.circumference(radius))
    elif choice == area_rectangle_choice:
        width = float(input('Enter the rectanlges width: '))
        length = float(input('Enter the rectangles length: '))
        print('The area is', rectangle.area(width, length))
    elif choice == perimeter_rectangle_choice:
        width = float(input('Enter the rectangles width: '))
        length = float(input('Enter the rectangels length: '))
        print('The perimeter is', \
              rectangle.perimeter(width, length))
    elif choice == quit_choice:
        print('Exiting the program...')
    else:
        print('Error invalid selection.')

#the display_menu function displays a menu
def display_menu():
    print('        MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) perimeter of a rectangle')
    print('5) quit')
    

    