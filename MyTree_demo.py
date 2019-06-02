import turtle
import random
from turtle import *
from time import sleep

def tree(branchlength , t):
    if branchlength>3 :
        if branchlength >= 8 and branchlength <= 12:
                if random.randint(0,2) == 0:
                    t.color('snow')
                else:
                    t.color('lightcoral')
                t.pensize(branchlength/3)
        if branchlength < 8:
                if random.randint(0,1)==0:
                    t.color('snow')
                else:
                    t.color('lightcoral')
                t.pensize(branchlength/2)
        else:
            t.color('sienna')
            t.pensize(branchlength/10)

        t.forward(branchlength)
        a = 1.5 * random.random()
        b = 1.5 * random.random()
        t.left(20*a)
        tree(branchlength-8*b, t)
        t.right(40*a)
        tree(branchlength-8*b, t)
        t.left(20*a)
        t.up()
        t.backward(branchlength)
        t.down()



def main():
    t= turtle.Turtle()
    myWindows = turtle.Screen()
    #getscreen().tracer(0,5)
    turtle.screensize(bg='wheat')
    t.pensize(10)
    t.pencolor('brown')
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
    tree(60,t)
    myWindows.exitonclick()


main()
