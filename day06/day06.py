import sys
import copy

days = int(sys.argv[1])
data = []

for line in sys.stdin:
  data.append(line.strip("\n"))

fish_nums = [int(d) for d in data[0].split(",")]

count_per_day = [0]*9
for i in range(9):
  count_per_day[i] = 0

for i in fish_nums:
  count_per_day[i] += 1

day = 0
while day < days:

  added = 0
  for age in range(9):
    if age != 0:
      count_per_day[age - 1] += count_per_day[age]
      count_per_day[age] -= count_per_day[age]
      if age == 6 or age == 8:
        count_per_day[age] += added
      continue
    elif age == 0:
      added = count_per_day[age]
      count_per_day[age] -= count_per_day[age]

  day += 1

total = sum(count_per_day)
print(total)