import sys
import copy

data = []

for line in sys.stdin:
  data.append(line.strip("\n"))

horiz_pos = [int(d) for d in data[0].split(",")]

max_pos = max(horiz_pos)

min_align = float("inf")
min_pos = None
for i in range(max_pos + 1):
  align_cost = 0
  for j in horiz_pos:
    align_cost += abs(j - i)
  if min_align > align_cost:
    min_align = align_cost
    min_pos = i
print(min_pos, min_align)

min_align = float("inf")
min_pos = None
for i in range(max_pos + 1):
  align_cost = 0
  for j in horiz_pos:
    diff = abs(j - i)
    align_cost += diff * (diff + 1) // 2
  if min_align > align_cost:
    min_align = align_cost
    min_pos = i
print(min_pos, min_align)