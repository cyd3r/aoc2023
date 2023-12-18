from pathlib import Path

grid = []
with open(Path(__file__).parent / "example.txt") as f:
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

from_pos = start_pos
num_steps = 1
print(start_pos, over_pos)

while over_pos != start_pos:
    # print(from_pos, over_pos, grid[over_pos[1]][over_pos[0]])
    next_over_pos = get_move(from_pos, over_pos)
    assert next_over_pos is not None
    from_pos = over_pos
    over_pos = next_over_pos
    num_steps += 1

print(num_steps // 2)
