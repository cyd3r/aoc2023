import re
from pathlib import Path

all_numbers = []
pos_to_id = {}
symbol_positions = []

with open(Path(__file__).parent / "input.txt") as f:
    for y, line in enumerate(f.readlines()):
        for m in re.finditer(r"\d+|[^\.]", line.strip()):
            try:
                value = int(m.group())
            except ValueError:
                assert len(m.group()) == 1, m.group()
                symbol_positions.append((y, m.start()))
                continue

            for x in range(m.start(), m.end()):
                pos_to_id[(y, x)] = len(all_numbers)
            all_numbers.append(value)

adjacent_ids = set()
for sy, sx in symbol_positions:
    for y in range(sy - 1, sy + 2):
        for x in range(sx - 1, sx + 2):
            if (y, x) in pos_to_id:
                adjacent_ids.add(pos_to_id[(y, x)])

print(sum((all_numbers[i] for i in adjacent_ids)))
