import re
from parse import parse
from collections import Counter

SAMPLE = [*open("data/04-sample.txt")]
INPUT = [*open("data/04.txt")]

def get_winners(line)->(int,int):
    """get the winners"""
    _, card, winners_str, mine_str = parse("Card{}{:d}: {} | {}", line)
    def get_nums(line):
        return set(int(s) for s in re.findall(r"(\d+)", line))

    winners = get_nums(winners_str)
    mine = get_nums(mine_str)
    my_winners = winners & mine

    return card, len(my_winners)

def part1(lines):
    """part1"""
    def score(match_count):
        return 0 if match_count==0 else 2**(match_count-1)
    return sum(score(get_winners(s)[1]) for s in lines)

def part2(lines):
    """part2"""
    game_to_winners = {}
    for line in lines:
        game, winners = get_winners(line)
        game_to_winners[game] = winners

    card_counts = {}
    for game in game_to_winners:
        card_counts[game] = 1

    for game, winners in game_to_winners.items():
        for i in range(game+1, game+1+winners):
            card_counts[i] += card_counts[game]

    return sum(card_counts.values())

print("Part1 SAMPLE", part1(SAMPLE))
print("Part1", part1(INPUT))

print("Part2 SAMPLE", part2(SAMPLE))
print("Part2", part2(INPUT))
