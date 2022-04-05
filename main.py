import turtle
import math

dart = turtle.Turtle()

windowColor = input("Which color for the background? ")
turtleShape = input("Choose a pointer shape (arrow, turtle, circle): ")
graphUnits = input("Units on the graph? (Type Yes or No): ")


def setupWindow(mywindow=None):
  turtle.setworldcoordinates(-5,-5,5,5)
  turtle.Screen().bgcolor(windowColor)
  dart.shape(turtleShape)

def setupUnits():
  fred = turtle.Turtle()
  fred.penup()
  units = ["-2\u03C0", "-3\u03C0/2","-\u03C0", "-\u03C0/2", "0", "\u03C0/2", "\u03C0", "3\u03C0/2", "2\u03C0"]
  count = 0
  x_val = math.radians(-360)
  for i in range(9):
    fred.goto(x_val, -0.75)
    fred.write(units[count])
    count = count + 1
    x_val = x_val + math.radians(90)
  fred.hideturtle()

def setupAxis(myturtle=None):
  dart.goto(0,-5)
  dart.goto(0,5)
  dart.penup()
  dart.goto(-10,0)
  dart.pendown()
  dart.goto(10,0)
  if graphUnits == "Yes":
    setupUnits()
    
angles = range(-360,361)

def drawSineCurve(myturtle=None):
  pointsList = []
  for i in angles:
    y_val = math.sin(math.radians(i))
    x_val = math.radians(i)
    sin_point = (x_val,y_val)
    dart.goto(sin_point)
    pointsList.append(sin_point)
  dart.pu()
  return pointsList
  
def drawCosineCurve(myturtle=None):
  for i in angles:
    y_val = math.cos(math.radians(i))
    x_val = math.radians(i)
    dart.goto(x_val,y_val)
    dart.pd()
  dart.pu()

def drawTangentCurve(myturtle=None):
  for i in angles:
    y_val = math.tan(math.radians(i))
    if y_val > 5:
      y_val = 5
      dart.pu()
    if y_val < -5:
      y_val = -5
      dart.pu()
    x_val = math.radians(i)
    dart.goto(x_val,y_val)
    dart.pd()
  dart.pu()

def drawInverseSine(myturtle=None):
  dart.color("lawngreen")
  for i in angles:
    y_val = math.sin(math.radians(i))
    if y_val == 0:
      y_val = 5
      dart.pu()
    inverseY = 1/y_val
    if inverseY > 5:
      inverseY = 5
      dart.pu()
    if inverseY < -5:
      inverseY = -5
      dart.pu()
    x_val = math.radians(i)
    dart.goto(x_val,inverseY)
    dart.pd()
  dart.pu()

value = input("Type a Coordinate [Format (x,y)]: ")

def plotPoint(value):
  albert = turtle.Turtle()
  albert.color("fuchsia")
  albert.shape("circle")
  albert.shapesize(0.5,0.5,0.5)
  albert.penup()
  x_val = int(value[1])
  y_val = int(value[3])
  point = (x_val,y_val)
  albert.goto(point)
  return(point)
  
def intersectionGraph():
  if plotPoint(value) in drawSineCurve():
    print("Point is on the sine graph.")
    return(True)
  else:
    print("Point is not on the sine graph.")
    return(False)


def main():
    wn = turtle.Screen()
    wn.tracer(5)
    dart.speed(0)
    drawSineCurve(dart)

    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
  
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
  
    drawInverseSine(dart)
    plotPoint(value)
    intersectionGraph()
    wn.exitonclick()
main()

