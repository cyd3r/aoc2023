import numpy as np
from pathlib import Path


def to_arr(text):
    values = []
    for c in text:
        if c == "A":
            values.append(14)
        elif c == "K":
            values.append(13)
        elif c == "Q":
            values.append(12)
        elif c == "J":
            values.append(11)
        elif c == "T":
            values.append(10)
        else:
            values.append(int(c))

    # let the cards start at 1
    return np.array(values) - 1


def get_hand_type(cards):
    unique_cards, counts = np.unique(cards, return_counts=True)
    if len(unique_cards) == 1 and counts.max() == 5:
        # five of a kind
        type_id = 6
    elif len(unique_cards) == 2 and counts.max() == 4:
        # four of a kind
        type_id = 5
    elif len(unique_cards) == 2 and counts.max() == 3:
        # full house
        type_id = 4
    elif len(unique_cards) == 3 and counts.max() == 3:
        # three of a kind
        type_id = 3
    elif len(unique_cards) == 3 and counts.max() == 2:
        # two pair
        type_id = 2
    elif len(unique_cards) == 4 and counts.max() == 2:
        # one pair
        type_id = 1
    elif len(unique_cards) == 5 and counts.max() == 1:
        type_id = 0
    else:
        raise RuntimeError(cards)

    return type_id


def get_rank(cards):
    card_rank = 0
    for i, c in enumerate(cards):
        card_rank += (14 ** (4 - i)) * c

    type_id = get_hand_type(cards)
    card_rank += (14**5) * type_id
    return card_rank


ranks_bids = []
with open(Path(__file__).parent / "input.txt") as f:
    for line in f.readlines():
        str_cards, bid = line.strip().split()
        cards = to_arr(str_cards)
        bid = int(bid)

        ranks_bids.append((get_rank(cards), bid))

ranks_bids = sorted(ranks_bids, key=lambda x: x[0])
output = 0
for i, (_, bid) in enumerate(ranks_bids):
    output += (i + 1) * bid

print(output)
