"""
Mykyta S.
turtle_sample.py
Implements various turtle challenges
"""

import turtle


def draw_star(t : turtle.Turtle, size):
    t.backward(size / 2)
    t.pendown()
    for side in range(5):
        t.forward(size)
        t.right(180-36)
    t.penup()
    t.forward(size / 2)


def draw_ch1(t : turtle.Turtle, size):
    t.pendown()
    for move in range(4):
        for side in range(4):
            t.forward(size / 2 * (1 if side % 2 else 0.4))
            t.right(90)
        t.right(90)
    t.penup()


def draw_ch2(t : turtle.Turtle, size):
    t.pendown()
    for triangle in range(6):
        for side in range(3):
            t.forward(size / 2)
            t.left(360/3)
        t.left(60)
    t.penup()


def draw_ch3(t : turtle.Turtle, size):
    t.pendown()
    for shape in range(4):
        for piece in range(12):
            t.forward(size / 6)
            t.left(90 if piece % 3 == 0 else -90)
        t.left(90)
    t.penup()


def draw_ch4(t : turtle.Turtle, size):
    size = size / 2
    t.pendown()
    t.right(90)
    for square in range(5):
        t.backward(size / 2)
        for side in range(4):
            t.forward(size)
            t.left(90)
        t.forward(size / 2)
        t.left(360/5)
    t.left(90)
    t.penup()


def draw_ch5(t : turtle.Turtle, size):
    width = size / 10
    turn = 90
    Lshape = [size / 4, size / 2, width, size / 2 - width, size / 4 - width, width]
    t.pendown()
    for L in range(8):
        turn = -turn
        for i, side in enumerate(Lshape):
            t.forward(side)
            t.left(turn if i != 3 else -turn)
        if L % 2:
            t.left(90)
    t.penup()



def draw_ch6(t : turtle.Turtle, size):
    t.pendown()
    for hexagon in range(8):
        for side in range(6):
            t.forward(size / 4)
            t.left(360/6)
        t.left(360 * 3 / 8)
    t.penup()


def draw_ch7(t : turtle.Turtle, size):
    t.pendown()
    for hourglass in range(5):
        for side in range(3):
            t.forward(size / 2)
            t.right(360 / 3)
        t.right(180)
        for side in range(3):
            t.forward(size / 2)
            t.right(360 / 3)
        t.right(360 / 5)
    t.right(180)
    t.penup()


def draw_ch8(t : turtle.Turtle, size):
    t.pendown()
    for hexagon in range(12):
        for side in range(6):
            t.forward(size / 4)
            t.right(360 / 6)
        t.right(360 / 12)
    t.penup()


window = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.shape("turtle")
t.speed(0)

size = 100
t.goto(-size*2.5, 200)

draw_ch1(t, size)
t.forward(size * 1.5)
draw_ch2(t, size)
t.forward(size * 1.5)
draw_ch3(t, size)
t.forward(size * 1.5)
draw_ch4(t, size)
t.forward(size * 1.5)

t.goto(-size*2.5, 200 - size * 1.5)

draw_ch5(t, size)
t.forward(size * 1.5)
draw_ch6(t, size)
t.forward(size * 1.5)
draw_ch7(t, size)
t.forward(size * 1.5)
draw_ch8(t, size)
t.forward(size * 1.5)

t.goto(0, 200 - size * 1.5 * 2)
draw_star(t, size)

t.forward(size * 1.5)

window.exitonclick()
