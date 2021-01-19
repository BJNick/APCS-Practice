"""
Mykyta S.
leap_years.py
Returns whether the entered year is a leap year
"""

def is_a_leap_year(year):
    """Print whether a given year is a leap year"""
    result = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    print(year, "is", "a leap year." if result else "not a leap year.")


entered_year = int(input("Enter year: "))
is_a_leap_year(entered_year)

