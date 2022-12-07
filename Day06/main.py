def part1(lines):
    print(lines)
    line = lines[0]
    for index in range(0, len(line)):
        actualPattern = line[index:index + 4]
        # print(actualPattern)
        fs = []
        res = 0
        nbOnes = 0
        for i in range(len(actualPattern)):
            # print(actualPattern[i])
            f = actualPattern.count(str(actualPattern[i]))
            fs.append(f)
        # print(f"fs: {fs}")
        for actualF in fs:
            if actualF == 1:
                nbOnes += 1
        if nbOnes == len(actualPattern):
            print(index + 4)
            break

def part2(lines):
    print(lines)
    line = lines[0]
    for index in range(0, len(line)):
        actualPattern = line[index:index + 14]
        # print(actualPattern)
        fs = []
        res = 0
        nbOnes = 0
        for i in range(len(actualPattern)):
            # print(actualPattern[i])
            f = actualPattern.count(str(actualPattern[i]))
            fs.append(f)
        # print(f"fs: {fs}")
        for actualF in fs:
            if actualF == 1:
                nbOnes += 1
        if nbOnes == len(actualPattern):
            print(index + 14)
            break

                

def main():
    file = open("Day06/input.txt", "r")
    lines = file.read()
    lines = lines.splitlines()
    part2(lines)

if __name__ == "__main__":
    main()