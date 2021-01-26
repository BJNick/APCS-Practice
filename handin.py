"""
Mykyta S.
handin.py
Generates a letter to Mr. Ruo
"""

import klembord # Copy paste
import datetime # Get hour
from os import listdir # Get all files
from os.path import isfile, join
import importlib.util # Get docstring

klembord.init()

link_start = "https://github.com/BJNick/APCS-Practice/tree/master/"

unit = input("Enter folder: ")

onlyfiles = [f for f in listdir(unit) if isfile(join(unit, f))]
print(onlyfiles)

files = input("Enter files: ")

if files == "all":
    files = onlyfiles
else:
    files = files.split(",")

lower_first = lambda test_str: test_str[:1].lower() + \
               test_str[1:] if test_str else ''

for i, f in enumerate(files):
    f = f.strip()
    python_module = importlib.import_module(unit+"."+f.replace(".py", ""))
    files[i] = '<li><a href="' + link_start + unit + "/" + f + '">' + f + '</a>  ' \
        + lower_first(python_module.__doc__.splitlines()[3].strip()) + ''



greeting = "Good morning" if datetime.datetime.now().hour < 12 else "Good afternoon" if datetime.datetime.now().hour < 17 else "Good evening"

pretty_unit = unit.split("les")
pretty_unit = pretty_unit[0].replace("unit", "Unit ").replace("_","") + " " + pretty_unit[1].replace("_", "-").replace("son", "Lessons ").replace("/hw", " homework")

email = greeting + " Mr. Ruo,<br><br>I have completed " + pretty_unit + ". Here are the files:<br>"


for f in files:
    email = email + f + "<br>"

email = email + "<br>Mykyta S."

email = email + "<br><br>P.S. This entire email was automatically generated with "\
                '<a href="' + link_start + "handin.py" + '">' + "handin.py" + '</a>'

print()

print(email)

klembord.set_with_rich_text("", email)
