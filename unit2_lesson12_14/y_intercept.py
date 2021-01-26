"""
Mykyta S.
y_intercept.py
Finds the slope and y-intercept from two points
"""


def slope(pt1, pt2):
    """Finds the slope given two points"""
    x1, y1 = pt1  # unpack tuple
    x2, y2 = pt2  # unpack tuple

    return (y2 - y1) / (x2 - x1)


def y_intercept(pt1, pt2):
    """Finds the y intercept given two points"""
    x1, y1 = pt1
    m = slope(pt1, pt2)
    x0 = -y1 / m + x1
    return x0


if __name__ == '__main__':
    point1 = (6, 2)  # pack a tuple
    point2 = (5, 5)  # pack a tuple

    print("Slope =", slope(point1, point2))
    print("Y-intercept =", y_intercept(point1, point2))
