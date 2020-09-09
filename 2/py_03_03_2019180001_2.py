import turtle

count = 0
i = 1


while (i <= 7):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0, 100 + count)
    count = count + 100
    i = i + 1

turtle.goto(0,0)
turtle.setheading(90)

j = 1
count2 = 0

while (j <= 6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(100 + count2, 0)
    count2 = count2 + 100
    j = j + 1

