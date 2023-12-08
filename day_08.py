"""8"""

import parse
import math

SAMPLE = [*open("data/08-sample.txt")]
SAMPLE2 = [*open("data/08-sample2.txt")]
INPUT = [*open("data/08.txt")]


def parse_input(lines):
    path = lines[0].strip()
    map = {}
    for line in lines[2:]:
        node, l, r = parse.parse("{:w} = ({:w}, {:w})", line.strip())
        map[node] = {'L':l, 'R':r}
    return path, map

def part_1(lines):
    path, map = parse_input(lines)
    step = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        curr = map[curr][path[step % len(path)]] # map['AAA']['L']
        step += 1
    return step

def traverse_count(start:str, path, map):
    step = 0
    curr = start
    while not curr.endswith('Z'):
        curr = map[curr][path[step % len(path)]] # map['AAA']['L']
        step += 1
    return step

def part_2(lines):
    path, map = parse_input(lines)
    path_lengths = []
    for key in map:
        if not key.endswith('A'): continue
        path_lengths.append(traverse_count(key, path, map))
    return math.lcm(*path_lengths)

print("Part1 Sample", part_1(SAMPLE))
print("Part1", part_1(INPUT))
print("Part2 Sample", part_2(SAMPLE2))
print("Part2", part_2(INPUT))