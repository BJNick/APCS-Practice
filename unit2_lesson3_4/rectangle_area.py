"""
Mykyta S.
rectangle_area.py
Calculate the area, perimeter and a diagonal of a rectangle
"""

import math

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = length * 2 + width * 2
diagonal = math.sqrt(length ** 2 + width ** 2)

if (length == width):
    print("Your rectangle is a square!")

print("Area = " + str(area), "perimeter = " + str(perimeter),
      "diagonal = " + str(diagonal), sep=", ")


