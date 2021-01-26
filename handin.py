"""
Mykyta S.
handin.py
Generates a letter to Mr. Ruo
"""

import klembord # Copy/paste
import datetime # Get hour
from os import listdir # List all entities in a directory
from os.path import isfile, join # Check for files
import importlib.util # Get docstring
import sys # Console arguments

klembord.init()

link_start = "https://github.com/BJNick/APCS-Practice/tree/master/"
raw_link_start = "https://raw.githubusercontent.com/BJNick/APCS-Practice/master/"


onlyfolders = [f for f in listdir("./") if (not isfile(join("./", f)) and
    f.startswith("unit"))]
onlyfolders.sort(key=lambda f: int(f.split("_")[0].replace("unit", "")) * 10
                               + int(f.split("_")[-1].replace("lesson", "")))
print(onlyfolders)

if (len(sys.argv) > 1):
    unit = sys.argv[1]
else:
    unit = input("Enter folder: ")

if (unit == "latest"):
    unit = onlyfolders[-1]


if (unit == "latest hw"):
    unit = onlyfolders[-1]+"/hw"

onlyfiles = [f for f in listdir(unit) if isfile(join(unit, f))]
onlyfiles.sort(key=lambda f: ("0" if f.endswith(".py") else "") + f)
print(onlyfiles)

if (len(sys.argv) > 2):
    files = sys.argv[2]
else:
    files = input("Enter files: ")

if files == "all":
    files = onlyfiles
else:
    files = files.split(",")

lower_first = lambda test_str: test_str[:1].lower() + \
               test_str[1:] if test_str else ''

for i, f in enumerate(files):
    f = f.strip()
    explanation = "- a supplementary file"
    if (f.endswith(".py")):
        python_module = importlib.import_module(unit.replace("/", ".")+"."+f.replace(".py", ""))
        explanation = python_module.__doc__.splitlines()[3].strip()
    files[i] = '<li><a href="' + link_start + unit + "/" + f + '">' + f + '</a>  ' \
        + lower_first(explanation) + '</li>'
    if f.endswith(".png") or f.endswith(".jpg"):
        files[i] = files[i] + '<img style="max-width: 75%; max-height: 75%; border: 1px solid; margin: auto;" src="' + raw_link_start + unit + "/" + f +'" alt="' + f + '">'



greeting = "Good morning" if datetime.datetime.now().hour < 12 else "Good afternoon" if datetime.datetime.now().hour < 17 else "Good evening"

pretty_unit = unit.split("les")
pretty_unit = pretty_unit[0].replace("unit", "Unit ").replace("_","") + " " + pretty_unit[1].replace("_", "-").replace("son", "Lessons ").replace("/hw", " homework")

email = greeting + " Mr. Ruo,<br><br>I have completed " + pretty_unit + ". Here are the files:<br>"

email = email + '<ul style="padding-left: 20px;">'

for f in files:
    email = email + f

email = email + '</ul>'

email = email + "<br>Mykyta S."

email = email + "<br><br>P.S. This entire email was automatically generated with "\
                '<a href="' + link_start + "handin.py" + '">' + "handin.py" + '</a>'

print()

print(email)

klembord.set_with_rich_text("", email)
