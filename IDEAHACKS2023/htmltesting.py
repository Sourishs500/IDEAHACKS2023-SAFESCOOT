#!/usr/bin/python3

# Run as: create-html-table.py {input-file-name}
# The script requires 1 argument: the input file name.
# It expects a comma-separated input file to parse into an html table,
# and assumes that the column headers are located in the first row.

import sys
import html
import random
import numpy as np
from Player import Player

usersAmount = 5

#filein = open(sys.argv[1], "r")
filein = open(r"create-html-table.py", "w+")
#filein.write()
p1 = Player("Kevin", 99)

names = ["Sourish", "Arsh", "Christine", "Adrian"]
people = []
scores = []

for i in range(usersAmount - 1):
    people.append(Player(names[i], random.randint(0,100)))
    scores.append(people[i].getScore())

allPeople = {"Kevin" : p1.getScore()}
for i in range(usersAmount ):
    allPeople.update({scores[i] : people[i]})

scores.sort(reverse = True)


filein.write("Rank,Name,AverageSafetyScore\n")
filein.write(str(1) + "," + p1.getName() + "," + str(p1.getScore()) + "\n") 
for i in range(usersAmount):
    filein.write(str(i + 2) + "," + str(allPeople[scores[i]].getName()) + "," + str(scores[i]) + "\n")

fileout = open("html-table.html", "w")
data = filein.readlines()


table = "<table>\n"

# Create the table's column headers
header = data[0].split(",")
table += "  <tr>\n"
for column in header:
    table += "    <th>{0}</th>\n".format(column.strip())
table += "  </tr>\n"

# Create the table's row data
for line in data[1:]:
    row = line.split(",")
    table += "  <tr>\n"
    for column in row:
        table += "    <td>{0}</td>\n".format(column.strip())
    table += "  </tr>\n"

table += "</table>"

fileout.writelines(table)
fileout.close()
filein.close()