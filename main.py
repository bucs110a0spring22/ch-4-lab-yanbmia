import turtle

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

import math

#y = (math.radians(270))
#print(y)

wn = turtle.Screen()
fred = turtle.Turtle()
#fred.goto(50,60)
#fred.goto(-25,-30)
#fred.goto(-45,50)
#fred.goto(65,-75)
#fred.clear()

def setupWindow(mywindow=None):
  turtle.setworldcoordinates(-5,-5,5,5)
  turtle.Screen().bgcolor("lavender")

setupWindow()

def setupAxis(myturtle=None):
  fred.goto(0,-5)
  fred.goto(0,5)
  fred.penup()
  fred.goto(-10,0)
  fred.pendown()
  fred.goto(10,0)

setupAxis()

angles = range(-360,361)

def drawSineCurve():
  for i in angles:
    y_val = math.sin(math.radians(i))
    x_val = math.radians(i)
    fred.goto(x_val,y_val)
  fred.pu()
    
drawSineCurve()


def drawCosineCurve(myturtle=None):
  for i in angles:
    y_val = math.cos(math.radians(i))
    x_val = math.radians(i)
    fred.goto(x_val,y_val)
    fred.pd()
  fred.pu()

drawCosineCurve()

def drawTangentCurve(myturtle=None):
  for i in angles:
    y_val = math.tan(math.radians(i))
    if y_val > 5:
      y_val = 5
      fred.pu()
    if y_val < -5:
      y_val = -5
      fred.pu()
    x_val = math.radians(i)
    fred.goto(x_val,y_val)
    fred.pd()
  fred.pu()

drawTangentCurve()


wn.exitonclick()





##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
