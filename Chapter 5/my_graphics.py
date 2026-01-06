import turtle
import geometry
import cirle
import rectangle
def square(x, y, width, color): #program 5-29 
    turtle.penup() 
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

def circle(x, y, radius, color):
    turtle.penup() #raise the pen
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
def line(startX, startY, endX, endY, color):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX, endY)
    
    #constants
def rectangle(x, y, topwidth, sidewidth, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(topwidth)
    turtle.left(90)
    turtle.forward(sidewidth)
    turtle.left(90)
    turtle.forward(topwidth)
    turtle.left(90)
    turtle.forward(sidewidth)
    
    turtle.end_fill()