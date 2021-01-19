"""
Mykyta S.
area_triangle.py
Returns area of a triangle based on input
"""

base = float(input("Enter base length: "))
height = float(input("Enter height:"))

def triangle_area(base : float, height : float):
    return base * height / 2

print("The area of the triangle is", triangle_area(base, height))



