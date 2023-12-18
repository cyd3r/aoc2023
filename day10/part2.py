from pathlib import Path
from collections import defaultdict

grid = []
with open(Path(__file__).parent / "input.txt") as f:
    for y, line in enumerate(f.readlines()):
        grid.append(line.strip())
        for x, c in enumerate(line.strip()):
            if c == "S":
                start_pos = (x, y)
                break


def get_move(from_pos, over_pos):
    from_x, from_y = from_pos
    over_x, over_y = over_pos
    over_c = grid[over_y][over_x]
    assert not (from_x == over_x and from_y == over_y)
    assert from_x == over_x or from_y == over_y
    if from_x == over_x:
        if from_y < over_y:
            if over_c == "|":
                return (over_x, over_y + 1)
            if over_c == "L":
                return (over_x + 1, over_y)
            if over_c == "J":
                return (over_x - 1, over_y)
        elif from_y > over_y:
            if over_c == "|":
                return (over_x, over_y - 1)
            if over_c == "F":
                return (over_x + 1, over_y)
            if over_c == "7":
                return (over_x - 1, over_y)
    if from_y == over_y:
        if from_x < over_x:
            if over_c == "-":
                return (over_x + 1, over_y)
            if over_c == "7":
                return (over_x, over_y + 1)
            if over_c == "J":
                return (over_x, over_y - 1)
        elif from_x > over_x:
            if over_c == "-":
                return (over_x - 1, over_y)
            if over_c == "F":
                return (over_x, over_y + 1)
            if over_c == "L":
                return (over_x, over_y - 1)

    # no movement possible in that direction
    return None

p = start_pos
for x, y, possible in [(-1, 0, ("-", "F", "L")), (1, 0, ("-", "7", "J")), (0, -1, ("|", "L", "J")), (0, 1, ("|", "7", "F"))]:
    if p[1] + y < 0 or p[0] + x < 0 or p[1] + y >= len(grid) or p[0] + x >= len(grid[0]):
        continue
    c = grid[p[1] + y][p[0] + x]
    if c in possible:
        over_pos = (p[0] + x, p[1] + y)

# start_symbol = "7"
start_symbol = "L"
from_pos = start_pos
num_steps = 1

pipes_by_row = defaultdict(list)
# pipes_by_row[start_pos[1]].append((start_pos[0], "F")) # L is hardcoded for the input file

while over_pos != start_pos:
    c = grid[over_pos[1]][over_pos[0]]
    # assert (from_pos[0], c) not in pipes_by_row[from_pos[1]]
    # print(c, end=",")
    fc = grid[from_pos[1]][from_pos[0]]
    if fc == "S":
        fc = start_symbol
    pipes_by_row[from_pos[1]].append((from_pos[0], fc))
    # print(from_pos, over_pos, grid[over_pos[1]][over_pos[0]])
    next_over_pos = get_move(from_pos, over_pos)
    assert next_over_pos is not None
    from_pos = over_pos
    over_pos = next_over_pos
    num_steps += 1
pipes_by_row[from_pos[1]].append((from_pos[0], grid[from_pos[1]][from_pos[0]]))

print(num_steps // 2)

# for y in range(10):
#     for x in range(20):
#         found = False
#         for c in pipes_by_row[y]:
#             if c[0] == x:
#                 print(c[1], end="")
#                 found = True
#                 break
#         if not found:
#             print(" ", end="")
#     print()
# print()


num_inside = 0
for rownum, row in pipes_by_row.items():
    # sort by x position
    row = sorted(row, key=lambda x: x[0])

    is_inside = False
    is_wall = False
    last_inside = False
    last_wall = False
    last_corner = None
    last_cur = None
    last_x = -1

    instr = ""
    inrow = 0
    for x, cur in row:
        if cur == "|":
            is_inside = not is_inside
        elif cur == "F" or cur == "L":
            is_wall = True
        elif cur == "J":
            is_wall = False
            if last_cur == "F":
                is_inside = not is_inside
            else:
                assert last_cur == "L"
        elif cur == "7":
            is_wall = False
            if last_cur == "L":
                is_inside = not is_inside
            else:
                assert last_cur == "F"

        if not last_wall and last_inside:
            inrow += x - last_x - 1

        last_wall = is_wall
        last_inside = is_inside

        if cur in ("|", "7", "J", "F", "L"):
            last_cur = cur
            last_x = x

    print("\t", inrow)
    num_inside += inrow
    # print()

print("Inside:", num_inside)

# 587