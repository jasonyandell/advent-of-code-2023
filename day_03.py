SAMPLE = [*open("data/03-p1-sample.txt")]
DATA = [*open("data/03.txt")]

input = SAMPLE

def solution(data, is_part_one=True):
    grid = [list(line.strip()+'.') for line in data]

    width = len(grid[0])
    height = len(grid)

    def char_at(r,c): 
        if r in range(height) and c in range(width): 
            return grid[r][c]
        else: 
            return '.'

    def is_symbol(r,c): 
        return char_at(r,c) not in '0123456789.'

    def get_numbers_near(r,c):        
        numbers = []
        for cc in [c-1,c,c+1]:
            for rr in [r-1,r,r+1]:
                if char_at(rr,cc).isdigit():
                    start = cc
                    while (char_at(rr,start-1).isdigit()): start -= 1
                    number = ""
                    curr = start
                    while (char_at(rr,curr).isdigit()):
                        number += char_at(rr, curr)
                        grid[rr][curr] = '.'
                        curr += 1
                    numbers.append(int(number))
        return numbers

    all = []
    for c in range(width):
        for r in range(height):
            if (is_part_one):
                if is_symbol(r,c):
                    all.extend(get_numbers_near(r, c))
            else:
                if char_at(r,c) == '*':
                    numbers = get_numbers_near(r, c)
                    if len(numbers)==2: all.append(numbers[0]*numbers[1])
    return sum(all)



print(solution(SAMPLE))
print(solution(DATA))  # 532460 too high, as is 530460

print("Part 2")
print(solution(SAMPLE, False))
print(solution(DATA, False))  # 532460 too high, as is 530460