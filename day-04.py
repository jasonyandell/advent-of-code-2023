import re
from parse import parse
from collections import Counter

SAMPLE = [*open("data/04-sample.txt")]
INPUT = [*open("data/04.txt")]

def getWinners(line)->(int,int):
    _, card, winnersStr, mineStr = parse("Card{}{:d}: {} | {}", line)
    getNums = lambda line:set([int(s) for s in re.findall(r"(\d+)", line)])

    winners = getNums(winnersStr)
    mine = getNums(mineStr)
    myWinners = winners & mine

    return card, len(myWinners)

def part1(input):
    score = lambda matchCount: 0 if matchCount==0 else 2**(matchCount-1)
    return sum([score(getWinners(s)[1]) for s in input])

def part2(input):
    gameToWinners = {}
    for line in input:
        game, winners = getWinners(line)
        gameToWinners[game] = winners
    
    cardCounts = {}
    for game in gameToWinners.keys():
        cardCounts[game] = 1
    
    for game, winners in gameToWinners.items(): 
        for i in range(game+1, game+1+winners):
            cardCounts[i] += cardCounts[game]

    return sum(cardCounts.values())
    
print("Part1 SAMPLE", part1(SAMPLE))
print("Part1", part1(INPUT))

print("Part2 SAMPLE", part2(SAMPLE))
print("Part2", part2(INPUT))
