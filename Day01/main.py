def main():
    file = open("input.txt", "r")
    lines = file.read()
    lines = lines.splitlines()
    # print(lines)
    elves = []
    elf = 0
    for line in lines:
        if line == "":
            elves.append(elf)
            elf = 0
            continue
        else:
            elf += int(line)
    # print(elves)
    part2(elves)

def part1(elves):
    # First part solution printed below
    print(max(elves))

def part2(elves):
    # sorted(elves)
    elves.sort()
    print(elves)
    l = len(elves) - 1
    threeHighest = elves[l] + elves[l - 1] + elves[l - 2]
    print(threeHighest)



if __name__ == "__main__":
    main()