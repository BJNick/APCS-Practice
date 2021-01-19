"""
Mykyta S.
rectangle_while_loop.py
Performs rectangle calculations in a while loop.
"""

response = input("Start? (Yes/No) ")

while response.lower() == "yes" or response == "y":
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
    response = input("Continue? (Yes/No) ")