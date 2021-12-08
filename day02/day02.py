import sys

data = []

for line in sys.stdin:
  data.append(line.strip("\n").split(" "))

horiz = 0
vert = 0

for item in data:
  if item[0] == "forward":
    horiz += int(item[1])
  elif item[0] == "down":
    vert += int(item[1])
  if item[0] == "up":
    vert -= int(item[1])

print(horiz*vert)

aim = 0
horiz = 0
vert = 0

for item in data:
  if item[0] == "forward":
    horiz += int(item[1])
    vert += aim * int(item[1])
  elif item[0] == "down":
    aim += int(item[1])
  if item[0] == "up":
    aim -= int(item[1])

print(horiz*vert)