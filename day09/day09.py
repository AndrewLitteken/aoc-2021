import sys
import copy
from collections import defaultdict

data = []

for line in sys.stdin:
  row = []
  for c in line.strip("\n"):
    row.append(int(c))
  data.append(row)

low_point_sum = 0
low_points = []
for i in range(len(data)):
  for j in range(len(data[i])):

    collected = []
    if j != len(data[i]) - 1:
      collected.append(data[i][j+1])
    if j != 0:
      collected.append(data[i][j-1])

    if i != len(data) - 1:
      collected.append(data[i+1][j])
    if i != 0:
      collected.append(data[i-1][j])

    all_greater = True
    for k in collected:
      if k <= data[i][j]:
        all_greater = False
        break

    if all_greater:
      low_points.append((i, j))
      low_point_sum += 1 + data[i][j]
print(low_point_sum)

basin_sizes = []
for low_point in low_points:

  frontier = [low_point]
  visited = set()
  basin = set()
  while len(frontier) > 0:

    new_frontier = []
    for f in frontier:
      basin.add(f)
      visited.add(f)
      left = (f[0] - 1, f[1])
      up = (f[0], f[1] + 1)
      right = (f[0] + 1, f[1])
      down = (f[0], f[1] - 1)

      to_analyze = [up, down, right, left]
      for a in to_analyze:
        if a in visited:
          continue

        if a[0] < 0 or a[0] >= len(data):
          continue

        if a[1] < 0 or a[1] >= len(data[0]):
          continue

        if data[a[0]][a[1]] == 9:
          continue

        new_frontier.append(a)
    frontier = new_frontier
  basin_sizes.append(len(basin))

basin_sizes.sort(reverse=True)
product = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
print(product)

