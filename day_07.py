"""7"""
from collections import Counter

SAMPLE=[*open("data/07-sample.txt")]
INPUT=[*open("data/07.txt")]

values = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6,'9':7,'T':8,'J':9,'Q':10, 'K':11, 'A':12}

def type_of(hand):
    counter = Counter(hand)
    two_of_a_kind = set([char for char, count in counter.items() if count == 2])
    three_of_a_kind = set([char for char, count in counter.items() if count == 3])
    four_of_a_kind = set([char for char, count in counter.items() if count == 4])
    five_of_a_kind = set([char for char, count in counter.items() if count == 5])
    two_pair = len(two_of_a_kind)==2
    full_house = True if len(two_of_a_kind) > 0 and len(two_of_a_kind | three_of_a_kind) > len(two_of_a_kind) else False
    if five_of_a_kind: return 6
    if four_of_a_kind: return 5
    if full_house: return 4
    if three_of_a_kind: return 3
    if two_pair: return 2
    if two_of_a_kind: return 1
    return 0

def score(hand):
    total = 0
    for card in hand:
        total = total * 13 + values[card]
    type_value = type_of(hand)
    total = type_value * 10000000 + total
    return total

def part1(lines):
    scores = []
    for line in lines:
        hand, bid_str = line.split()
        bid = int(bid_str)        
        scores.append((score(hand), bid))
    ordered_scores = sorted(scores, key=lambda x: x[0])
    total = 0
    for i in range(len(ordered_scores)):
        _, bid = ordered_scores[i]
        total += (i+1) * bid
    return total

print(part1(SAMPLE))

print(part1(INPUT))