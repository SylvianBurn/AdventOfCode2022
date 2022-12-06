
def part1(lines):
    total = 0
    for line in lines:
        pairs = line.split(",")
        first_pair = pairs[0].split("-")
        second_pair = pairs[1].split("-")
        s1, b1, s2, b2 = first_pair[0], first_pair[1], second_pair[0], second_pair[1]
        # print(first_pair, second_pair)
        # first_list = range(int(s1), int(b1))
        # second_list = range(int(s2), int(b2))
        # if ((s1 >= s2 and s1 <= b2 and b1 <= b2 and b1 >= s2)
        # or (s2 >= s1 and s2 <= b1 and b2 <= b1 and b2 >= s1)):
        #     total += 1
        if int(s1) >= int(s2) and int(b1) <= int(b2):
            total += 1
        elif int(s2) >= int(s1) and int(b2) <= int(b1):
            total += 1
    print(total)
    # solution is between 517 and 570 for the input file

def part2(lines):
    total = 0
    for line in lines:
        pairs = line.split(",")
        first_pair = pairs[0].split("-")
        second_pair = pairs[1].split("-")
        s1, b1, s2, b2 = first_pair[0], first_pair[1], second_pair[0], second_pair[1]
        # print(first_pair, second_pair)
        first_list = range(int(s1), int(b1) + 1)
        second_list = range(int(s2), int(b2) + 1)
        # inter = set(first_list).intersection(second_list)
        # inter2 = set(second_list).intersection(first_list)
        # if len(inter) != 0 or len(inter2) != 0:
        #     total += 1
        # inter = [i for i in first_list if i in second_list]
        inter = set(first_list) & set(second_list)
        # print(inter)
        if len(inter) != 0:
            total += 1
    print(total)
        

def main():
    file = open("Day04/input.txt", "r")
    lines = file.read()
    lines = lines.splitlines()
    part2(lines)


if __name__ == "__main__":
    main()