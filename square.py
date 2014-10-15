# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 10:46:44 2014

@author: sanajaved
"""

import turtle
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("green")
    
#Draw Square    
    brad = turtle.Turtle()
    brad.shape ("turtle")
    for i in range (1,37):
        draw_shapes()
        brad.right(10)
        
#Draw Circle        
  #  angie = turtle.Turtle()
   # angie.circle(100)
    #angie.shape("arrow")
    #angie.color("blue")
    
 #Draw Triangle
 #   mark = turtle.Turtle()
 #   mark.color("white")    
 #   lines = 3
 #   count = 0
 #   while (count < lines):
  #      mark.forward(80)
   #     mark.left(120)
    #    count = count + 1
    
    window.exit
    
draw_shapes()