import sys

data = []

for line in sys.stdin:
  data.append(line.strip("\n"))

gamma_rate = ""
epsilon_rate = ""

for i in range(len(data[0])):
  one_count = 0
  zero_count = 0
  for item in data:
    c = item[i]
    if c == "1":
      one_count += 1
    else:
      zero_count += 1

  if one_count > zero_count:
    gamma_rate += "1"
    epsilon_rate += "0"
  else:
    gamma_rate += "0"
    epsilon_rate += "1"

gamma_num = int(gamma_rate, 2)
epsilon_num = int(epsilon_rate, 2)

print(gamma_num*epsilon_num)

items = set(data)
ox_gen_val = None
for i in range(len(data[0])):
  zeroes_in_pos = set()
  ones_in_pos = set()
  one_count = 0
  zero_count = 0
  for item in items:
    c = item[i]
    if c == "1":
      ones_in_pos.add(item)
      one_count += 1
    else:
      zeroes_in_pos.add(item)
      zero_count += 1

  if one_count > zero_count:
    for item in zeroes_in_pos:
      items.remove(item)
  elif one_count < zero_count:
    for item in ones_in_pos:
      items.remove(item)
  else:
    for item in zeroes_in_pos:
      items.remove(item)

  if len(items) == 1:
    ox_gen_val = list(items)[0]
    break

items = set(data)
co2_gen_val = None
for i in range(len(data[0])):
  zeroes_in_pos = set()
  ones_in_pos = set()
  one_count = 0
  zero_count = 0
  for item in items:
    c = item[i]
    if c == "1":
      ones_in_pos.add(item)
      one_count += 1
    else:
      zeroes_in_pos.add(item)
      zero_count += 1

  if one_count > zero_count:
    for item in ones_in_pos:
      items.remove(item)
  elif one_count < zero_count:
    for item in zeroes_in_pos:
      items.remove(item)
  else:
    for item in ones_in_pos:
      items.remove(item)

  if len(items) == 1:
    co2_gen_val = list(items)[0]
    break

ox_num = int(ox_gen_val, 2)
co2_num = int(co2_gen_val, 2)

print(ox_num*co2_num)