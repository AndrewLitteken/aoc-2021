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

  count_per_day = count_per_day[1:7] + [count_per_day[0] + count_per_day[7], count_per_day[8], count_per_day[0]]

  day += 1

total = sum(count_per_day)
print(total)