import turtle
#import random

pen1 = turtle.Turtle()
pen2 = turtle.Turtle()
#creating the turtles

myScreen = turtle.Screen()
myScreen.bgcolor("grey")
#creating the screen and its bg colour

pen1.color("black", "black")
#outer and inner colour
pen1.penup()
pen1.setpos(-300,50)
#setting the turtle's position
pen1.speed(5)
#setting turtle speed

pen2.color("black", "dark green")
pen2.penup()
pen2.setpos(-300,-60)
pen2.speed(5)


pen1.pendown()
pen2.pendown()
pen1.begin_fill()
pen2.begin_fill()
#starting to draw now that the turtles are in position
#begin_fill = putting down colour as they move


#####################################
#-------Adding the words--------# 
#####################################


#H
pen1.left(90)
pen1.forward(80)
pen1.back(40)
pen1.right(90)
pen1.forward(35)
pen1.left(90)
pen1.forward(40)
pen1.back(80)
pen1.penup()

