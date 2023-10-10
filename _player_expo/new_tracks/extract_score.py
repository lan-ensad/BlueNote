import re

file = open("t03.txt", 'r')
extract_number = "\\d+"
score = []

for line in file:
   x = line.split(", ")
   score.append(x)

print(score)