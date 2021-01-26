"""
Mykyta S.
functions.py
Contains all the "Functions that return values" exercises
"""


def fahrenheit_to_celsius(f_degrees):
    """Coverts degrees Fahrenheit to Celsius"""
    return (f_degrees - 32) / 1.8


def celsius_to_fahrenheit(c_degrees):
    """Converts degrees Celsius to Fahrenheit"""
    return c_degrees * 1.8 + 32


def km_to_miles(km):
    """Converts kilometers to miles"""
    return km / 1.61


def miles_to_km(miles):
    """Converts miles to kilometers"""
    return miles * 1.61


def zodiac(birth_year):
    """Returns the zodiac sign for a given year"""
    z = birth_year % 12
    signs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit",
             "Dragon", "Snake", "Horse", "Sheep"]
    return signs[z]


def ln_2(n_terms):
    """Calculates the natural log of two using its taylor series"""
    sum = 1
    for i in range(n_terms):
        sum += 1 / (i + 2) * (1 if i % 2 else -1)
    return sum


def pi_over_4(n_terms):
    """Calculates the value of pi/4 using the Leibniz formula"""
    sum = 1
    for i in range(n_terms):
        sum += 1 / (i * 2 + 3) * (1 if i % 2 else -1)
    return sum


def square_num(n):
    """Squares the number using a staircase formula (my own function)"""
    sum = 0
    for i in range(n):
        sum += (i * 2 + 1)
    return sum


def gravity_force(mass1, mass2, distance):
    """Calculates the gravitational pull from one object to another"""
    G = 6.674E-11
    return G * mass1 * mass2 / (distance ** 2)
