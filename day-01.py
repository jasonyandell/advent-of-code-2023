from aoc import read_lines
import re

part1Sample = read_lines("data/01-p1-sample.txt")
actualInput = read_lines("data/01.txt")
part2SampleInput = read_lines("data/01-p2-sample.txt")

def part1(lines:list):
    sum = 0
    for line in lines:
        digits = re.sub("[^0-9]", "", line)
        num = int(digits[0]+digits[-1])
        sum += num
    return sum

def part2(lines:list):
    digit_map = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    def getDigits(line):
        digits = []
        for i in range(len(line)):
            if line[i].isdigit():
                digits.append(int(line[i]))
            for word, num in digit_map.items():
                if line[i:].startswith(word):
                    digits.append(num)
        return digits

    sum = 0
    for line in lines:
        digits = getDigits(line)
        first = digits[0]
        last = digits[-1]
        num = first*10+last
        sum += num
    return sum

assert 142 == part1(part1Sample)
assert 54951 == part1(actualInput)
assert 281 == part2(part2SampleInput)
assert 55218 == part2(actualInput)
print("correct")
