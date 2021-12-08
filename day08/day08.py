import sys
import copy
from collections import defaultdict

data = []

unique_lines = []
outputs = []
for line in sys.stdin:
  data.append(line.strip("\n"))
  unique_lines.append(line.strip("\n").split(" | ")[0].split(" "))
  outputs.append(line.strip("\n").split(" | ")[1].split(" "))

counts = 0
for i in range(len(unique_lines)):
  signal_map = {}
  for signal in unique_lines[i]:
    sorted_t = tuple(sorted(list(signal)))
    if len(signal) == 2:
      signal_map[sorted_t] = 1
    elif len(signal) == 3:
      signal_map[sorted_t] = 7
    elif len(signal) == 4:
      signal_map[sorted_t] = 4
    elif len(signal) == 7:
      signal_map[sorted_t] = 8

  for signal in outputs[i]:
    sorted_t = tuple(sorted(list(signal)))
    if sorted_t in signal_map:
      counts += 1
print(counts)

counts = 0
mapping_to_num = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4,
                   "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}
for i in range(len(unique_lines)):
  signal_map = {}
  back_map = {}
  mapping_to_real = {"a": None, "b": None, "c": None, "d": None,
                     "e": None, "f": None, "g": None}
  lengths = defaultdict(list)
  for signal in unique_lines[i]:
    sorted_t = tuple(sorted(list(signal)))
    if len(signal) == 2:
      signal_map[sorted_t] = 1
      back_map[1] = sorted_t
    elif len(signal) == 3:
      signal_map[sorted_t] = 7
      back_map[7] = sorted_t
    elif len(signal) == 4:
      signal_map[sorted_t] = 4
      back_map[4] = sorted_t
    elif len(signal) == 7:
      signal_map[sorted_t] = 8
      back_map[8] = sorted_t
    lengths[len(signal)].append(sorted_t)

  a_val = set(back_map[7]).difference(set(back_map[1])).pop()
  mapping_to_real[a_val] = "a"
  for signal in lengths[6]:
    inter = set(signal).intersection(set(back_map[1]))
    diff = set(back_map[1]).difference(set(signal))
    if len(inter) == 1:
      signal_map[signal] = 6
      f_val = inter.pop()
      mapping_to_real[f_val] = "f"
      c_val = diff.pop()
      mapping_to_real[c_val] = "c"
    else:
      inter = set(signal).intersection(set(back_map[4]))
      if len(inter) == 3:
        signal_map[signal] = 0
        diff = set(back_map[4]).difference(set(signal))
        b_val = inter.difference(set(back_map[1])).pop()
        mapping_to_real[b_val] = "b"
        d_val = diff.pop()
        mapping_to_real[d_val] = "d"
      else:
        signal_map[signal] = 9
        full_inter = set("abcdefg").difference(set(signal))
        e_val = full_inter.pop()
        mapping_to_real[e_val] = "e"
        diff = set(signal).difference(set(back_map[4])).difference(set(back_map[7]))
        g_val = diff.pop()
        mapping_to_real[g_val] = "g"
  for signal in unique_lines[i]:
    sorted_t = tuple(sorted(list(signal)))
    if sorted_t in signal_map:
      continue
    test = []
    for c in sorted_t:
      test.append(mapping_to_real[c])
    test.sort()
    num = mapping_to_num["".join(test)]
    signal_map[sorted_t] = num

  string = ""
  for signal in outputs[i]:
    sorted_t = tuple(sorted(list(signal)))
    string += str(signal_map[sorted_t])
  counts += int(string)
print(counts)