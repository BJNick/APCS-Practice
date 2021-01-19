"""
Mykyta S.
day_of_week.py
Prints the next day after a day
"""

days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday",
                "saturday", "sunday"]

today = input("Enter day: ").lower()
next_day = None

for i, day in enumerate(days_of_week):
    if today == day:
        next_day = days_of_week[(i+1) % 7]
        break

if not next_day:
    print("This day of the week does not exist.")
else:
    print(next_day.capitalize(), "goes next.")


