from pathlib import Path
from collections import defaultdict

total_cards = 0
won_copies = defaultdict(lambda: 0)

with open(Path(__file__).parent / "input.txt") as f:
    for i, line in enumerate(f.readlines()):
        numbers = line.strip().split(": ")[1]
        left, right = numbers.split(" | ")
        left_nums = set((int(x) for x in left.split()))
        right_nums = set((int(x) for x in right.split()))

        num_winning = len(right_nums.intersection(left_nums))

        num_copies = won_copies[i]
        for c in range(i + 1, i + num_winning + 1):
            won_copies[c] += 1 + num_copies

print(sum(won_copies.values()) + i + 1)
print(max((won_copies.keys())))
