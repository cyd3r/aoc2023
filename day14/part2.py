from pathlib import Path
from collections import defaultdict
import numpy as np

last_fixpos = defaultdict(lambda: -1)
rocks_in_row = defaultdict(lambda: 0)
num_lines = 0
total = 0

with open(Path(__file__).parent / "input.txt") as f:
    rows = []
    for y, line in enumerate(f.readlines()):
        row = []
        for x, c in enumerate(line.strip()):
            if c == "#":
                row.append(9)
            elif c == ".":
                row.append(0)
            elif c == "O":
                row.append(1)
        rows.append(row)

grid = np.array(rows)


def print_rocks(rocks: np.ndarray):
    for row in rocks:
        for c in row:
            if c == 0:
                print(".", end="")
            elif c == 1:
                print("O", end="")
            elif c == 9:
                print("#", end="")
        print()


def move_rocks(rocks: np.ndarray):
    for row in rocks:
        last_fixed_pos = -1
        for fixed_pos in (row == 9).nonzero()[0]:
            between_rocks = row[last_fixed_pos + 1 : fixed_pos].sum()
            row[last_fixed_pos + 1 : fixed_pos] = 0
            row[last_fixed_pos + 1 : last_fixed_pos + 1 + between_rocks] = 1
            last_fixed_pos = fixed_pos

        fixed_pos = len(row)
        between_rocks = row[last_fixed_pos + 1 : fixed_pos].sum()
        row[last_fixed_pos + 1 : fixed_pos] = 0
        row[last_fixed_pos + 1 : last_fixed_pos + 1 + between_rocks] = 1


def get_hash(rocks: np.ndarray):
    out_set = []
    for y, x in zip(*(rocks == 1).nonzero()):
        out_set.append((int(y), int(x)))
    return frozenset(out_set)


def get_load(rocks: np.ndarray):
    return (rocks.shape[1] - (rocks == 1).nonzero()[1]).sum()


# north
grid = np.rot90(grid)

states = set()


def cycle(rocks: np.ndarray):
    # north
    move_rocks(rocks)
    # west
    rocks = np.rot90(rocks, k=3)
    move_rocks(rocks)
    # south
    rocks = np.rot90(rocks, k=3)
    move_rocks(rocks)
    # east
    rocks = np.rot90(rocks, k=3)
    move_rocks(rocks)
    # rotate to north
    rocks = np.rot90(rocks, k=3)
    return rocks


state_ids = {get_hash(grid): 0}

i = 0
cycle_len = None
cycle_start = None
while True:
    i += 1
    grid = cycle(grid)

    state = get_hash(grid)

    if state in state_ids:
        cycle_len = i - state_ids[state]
        cycle_start = state_ids[state]
        break

    state_ids[state] = i


for _ in range((1000000000 - cycle_start) % cycle_len):
    grid = cycle(grid)

print(get_load(grid))

# 93102