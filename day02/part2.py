from collections import defaultdict

power_sum = 0

with open("input.txt") as f:
    for line in f.readlines():
        dice = line.split(":")[1].strip()
        rounds = dice.split("; ")
        is_possible = True
        min_dice = defaultdict(lambda: 0)
        for rnd in rounds:
            for die in rnd.split(", "):
                num, colour = die.split(" ")
                num = int(num)
                min_dice[colour] = max(min_dice[colour], num)

        pwr = min_dice["red"] * min_dice["green"] * min_dice["blue"]
        power_sum += pwr

print(power_sum)
