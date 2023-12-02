from aoc import read_lines
import re

part1_sample = read_lines("data/01-p1-sample.txt")
actual_input = read_lines("data/01.txt")
part2_sample = read_lines("data/01-p2-sample.txt")

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

    def get_digits(line):
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
        digits = get_digits(line)
        num = digits[0]*10+digits[-1]
        sum += num
    return sum

assert 142 == part1(part1_sample)
assert 54951 == part1(actual_input)
assert 281 == part2(part2_sample)
assert 55218 == part2(actual_input)
print("correct")
