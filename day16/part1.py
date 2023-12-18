from pathlib import Path
from collections import defaultdict

by_x = defaultdict(list)
by_y = defaultdict(list)
get_x_idx = defaultdict(dict)
get_y_idx = defaultdict(dict)

with open(Path(__file__).parent / "input.txt") as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            if c in ("/", "\\", "-", "|"):
                by_x[x].append((y, c))
                by_y[y].append((x, c))

                get_x_idx[y][x] = len(by_y[y]) - 1
                get_y_idx[x][y] = len(by_x[x]) - 1

height = y + 1
width = x + 1

def myrange(a, b):
    if a > b:
        a, b = b, a
    return range(a, b + 1)

def move(c, axis, direction):
    assert direction in (1, -1)
    assert axis in ("x", "y")
    if c == "\\":
        if axis == "x":
            yield ("y", direction)
        if axis == "y":
            yield ("x", direction)
    elif c == "/":
        if axis == "x":
            yield ("y", -direction)
        if axis == "y":
            yield ("x", -direction)
    elif c == "|":
        if axis == "y":
            yield (axis, direction)
        yield ("y", -1)
        yield ("y", 1)
    elif c == "-":
        if axis == "x":
            yield (axis, direction)
        yield ("x", -1)
        yield ("x", 1)
    else:
        raise RuntimeError()


visited_tiles = set()
# move: pos, axis, direction
already_moved = set()


pending_moves = [("x", 1, 0, 0)]
while pending_moves:
    the_move = pending_moves.pop()
    if the_move in already_moved:
        continue
    already_moved.add(the_move)

    move_axis, move_dir, x_pos, y_pos = the_move

    if move_axis == "x":
        if x_pos == 0 and y_pos == 0 and move_dir == 1:
            new_x, c = by_y[y_pos][0]
        else:
            x_idx = get_x_idx[y_pos][x_pos] + move_dir
            # beam hit the border?
            if x_idx < 0:
                for x in myrange(0, x_pos):
                    visited_tiles.add((x, y_pos))
                continue
            elif x_idx >= len(by_y[y_pos]):
                for x in myrange(x_pos, width - 1):
                    visited_tiles.add((x, y_pos))
                continue
            new_x, c = by_y[y_pos][x_idx]

        for x in myrange(x_pos, new_x):
            visited_tiles.add((x, y_pos))

        for m in move(c, move_axis, move_dir):
            pending_moves.append((*m, new_x, y_pos))
    elif move_axis == "y":
        y_idx = get_y_idx[x_pos][y_pos] + move_dir
        # beam hit the border?
        if y_idx < 0:
            for y in myrange(0, y_pos):
                visited_tiles.add((x_pos, y))
            continue
        elif y_idx >= len(by_x[x_pos]):
            for y in myrange(y_pos, height - 1):
                visited_tiles.add((x_pos, y))
            continue
        new_y, c = by_x[x_pos][y_idx]

        for y in myrange(y_pos, new_y):
            visited_tiles.add((x_pos, y))

        for m in move(c, move_axis, move_dir):
            pending_moves.append((*m, x_pos, new_y))

print("done", len(visited_tiles))

# for y in range(10):
#     for x in range(10):
#         if (x, y) in visited_tiles:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()
