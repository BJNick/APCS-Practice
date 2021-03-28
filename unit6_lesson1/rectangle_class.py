"""
Mykyta S.
rectangle_class.py
Contains Rectangle class exercise
"""

import turtle  # Allows us to use turtles

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def print_point(pt):
        print("({0}, {1})".format(pt.x, pt.y))

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

    def midpoint(p1, p2):
        """ Return the midpoint of points p1 and p2 """
        mx = (p1.x + p2.x) / 2
        my = (p1.y + p2.y) / 2
        return Point(mx, my)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def slope_from_origin(self):
        # y over x
        return self.y / self.x

class Rectangle:
    """A class to manufacture rectangle objects"""

    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width w, height h"""
        self.corner = posn  # bottom left corner of rectangle
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def rectangle_area(self):
        """Find the area of the Rectangle object of width and height"""
        return self.width * self.height

    def rectangle_perimeter(self):
        """Find the perimeter of the Rectangle object of width and height"""
        return self.width * 2 + self.height * 2


def rectangle_collision(rect1, rect2):
    """Determine if two Rectangle objects collide
    rect1 is a Rectangle object
    rect2 is a Rectangle object
    """
    if rect1.corner.x > rect2.corner.x + rect2.width or \
            rect2.corner.x > rect1.corner.x + rect1.width:
        return False

    if rect1.corner.y > rect2.corner.y + rect2.height or \
            rect2.corner.y > rect1.corner.x + rect1.height:
        return False

    return True


def plot_rectangle(rect, ttl):
    """
    plots a class rect with turtle ttl
    Corrected! Starts at Bottom left corner
    """
    ttl.up()
    ttl.setheading(0)  # i forgot to put this in!
    ttl.goto(rect.corner.x, rect.corner.y)
    ttl.down()
    ttl.forward(rect.width)
    ttl.left(90)
    ttl.forward(rect.height)  # Complete the second side of a rectangle
    ttl.left(90)
    ttl.forward(rect.width)
    ttl.left(90)
    ttl.forward(rect.height)
    ttl.up()


if __name__ == "__main__":
    wn = turtle.Screen()  # Creates a playground for turtles
    alex = turtle.Turtle()  # Create a turtle, assign to alex

    box = Rectangle(Point(200, 200), 100, 150)
    plot_rectangle(box, alex)

    bomb = Rectangle(Point(200, 205), 50, 10)  # In my video game
    plot_rectangle(bomb, alex)

    alex.goto(0, 0)  # return to the origin (centre of the turtle window)
    print("box: ", box)
    print("box area: ", box.rectangle_area())
    print("box perimeter: ", box.rectangle_perimeter())

    print("bomb: ", bomb)

    # test for collision when you've coded the function
    collision = rectangle_collision(box, bomb)
    print(collision)

    # second test - no collision
    box = Rectangle(Point(100, 100), 100, 50)
    alex.color('red')
    plot_rectangle(box, alex)
    bomb = Rectangle(Point(20, 25), 50, 10)  # In my video game
    plot_rectangle(bomb, alex)
    collision = rectangle_collision(box, bomb)
    print("box: ", box)
    print("box area: ", box.rectangle_area())
    print("box perimeter: ", box.rectangle_perimeter())
    print(collision)

    wn.mainloop()
