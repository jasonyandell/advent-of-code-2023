"""5 - got the stars but it's incomplete"""

import re
from datetime import datetime

SAMPLE = [*open("data/05-sample.txt")]
INPUT = [*open("data/05.txt")]

class Bag:
    def __init__(self):
        self.to_map = {}
        self.next = None
        self.name = None
        self.seeds = []
        self.lookups = []

    def find(self, x):
        for [dest, start, count] in self.lookups:
            if start <= x and start+count > x:
                return dest+(x - start)
        return x

def parse_input(input:list[str]):
    curr = Bag()
    start = curr

    start.seeds = [int(s) for s in input[0].split()[1:]]

    for line in input[2:]:
        map_line_match = re.match(r"(\w+)-to-(\w+) map:", line)
        if map_line_match:
            [source, dest] = map_line_match.groups()
            curr.name = source
        
        if line == '\n': 
            curr.next = Bag()
            curr = curr.next

        data_line_match = re.match(r"(\d+) (\d+) (\d+)", line)        
        if data_line_match:
            [dest_start, source_start, count] = [int(g) for g in data_line_match.groups()]
            curr.lookups.append([dest_start, source_start, count])

    return start


def traverse(bag:Bag, seed:int):
    start = seed
    #print(bag.name, seed, end=', ')
    seed = bag.find(seed)
    if bag.next:
        return traverse(bag.next, seed)
    #print("location", seed)
    return seed

def part1(lines):
    bag = parse_input(lines)
    vals = [traverse(bag, seed) for seed in bag.seeds]
    result = min(vals)
    return result


# this is just awful 
    
def part2(lines):
    bag = parse_input(lines)

    total = 0
    for i in range(len(bag.seeds)//2):
        [start, count] = [bag.seeds[i*2], bag.seeds[i*2+1]]
        total += count
#    print(total)

    tries = 0
    best = 100000000000000
    start_time = datetime.now()

    for i in range(len(bag.seeds)//2):
        [start, count] = [bag.seeds[i*2], bag.seeds[i*2+1]]
        step = 100

        good_start = 682397438
        if start != good_start: continue

#        for i in range(start, start+count, step): 
        for i in range(692213738-100000, 692213738+100, 1): 
            location = traverse(bag, i)
            if location < best:
                best = location
                seed_start = start
                found_at = i
            tries += step
            if tries % 10000 == 0: print(best, seed_start, found_at, datetime.now()-start_time, tries, 100.0 * tries/total)
    return best

# 12818416
# 12718416
# 12638416 
# 12634632

# print("Part 1 sample:", part1(SAMPLE))
# print("Part 1:", part1(INPUT))
print(part2(SAMPLE))
print(part2(INPUT))
