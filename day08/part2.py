from pathlib import Path
from collections import defaultdict

forks = {}

with open(Path(__file__).parent / "input.txt") as f:
    sequence = f.readline().strip()
    f.readline()
    for line in f.readlines():
        src, dest = line.strip().split(" = ")
        nodes = dest.strip("()").split(", ")

        forks[src] = nodes

# num steps for node&sequence idx

required_steps = defaultdict(list)


for start_pos in forks:
    if start_pos[2] != "A":
        continue
    processed = set()
    num_steps = 0
    current = start_pos
    while True:
        si = num_steps % len(sequence)

        if (current, si) in processed:
            # entering a cycle -> abort
            break
        processed.add((current, si))

        if current[2] == "Z":
            required_steps[start_pos].append(num_steps)

        d = sequence[si]
        num_steps += 1
        assert d in ("L", "R")
        if d == "L":
            current = forks[current][0]
        else:
            current = forks[current][1]

print(required_steps)

p = 1
for x in required_steps.values():
    y = x[0] % (len(sequence) - 1)
    p *= y
print(p * len(sequence))