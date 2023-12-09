"""9"""

SAMPLE = [*open("data/09-sample.txt")]
INPUT = [*open("data/09.txt")]

def nonzero(nums:list[int]):
    for n in nums:
        if n != 0: 
            return True
    return False

def tree(nums:list[int], part2=False):
    diffs = [nums]

    curr = nums
    while nonzero(curr):
        diff_line = []
        for i in range(len(curr) - 1):
            diff_line.append(curr[i+1] - curr[i])
        diffs.append(diff_line)
        curr = diff_line
    
    if (part2):
        for d in diffs:
            d.reverse()
        
    diffs[-1].append(0)
    for i in range(len(diffs)-1, 0, -1):
        # new_val - prev_end = my_end
        # new_val = my_end + last
        new_val = diffs[i][-1] + diffs[i-1][-1]
        if (part2):
            # prev_end - new_val = my_end
            # new_val = prev_end - my_end
            new_val = diffs[i-1][-1] - diffs[i][-1]
        diffs[i-1].append(new_val)

    return diffs[0][-1]

def part1(lines):
    total = 0
    for line in lines:
        total += tree([*map(int, line.split())])
    return total

def part2(lines):
    total = 0
    for line in lines:
        total += tree([*map(int, line.split())], True)
    return total

print("Part 1 Sample", part1(SAMPLE))
print("Part 1", part1(INPUT))
print("Part 2 Sample", part2(SAMPLE))
print("Part 2", part2(INPUT))