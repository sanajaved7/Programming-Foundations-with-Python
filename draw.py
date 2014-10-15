import turtle
def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    brad = turtle.Turtle()
    brad.shape ("turtle")
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)
    exit.window()

draw_art()

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
