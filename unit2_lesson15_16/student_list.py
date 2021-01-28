"""
Mykyta S.
student_list.py
Extracts student information from a list
"""

if __name__ == "__main__":
    students = [
        ["Jen", 17, "brown"],
        ["Julius", 18, "dark"],
        ["Mullius", 16, "blonde"],
        ["Tiberius", 17, "dark"],
        ["Maximus", 16, "black"]
    ]

    for student in students:
        print("%s is %d years old and has %s hair." % tuple(student))