# dumb brute force solution to get the task for part 2
from pathlib import Path


def place(numbers: list, remainig):
    if len(numbers) == 0:
        yield 0
        return
    if remainig < 0:
        # yield 0
        return
    n = numbers[0]
    numsum = sum(numbers[1:]) + len(numbers) - 2
    for i in range(1 + remainig - n - numsum):
        end_pos = i + n - 1
        # i is the starting position
        # i + n - 1 is the end position
        # everything up until start position
        start_range = (1 << i) - 1
        # everything including end position
        end_range = (1 << (end_pos + 1)) - 1
        spring = end_range - start_range

        new_remaining = remainig - (end_pos + 2)
        if new_remaining >= numsum:
            for p in place(numbers[1:], remainig=new_remaining):
                yield spring + (p << end_pos + 2)


def print_mask(mask, n):
    i = 0
    for i in range(n):
        probe = 1 << i
        if (mask & probe) == probe:
            print("#", end="")
        else:
            print(".", end="")
    print()


all_num_valid = 0
with open(Path(__file__).parent / "input.txt") as f:
    for line in f.readlines():
        springs, numbers = line.strip().split()
        pos_mask = 0
        neg_mask = 0
        for i, c in enumerate(springs):
            if c == "#":
                pos_mask += 1 << i
            if c == ".":
                neg_mask += 1 << i

        numbers = [int(n) for n in numbers.split(",")]

        num_valid = 0
        total = 0
        for config in place(numbers, remainig=len(springs)):
            total += 1
            if (config & pos_mask) == pos_mask and ((~config) & neg_mask) == neg_mask:
                num_valid += 1
        all_num_valid += num_valid

print(all_num_valid)
