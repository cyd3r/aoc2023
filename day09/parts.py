from pathlib import Path

def predict_next(nums):
    is_same = True
    output = []
    prev = nums[0]
    for x in nums[1:]:
        if x != prev:
            is_same = False
        output.append(x - prev)
        prev = x

    if is_same:
        return prev, prev
    else:
        left, right = predict_next(output)
        return nums[0] - left, nums[-1] + right


left_sum = 0
right_sum = 0
with open(Path(__file__).parent / "input.txt") as f:
    for line in f.readlines():
        nums = [int(x) for x in line.strip().split()]
        l, r = predict_next(nums)
        left_sum += l
        right_sum += r
print(left_sum, right_sum)
