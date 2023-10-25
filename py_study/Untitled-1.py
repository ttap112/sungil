from turtle import *
import time

def startSetup():
    penup()
    left(90)
    forward(200)
    left(90)
    forward(300)
    left(180)
    pendown()


def nameOne():
    forward(50)
    right(90)
    forward(50)

    penup()
    forward(10)
    pendown()

    #ㅣ
    left(90)
    forward(50)
    left(180)
    forward(100)
    left(180)
    forward(50)
    right(90)
    forward(50)
    right(180)
    forward(50)
    right(90)
    forward(50)

    penup()
    forward(20)
    pendown()

    #ㄴ
    left(90)
    forward(50)
    left(180)
    forward(100)

    penup()

    right(90)
    forward(50)

    pendown()

    left(90)
    forward(50)
    left(90)
    forward(100)
    penup()

def nameTwo():
    left(90)
    forward(165)
    pendown()

    right(90)
    forward(50)
    right(180)
    forward(50)
    left(90)
    forward(25)
    left(90)
    forward(50)
    left(180)
    forward(25)
    left(90)
    forward(25)
    right(90)
    forward(25)
    right(180)
    forward(50)
    right(180)

    penup()
    forward(37)
    left(90)
    forward(30)
    pendown()

    circle(20)

    penup()
    left(90)
    forward(100)
    left(90)
    forward(50)
    pendown()

    circle(20)

    penup()
    right(90)
    forward(50)
    pendown()

    right(90)
    forward(50)
    right(180)
    forward(100)
    right(180)

    forward(25)
    right(90)
    forward(25)
    right(180)
    forward(25)
    right(90)
    forward(30)
    right(90)
    forward(25)
    right(180)
    forward(25)
    right(90)

    penup()
    forward(90)
    pendown()

    circle(20)

startSetup()
time.sleep(0.1)

nameOne()
time.sleep(0.1)

nameTwo()





done()