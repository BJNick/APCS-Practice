"""
Mykyta S.
turtle_fractals.py
Draws various fractals with turtle using recursion
"""
import math
import turtle


def draw_koch_triangle(t, order, size):
    """Draws a Koch triangle"""
    if order == 0:
        t.pendown()
        t.forward(size)
        t.penup()
        return

    draw_koch_triangle(t, order-1, size/3)
    t.left(60)
    draw_koch_triangle(t, order-1, size/3)
    t.right(120)
    draw_koch_triangle(t, order-1, size/3)
    t.left(60)
    draw_koch_triangle(t, order-1, size/3)


def draw_cesaro_torn_line(t, order, size):
    """Draws a Cesaro torn line fractal"""
    if order == 0:
        t.pendown()
        t.forward(size)
        t.penup()
        return

    side_length = size * (1 - math.sin(5)) / 4

    draw_cesaro_torn_line(t, order-1, side_length)
    t.right(85)
    draw_cesaro_torn_line(t, order-1, size / 2)
    t.left(170)
    draw_cesaro_torn_line(t, order-1, size / 2)
    t.right(85)
    draw_cesaro_torn_line(t, order-1, side_length)


def draw_sierpinski_triangle(t, order, side_length, color_change_depth=-1):

    if (order == 0):
        t.pendown()
        for i in range(3):
            t.forward(side_length)
            t.left(120)
        t.penup()
        return

    if color_change_depth == 0:
        t.color('red')
    draw_sierpinski_triangle(t, order-1, side_length/2, color_change_depth-1)
    if color_change_depth == 0:
        t.color('blue')
    t.forward(side_length/2)
    draw_sierpinski_triangle(t, order-1, side_length/2, color_change_depth-1)
    if color_change_depth == 0:
        t.color('magenta')
    t.left(120)
    t.forward(side_length/2)
    t.right(120)
    draw_sierpinski_triangle(t, order-1, side_length/2, color_change_depth-1)
    t.right(120)
    t.forward(side_length/2)
    t.left(120)




if __name__ == "__main__":
    window = turtle.Screen()
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    t.penup()
    t.backward(300)
    t.goto(-300,-300)

    draw_sierpinski_triangle(t, 5, 600, 3)

    window.exitonclick()
