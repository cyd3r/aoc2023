from pathlib import Path

point_sum = 0

with open(Path(__file__).parent / "input.txt") as f:
    for line in f.readlines():
        numbers = line.strip().split(": ")[1]
        left, right = numbers.split(" | ")
        left_nums = set((int(x) for x in left.split()))
        right_nums = set((int(x) for x in right.split()))

        winning = len(right_nums.intersection(left_nums))

        if winning > 0:
            point_sum += 2 ** (winning - 1)

print(point_sum)
