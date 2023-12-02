import re

SAMPLE:list[str] = [*open("data/02-p1-sample.txt")]
DATA:list[str] = [*open("data/02.txt")]

def get_count(color:str, s:str)->int:
    matches = re.findall(fr"(\d+) {color}", s)
    if matches:
        return int(matches[0])
    else: 
        return 0

def get_max_values(line) -> (int, (int,int,int)):
    game = int(re.findall(r"Game (\d+):", line)[0])
    draws_str = line[line.find(": ")+2:]
    draws:list[str] = draws_str.split("; ")

    reds = [get_count("red", s) for s in draws]
    red = max(reds)
    greens = [get_count("green", s) for s in draws]
    green = max(greens)
    blues = [get_count("blue", s) for s in draws]
    blue = max(blues)
    
    return (game, (red, green, blue))

def part1(target:(int,int,int), lines:list[str]) -> int:
    game_maxes = [get_max_values(s) for s in lines]
    total = 0
    for (game, maxes) in game_maxes:
        if all(a <= b for (a, b) in zip(maxes, target)): #(red <= target[0] and green <= target[1] and blue <= target[2]):
            total += game
    return total

def part2(lines:list[str]) -> int:
    game_maxes = [get_max_values(s) for s in lines]
    total = 0
    for (game, (red, green, blue)) in game_maxes:
        total += red*green*blue
    return total


assert 8 == part1((12,13,14), SAMPLE)
assert 2563 == part1((12,13,14), DATA)
assert 2286 == part2(SAMPLE)
assert 70768 == part2(DATA)