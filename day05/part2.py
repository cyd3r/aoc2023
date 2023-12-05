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

intervals = []
for seed_start, seed_range in zip(seeds[0::2], seeds[1::2]):
    intervals.append((seed_start, seed_start + seed_range - 1))

for name in map_names:
    mapping = sorted(maps[name], key=lambda x: x[1])

    new_intervals = []
    for start, end in intervals:
        s = start
        for dest, src, rng in mapping:
            offset = dest - src
            if s < src:
                e = min(src - 1, end)
                new_intervals.append((s, e))
                s = e + 1
                if e == end:
                    break

            if s < src + rng:
                e = min(src + rng - 1, end)
                new_intervals.append((s + offset, e + offset))
                s = e + 1
                if e == end:
                    break

        if s <= end:
            new_intervals.append((s, end))

    intervals = new_intervals

print(min((s for s, e in intervals)))
