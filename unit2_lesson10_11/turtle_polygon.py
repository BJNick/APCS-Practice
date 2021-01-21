"""
Mykyta S.
turtle_polygon.py
Draws a polygon, based on number of sides n
"""

import turtle


def draw_square(my_turtle, size):
    my_turtle.pendown()
    for move in range(4):
        my_turtle.forward(size)
        my_turtle.left(360/4)
    my_turtle.penup()


def draw_pentagon(my_turtle,size):
    my_turtle.pendown()
    for move in range(5):
        my_turtle.forward(size)
        my_turtle.left(360/5)
    my_turtle.penup()


def draw_triangle(my_turtle,size):
    my_turtle.pendown()
    for move in range(3):
        my_turtle.forward(size)
        my_turtle.left(360/3)
    my_turtle.penup()


def draw_hexagon(my_turtle,size):
    my_turtle.pendown()
    for move in range(6):
        my_turtle.forward(size)
        my_turtle.left(360/6)
    my_turtle.penup()


def draw_polygon(my_turtle,size,n):
    my_turtle.pendown()
    for move in range(n):
        my_turtle.forward(size)
        my_turtle.left(360/n)
    my_turtle.penup()


window = turtle.Screen()  # Creates a window for bob so play
bob = turtle.Turtle()  # creates a turtle named bob
bob.speed(5) #speed(0) is fastest
bob.shape("turtle")       # Makes bob look like a turtle

bob.penup()
bob.backward(200)

draw_square(bob,30)
bob.forward(80)
draw_pentagon(bob,30)
bob.forward(80)
draw_triangle(bob, 30)
bob.forward(80)
draw_hexagon(bob, 30)

bob.forward(80)
draw_polygon(bob, 30, 7)

window.exitonclick()
