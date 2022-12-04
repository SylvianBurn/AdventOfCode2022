rock, paper, scissors = 1, 2, 3
lost, draw, won = 0, 3, 6


def part1(lines, map):
    total = 0
    for line in lines:
        lenLine = int(len(line) / 2)
        # print(lenLine)
        first_comp = line[:lenLine]
        second_comp = line[lenLine:]
        # print(f"line: {line} 1:{first_comp} 2:{second_comp}")
        a = list(set(first_comp) & set(second_comp))
        # a.sort()
        # print(a)
        total += map[a[0]]
    print(total)

def part2(lines, map):
    total = 0
    for i in range(0, len(lines), 3):
        a = list(set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2]))
        # a.sort()
        # print(a)
        total += map[a[0]]
    print(total)

def buildPriorities():
    map = {}
    base = 1
    for letter in range(97, 123):
        map[chr(letter)] = base
        base += 1
    for letter in range(65, 91):
        map[chr(letter)] = base
        base += 1
    return map

def main():
    file = open("Day03/input.txt", "r")
    lines = file.read()
    lines = lines.splitlines()
    map = buildPriorities()
    # print(map)
    part2(lines, map)


if __name__ == "__main__":
    main()