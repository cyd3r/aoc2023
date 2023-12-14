from pathlib import Path
import numpy as np

blocks = []
block = []
with open(Path(__file__).parent / "input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            block.append([1 if c == "#" else 0 for c in line])
        else:
            if block:
                blocks.append(np.array(block))
            # new block
            block = []

    if block:
        blocks.append(np.array(block))

output = 0
for block in blocks:
    for i in range(1, block.shape[1]):
        max_len = min(block.shape[1] - i, i)
        left = block[:, i - max_len : i]
        right = block[:, i : i + max_len][:, ::-1]
        assert left.shape == right.shape
        if (left != right).sum() == 1:
            output += i

    for i in range(1, block.shape[0]):
        max_len = min(block.shape[0] - i, i)
        top = block[i - max_len : i]
        bottom = block[i : i + max_len][::-1]
        assert top.shape == bottom.shape
        if (top != bottom).sum() == 1:
            output += 100 * i

print(output)
