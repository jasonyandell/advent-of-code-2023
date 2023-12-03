SAMPLE = [*open("data/03-p1-sample2.txt")]
PART1 = [*open("data/03.txt")]

input = SAMPLE

def part1(data):
    grid = [list(line.strip()+'.') for line in data]

    width = len(grid[0])
    height = len(grid)

    def is_symbol_near(r:int,c:int,grid:list[list[str]]):
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                rpos = r+dr
                cpos = c+dc
                try:
                    if grid[rpos][cpos] != "." and not grid[rpos][cpos].isdigit():
                        return True
                except IndexError:
                    continue
        return False
    
    numbers = []

    for r in range(height):
        current = ""
        found_symbol = False

        for c in range(width):
            if is_symbol_near(r, c, grid):
                found_symbol = True
            if grid[r][c].isdigit():
                current += grid[r][c]
            else:
                if len(current)>0 and found_symbol:
#                    if int(current)>1000:
                    numbers.append(int(current))
                current = ""
                found_symbol = False
    return sum(numbers)

print(part1(SAMPLE))
print(part1(PART1))  # 532460 too high, as is 530460