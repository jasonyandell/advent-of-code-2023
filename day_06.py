
SAMPLE = [*open("data/06-sample.txt")]
INPUT = [*open("data/06.txt")]

def race(races):
    wins = []
    for time, record in races:
        win_count = 0
        for hold in range(time):
            distance = hold * (time - hold)
            if distance > record:
                win_count += 1
        wins.append(win_count)
    
    product = 1
    for w in wins: product *= w
    return product


def part1(lines):
    times = [int(s) for s in lines[0].split()[1:]]
    records = [int(s) for s in lines[1].split()[1:]]
    races = [*zip(times, records)]
    return race(races)
    
def part2(lines):
    def nums(line):
        [word,num_str] = line.split(':')
        num_str = num_str.replace(' ', '')
        return int(num_str)
    races = [(nums(lines[0]), nums(lines[1]))]
    return race(races)


print("Part 1 sample", part1(SAMPLE))
print("Part 1", part1(INPUT))
print("Part 2 sample", part2(SAMPLE))
print("Part 2", part2(INPUT))