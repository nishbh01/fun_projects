from tkinter import CENTER, LEFT, RIGHT
from turtle import *

youryear = int(input("How old are you? "))

yourlife = int(input("How many years do you expect to live? "))


remaining = yourlife - youryear


import turtle
turtle.setup(600,700)
turtle.bgcolor("white")
life = turtle.Turtle()
life.up()
life.goto(100, 300)
life.down()
life.write("Red: Years you lived\nGreen: Years yet to live", align = RIGHT, font=('Arial', 15, 'bold'))
 
# draws a rectangle of a specified length, breadth, fill, and boder color.
def rectangle(life,x,y,length,breadth,size,pcolor,fill):
  life.fillcolor(fill)
  life.pencolor(pcolor)
  life.pensize(size)
  life.up()
  life.setheading(0)
  life.goto(x,y)
  life.down()
  life.begin_fill()
  # drawing rectangle as specified
  for i in range(2):
    life.forward(length)
    life.right(90)
    life.forward(breadth)
    life.right(90)
  life.end_fill()
 

total = 0  # keeping tracks of your years as the # of rect. drawn
for x in range(youryear):
    for y in range(6):
        total += 1  
        if total > yourlife:  # when the number of rectangle reaches your age, it breaks.
            break
        else:
            if total <= youryear: # lived years are drawn as red rect.
                rectangle(life,-200+x*20,y*20,20,20,5,"white","red")
            else: # unlived years are drawn as green rect
                rectangle(life,-200+x*20,y*20,20,20,5,"white","green")
life.hideturtle()
turtle.done()
