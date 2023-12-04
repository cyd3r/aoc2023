import re

max_red = 12
max_green = 13
max_blue = 14
id_sum = 0

with open("input.txt") as f:
    for line in f.readlines():
        game_id = int(re.match(r"Game (\d+):", line)[1])
        dice = line.split(":")[1].strip()
        rounds = dice.split("; ")
        is_possible = True
        for rnd in rounds:
            for die in rnd.split(", "):
                num, colour = die.split(" ")
                num = int(num)
                if colour == "red" and num > max_red:
                    is_possible = False
                    break
                elif colour == "green" and num > max_green:
                    is_possible = False
                    break
                elif colour == "blue" and num > max_blue:
                    is_possible = False
                    break

            if not is_possible:
                break

        if is_possible:
            id_sum += game_id

print(id_sum)