from pathlib import Path
import numpy as np

# expansion_factor = 2
# expansion_factor = 10
# expansion_factor = 100
expansion_factor = 1000000

positions = []
row_offset = 0
non_empty_cols = set()
with open(Path(__file__).parent / 'input.txt') as f:
    for y, line in enumerate(f.readlines()):
        row_is_empty = True
        for x, c in enumerate(line.strip()):
            if c == '#':
                row_is_empty = False
                positions.append((x, y + row_offset))
                non_empty_cols.add(x)
        if row_is_empty:
            row_offset += expansion_factor - 1

# update columns
non_empty_cols = np.array(list(non_empty_cols))

new_positions = []
for x, y in positions:
    num_non_empty_left = (non_empty_cols < x).sum()
    empty_left = x - num_non_empty_left
    new_positions.append((x + empty_left * (expansion_factor - 1), y))

def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

len_sum = 0
for i in range(len(new_positions)):
    for k in range(i + 1, len(new_positions)):
        len_sum += dist(new_positions[i], new_positions[k])

print(len_sum)
