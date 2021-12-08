import sys
import copy

data = []

for line in sys.stdin:
  data.append(line.strip("\n"))

num_list = [int(i) for i in data[0].split(",")]

boards = []

board = {"rows": [], "cols": []}
for i, line in enumerate(data[2:]):
  if line == "":
    boards.append(board)
    board = {"rows": [], "cols": []}
    continue

  nums = [int(j) for j in line.split(" ") if j != ""]
  board["rows"].append(set(nums))
  if len(board["cols"]) == 0:
    board["cols"] = [set() for j in range(len(nums))]
  for j, num in enumerate(nums):
    board["cols"][j].add(num)

boards.append(board)
boards_cp = copy.deepcopy(boards)

bingo_found_num = None
bingo_found_board = None
for num in num_list:

  for board in boards_cp:

    for row in board["rows"]:
      if num in row: row.remove(num)
      if len(row) == 0:
        bingo_found_num = num
        bingo_found_board = board

    for col in board["cols"]:
      if num in col: col.remove(num)
      if len(col) == 0:
        bingo_found_num = num
        bingo_found_board = board

    if bingo_found_board is not None:
      break
  if bingo_found_board is not None:
    break

remaining_sum = 0
for row in bingo_found_board["rows"]:
  for num in row:
    remaining_sum += num

print(bingo_found_num)
print(remaining_sum*bingo_found_num)

boards_cp = copy.deepcopy(boards)
bingo_found_num = None
bingo_found_board = None
not_winning = set(list(range(len(boards_cp))))
for num in num_list:

  for i, board in enumerate(boards_cp):
    if i not in not_winning:
      continue

    for row in board["rows"]:
      if num in row: row.remove(num)
      if len(row) == 0:
        if len(not_winning) == 1:
          bingo_found_num = num
          bingo_found_board = board
        if i in not_winning: not_winning.remove(i)

    for col in board["cols"]:
      if num in col: col.remove(num)
      if len(col) == 0:
        if len(not_winning) == 1:
          bingo_found_num = num
          bingo_found_board = board
        if i in not_winning: not_winning.remove(i)

    if len(not_winning) == 0:
      break
  if len(not_winning) == 0:
      break

remaining_sum = 0
for row in bingo_found_board["rows"]:
  for num in row:
    remaining_sum += num
print(remaining_sum)
print(bingo_found_board)
print(bingo_found_num)
print(remaining_sum*bingo_found_num)
