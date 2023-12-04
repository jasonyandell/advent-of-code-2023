import re
from parse import parse

SAMPLE = [*open("data/04-sample.txt")]
INPUT = [*open("data/04.txt")]

def getWinners(line):
    _, card, winnersStr, mineStr = parse("Card{}{:d}: {} | {}", line)
    getNums = lambda line:set([int(s) for s in re.findall(r"(\d+)", line)])
    
    winners = getNums(winnersStr)
    mine = getNums(mineStr)
    myWinners = winners & mine

    score = 0
    if len(myWinners): score = 2**(len(myWinners)-1)

    return score

def part1(input):
    return sum([getWinners(s) for s in input])
    
print("Part1 SAMPLE", part1(SAMPLE))
print("Part1:", part1(INPUT))