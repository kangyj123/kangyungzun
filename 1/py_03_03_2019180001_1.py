
import turtle


def ㄱ():
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()

def ㅇ():
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(40)
    turtle.penup()

def ㅏ():
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(200)
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()

def ㅛ():
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(200)
    turtle.backward(150)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()

def ㅈ():
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(200)
    turtle.backward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.penup()

def ㅜ():
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(200)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()

def ㄴ():
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.penup()

turtle.penup()
turtle.goto(-400, 100)

ㄱ()
turtle.goto(-250, 150)
ㅏ()
turtle.goto(-300, -100)
ㅇ()
turtle.goto(-50, 100)
ㅇ()
turtle.goto(-150, 45)
ㅛ()
turtle.goto(-50, -100)
ㅇ()
turtle.goto(50, 150)
ㅈ()
turtle.goto(50, 0)
ㅜ()
turtle.goto(50, -50)
ㄴ()



turtle.exitonclick()
