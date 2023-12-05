from pathlib import Path

seeds = []
current_map = None
maps = {}

map_names = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]

with open(Path(__file__).parent / "input.txt") as f:
    for line in f.readlines():
        if line.startswith("seeds"):
            raw_seeds = line.strip().split(": ")[1].split()
            seeds = [int(s) for s in raw_seeds]

        else:
            new_map = False
            for name in map_names:
                if line.startswith(name):
                    new_map = True
                    current_map = name
                    maps[current_map] = []

            if not new_map and current_map is not None:
                values = [int(n) for n in line.strip().split()]
                if len(values) == 3:
                    maps[current_map].append(values)

locations = []
for s in seeds:
    x = s
    # print('seed', x)
    for name in map_names:
        for dest, src, rng in maps[name]:
            if x >= src and x < src + rng:
                x += dest - src
                was_mapped = True
                break
        # print(x)

    locations.append(x)

print(min(locations))
