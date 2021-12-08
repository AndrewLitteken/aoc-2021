import sys

data = []

for line in sys.stdin:
  data.append(int(line.strip("\n")))

num_increased = 0
for index, item in enumerate(data[1:], 1):
  if item > data[index - 1]:
    num_increased += 1
print(num_increased)

num_increased_2 = 0
for index, item in enumerate(data[:-3]):
  sum_1 = sum(data[index:index+3])
  sum_2 = sum(data[index+1:index+4])
  if sum_2 > sum_1:
    num_increased_2 += 1
print(num_increased_2)