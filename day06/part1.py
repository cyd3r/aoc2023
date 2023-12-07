from pathlib import Path
import math

times = []
distances = []
with open(Path(__file__).parent / "input.txt") as f:
    nums = f.readline().strip().split(":")[1].split()
    times = [int(n) for n in nums]

    nums = f.readline().strip().split(":")[1].split()
    distances = [int(n) for n in nums]


def calc(t, d):
    left = 0.5 * (t + math.sqrt(t * t - 4 * d))
    right = 0.5 * (t - math.sqrt(t * t - 4 * d))
    if left > right:
        left, right = right, left

    left = math.ceil(left)
    right = math.floor(right)

    return right - left + 1


out = 1
for t, d in zip(times, distances):
    t2 = calc(t, d + 1)
    out *= t2
print(out)
