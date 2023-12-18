import re

sum = 0
with open("input.txt") as f:
    for line in f.readlines():
        digits = re.findall(r"\d", line)
        number = int(digits[0] + digits[-1])
        sum += number

print(sum)
