from pathlib import Path

forks = {}

with open(Path(__file__).parent / "input.txt") as f:
    sequence = f.readline().strip()
    f.readline()
    for line in f.readlines():
        src, dest = line.strip().split(" = ")
        nodes = dest.strip("()").split(", ")

        forks[src] = nodes

current = "AAA"
i = 0
num_steps = 0
while current != "ZZZ":
    num_steps += 1
    d = sequence[i]
    assert d in ("L", "R")
    if d == "L":
        current = forks[current][0]
    else:
        current = forks[current][1]
    i = (i + 1) % len(sequence)

print(num_steps)