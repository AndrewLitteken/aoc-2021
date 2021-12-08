import sys
import copy

data = []

for line in sys.stdin:
  data.append(line.strip("\n"))

grid = []
line_segments = []
max_x = float("-inf")
max_y = float("-inf")
for line in data:
  points = line.split("->")
  start = points[0].split(",")
  end = points[1].split(",")
  line_segments.append(((int(start[0]), int(start[1])), (int(end[0]), int(end[1]))))
  for i in line_segments[-1]:
    if i[0] > max_x:
      max_x = i[0]
    if i[1] > max_y:
      max_y = i[1]

for i in range(max_y+1):
  row = []
  for j in range(max_x+1):
    row.append(0)
  grid.append(row)

grid_copy = copy.deepcopy(grid)

for line in line_segments:
  if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
    continue

  if line[0][0] == line[1][0]:
    start = line[0][1]
    end = line[1][1]
    inc = -1 if start > end else 1
    for i in range(start, end+inc, inc):
      grid_copy[i][line[0][0]] += 1
  else:
    start = line[0][0]
    end = line[1][0]
    inc = -1 if start > end else 1
    for i in range(start, end+inc, inc):
      grid_copy[line[0][1]][i] += 1

num_greater = 0
for i in grid_copy:
  for j in i:
    if j > 1: num_greater += 1
print(num_greater)

greater_than_1 = set()
grid_copy = copy.deepcopy(grid)
for line in line_segments:

  if line[0][0] == line[1][0]:
    start = line[0][1]
    end = line[1][1]
    inc = -1 if start > end else 1
    for i in range(start, end+inc, inc):
      grid_copy[i][line[0][0]] += 1
  elif line[0][1] == line[1][1]:
    start = line[0][0]
    end = line[1][0]
    inc = -1 if start > end else 1
    for i in range(start, end+inc, inc):
      grid_copy[line[0][1]][i] += 1
  else:
    x_start = line[0][0]
    x_end = line[1][0]
    y_start = line[0][1]
    y_end = line[1][1]
    x_inc = -1 if x_start > x_end else 1
    y_inc = -1 if y_start > y_end else 1
    curr_x = x_start
    curr_y = y_start
    while curr_x != x_end + x_inc and curr_y != y_end + y_inc:
      grid_copy[curr_y][curr_x] += 1
      curr_y += y_inc
      curr_x += x_inc

num_greater = 0
for i in grid_copy:
  for j in i:
    if j > 1: num_greater += 1
print(num_greater)