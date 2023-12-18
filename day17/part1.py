from pathlib import Path

grid = []
with open(Path(__file__).parent / "example.txt") as f:
    for line in f.readlines():
        grid.append([int(n) for n in line.strip()])

height = len(grid)
width = len(grid[0])

pending = [((1, 0), (0, 0), 0), ((0, 1), (0, 0), 0)]
visited = set()
max_straight_steps = 3
parent = {}

def tuple_add(left, right):
    return (left[0] + right[0], left[1] + right[1])

while pending:
    move = pending.pop(0)
    if move in visited:
        continue
    visited.add(move)

    direction, pos, straigth_steps = move

    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if d == direction:
            s = straigth_steps + 1
            if s > max_straight_steps:
                # move not allowed
                continue
        else:
            s = 0
        new_pos = tuple_add(pos, d)
        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= width or new_pos[1] >= height:
            # move not allowed
            continue
        if new_pos[0] == 12 and new_pos[1] == 12:
            print("reached")
            print(parent[pos])
            pending = []
            break
        if new_pos in parent:
            (prev_pos, path_len) = parent[new_pos]
            new_path_len = parent[pos][1] + 1
            if new_path_len < path_len:
                parent[new_pos] = (pos, new_path_len)
        else:
            parent[new_pos] = (pos,1)
        pending.append((d, new_pos, s))

print("done")