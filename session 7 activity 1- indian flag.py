# programming for Indian Flag
#Import Turtle

import turtle as t


# define function
def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()


# set up the positon of Turtle at (0, -300)

t.up()
t.goto(0,-300)
t.down()
t.goto(0,300)
rectangle("orange")

t.goto(0,200)
t.forward(200)
t.color("blue")
t.circle(-50)
t.setheading(270)
t.forward(50)
t.setheading(0)

# program for line in ashok chakra

for i in range(24):
    t.forward(45)
    t.bk(45)
    t.left(15)
t.setheading(90)
t.forward(50)
t.setheading(0)


t.color("black")
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)




t.goto(0,100)
rectangle("green")




