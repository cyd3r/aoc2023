from pathlib import Path
from collections import defaultdict

last_fixpos = defaultdict(lambda: -1)
rocks_in_row = defaultdict(lambda: 0)
num_lines = 0
total = 0

with open(Path(__file__).parent / "input.txt") as f:
    for y, line in enumerate(f.readlines()):
        num_lines += 1
        for x, c in enumerate(line.strip()):
            if c == "#":
                last_fixpos[x] = y
            elif c == ".":
                pass
            elif c == "O":
                total += 1
                last_fixpos[x] += 1
                rocks_in_row[last_fixpos[x]] += 1

output = 0
for y in range(num_lines):
    print(num_lines - y, rocks_in_row[y])
    output += rocks_in_row[y] * (num_lines - y)
print(output)
print("total", total)
