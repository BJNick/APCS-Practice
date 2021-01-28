"""
Mykyta S.
summative_exit_slip.py
Separates my first and last name from a string, then prints the latter
"""

if __name__ == '__main__':
    full_name = "Mykyta Shvets"
    at_space = full_name.find(" ")
    last_name = full_name[at_space+1:]
    print(last_name)