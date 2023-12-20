from pathlib import Path
from collections import defaultdict

FLIPFLOP = "%"
CONJUNCTION = "&"

children = {}
parents = defaultdict(list)
node_info = {}

with open(Path(__file__).parent / "input.txt") as f:
    for line in f.readlines():
        line = line.strip()

        src, targets = line.split(" -> ")
        targets = targets.split(", ")

        if src[0] in (FLIPFLOP, CONJUNCTION):
            node_type = src[0]
            src = src[1:]
        else:
            node_type = src

        node_info[src] = {"type": node_type}

        if node_type == FLIPFLOP:
            node_info[src]["is_on"] = False

        children[src] = targets
        for tgt in targets:
            parents[tgt].append(src)

for src, ps in parents.items():
    if src in node_info and node_info[src]["type"] == CONJUNCTION:
        node_info[src]['in_pulses'] = {n: False for n in ps}

num_low = 0
num_high = 0
for _ in range(1000):
    num_low += 1
    pending = [(n, 'broadcaster', False) for n in children["broadcaster"]]
    while pending:
        node, from_node, pulse = pending.pop(0)

        if pulse:
            num_high += 1
        else:
            num_low += 1

        if node not in node_info:
            continue

        info = node_info[node]
        if info['type'] == FLIPFLOP:
            if not pulse:
                info['is_on'] = not info['is_on']
                for c in children[node]:
                    pending.append((c, node, info['is_on']))
        elif info['type'] == CONJUNCTION:
            # update memory for incoming
            node_info[node]['in_pulses'][from_node] = pulse
            out_pulse = not all((node_info[node]['in_pulses'].values()))
            for c in children[node]:
                pending.append((c, node, out_pulse))

print('high', num_high, 'low', num_low)
print(num_high * num_low)
