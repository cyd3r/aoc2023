from pathlib import Path
import math

with open(Path(__file__).parent / 'input.txt') as f:
    t = int(f.readline().strip().split(':')[1].replace(' ', ''))
    d = int(f.readline().strip().split(':')[1].replace(' ', ''))

def calc(t, d):
    left = .5 * (t + math.sqrt(t * t - 4 * d))
    right = .5 * (t - math.sqrt(t * t - 4 * d))
    if left > right:
        left, right = right, left

    left = math.ceil(left)
    right = math.floor(right)

    return right - left + 1

print(calc(t, d+1))
