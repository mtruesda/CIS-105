#
# This program will generate an estonian flag using turtle graphics
# 2/13/2020
# @Myron Truesdale
# Problem 5
#

# necessary import
import turtle

# Introductory Piece
print('Problem 5 - Turtle Graphics Drawing - Estonian Flag')
print('This program will generate an Estonian flag using turtle graphics')

# turtle stuff

# keep bg white
turtle.bgcolor('white')

# movements
turtle.showturtle()
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)

# fillings - blue
turtle.penup()
turtle.forward(150)
turtle.setheading(180)
turtle.pendown()
turtle.fillcolor('light blue')
turtle.begin_fill()
turtle.forward(300)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(50)
turtle.end_fill()
turtle.setheading(270)

# fillings - black
turtle.forward(50)
turtle.right(90)
turtle.fillcolor('black')
turtle.begin_fill()
turtle.forward(300)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(50)
turtle.end_fill()

turtle.hideturtle()

#did not paint white because I didn't think it was required, the background
#is intentionally set to white.

