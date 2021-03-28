"""
Mr. Ruo
point_class_example.py
Mr. Ruo's example of a class for a point
"""

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


def distance(p1, p2):
    # p1 and p2 are Point objects
    # sqrt((p1.x - p2.x)^2 + (p1.y - p2.y)^2)
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


if __name__ == "__main__":

    p = Point(1, 1)  # Instantiate an object of type Point
    q = Point(0, 2)  # Make a second point

    print(distance(p, q))
    print(p.slope_from_origin())
    # print('(',p.x,',', p.y,')')
    p.print_point()
    # print('(',q.x,',', q.y,')')
    print(p.distance_from_origin())
    print(p.to_string())
    midpt = Point.midpoint(p, q)
    print(midpt, 'of', str(p), 'and', str(q))
    halfwayp = p.halfway(q)
    print(str(halfwayp), 'halfway point of ', str(p), 'and', str(q))
