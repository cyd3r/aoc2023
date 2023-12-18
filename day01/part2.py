import re

names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def parse_line(line):
    min_val = None
    max_val = None

    for s in range(len(line)):
        for i in range(1, 10):
            if line[s] == str(i):
                max_val = i
                if min_val is None:
                    min_val = i
        for i, name in enumerate(names, 1):
            if line[s:s+len(name)] == name:
                max_val = i
                if min_val is None:
                    min_val = i

    return min_val * 10 + max_val


sum = 0
with open("input.txt") as f:
    for line in f.readlines():
        sum += parse_line(line.strip())

print(sum)
