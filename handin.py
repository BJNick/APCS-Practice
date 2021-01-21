"""
Mykyta S.
handin.py
Generates a letter to Mr. Ruo
"""

import klembord
import datetime
from os import listdir
from os.path import isfile, join


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

for i, f in enumerate(files):
    f = f.strip()
    files[i] = '<a href="' + link_start + unit + "/" + f + '">' + f + '</a>'

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
