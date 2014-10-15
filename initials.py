# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 22:35:59 2014

@author: sanajaved
"""
import turtle 
turtle.clearscreen()
window = turtle.Screen()
window.bgcolor("blue")
mark = turtle.Turtle()
mark.color("white")    
#s
mark.forward(100)
mark.left(90)
mark.forward(100)
mark.left(90)
mark.forward(100)
mark.right(90)
mark.forward(100)
mark.right(90)
mark.forward(100)
#j
dog = turtle.Turtle()
dog.color("pink")
dog.penup()
dog.forward(120)
dog.pendown()
dog.forward(150)
dog.left(90)
dog.forward(200)
dog.left(90)
dog.forward(100)
dog.backward(150)
