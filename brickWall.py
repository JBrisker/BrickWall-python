#This program draws a brick wall with turtle
import turtle
turtle.speed(0)
turtle.penup()   #pull up pen
turtle.goto(-280, -260) #go to bottom left corner
turtle.pendown()
turtle.bgcolor("green")
turtle.fillcolor("red")
turtle.begin_fill()

rows=10



def drawSquare(sideLen):            #draw a square
    #turtle.setup(620,480)
    for i in range(4):
        turtle.forward(sideLen)
        turtle.right(90)
    turtle.forward(sideLen)
      
def drawRectangle(shortLen):         #draw a rectangle
    for i in range(2):
        turtle.forward(shortLen*2)
        turtle.right(90)
        turtle.forward(shortLen)
        turtle.right(90)
    turtle.forward(shortLen*2)
        
        
def drawRowRec(shortLen,num):       #draw a Row of rectangles for given value
    for j in range(num): 
      drawRectangle(shortLen)

def drawRowSquare(sideLen,num):    #draw row of squares for given value
    for x in range(num):
        drawSquare(sideLen)
        
def rowSquareStart(): #A function for the rows that start/ends with a square and 7 rectangles
    drawRowSquare(30,1)
    drawRowRec(30,7)
    drawRowSquare(30,1)
    
def rowRectangles():  #A row of 8 rectangles
    drawRowRec(30,8)
   
def main():
    for row in range(rows):
        rowRectangles()
        turtle.left(180)
        rowSquareStart()
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)    
    
main()   
turtle.end_fill()
turtle.done()
