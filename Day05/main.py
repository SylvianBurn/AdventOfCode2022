from queue import Queue

# def buildStack(queue):
#     stack = []
#     for q in queue:
#         for i in range()

# [N]         [C]     [Z]            
# [Q] [G]     [V]     [S]         [V]
# [L] [C]     [M]     [T]     [W] [L]
# [S] [H]     [L]     [C] [D] [H] [S]
# [C] [V] [F] [D]     [D] [B] [Q] [F]
# [Z] [T] [Z] [T] [C] [J] [G] [S] [Q]
# [P] [P] [C] [W] [W] [F] [W] [J] [C]
# [T] [L] [D] [G] [P] [P] [V] [N] [R]
#  1   2   3   4   5   6   7   8   9 


def part1(lines, Q):
    for q in Q:
        print(q)
    # print(lines[0].split(" "))
    for line in lines:
        tab = line.split(" ")
        nb = int(tab[1])
        nbFrom = int(tab[3])
        nbTo = int(tab[5])
        # print(line)
        # print(f"move {nb} from {nbFrom} to {nbTo}")
        for i in range(nb):
            if len(Q[nbFrom - 1]) != 0:
                tmp = Q[nbFrom - 1].pop(0)
                Q[nbTo - 1].insert(0, tmp)
    print("")
    for queue in Q:
        print(queue[0], end="")

def part2(lines, Q):
    for q in Q:
        print(q)
    # print(lines[0].split(" "))
    for line in lines:
        tab = line.split(" ")
        nb = int(tab[1])
        nbFrom = int(tab[3])
        nbTo = int(tab[5])
        # print(line)
        # print(f"move {nb} from {nbFrom} to {nbTo}")
        tmpList = []
        for i in range(nb):
            tmp = Q[nbFrom - 1].pop(0)
            tmpList.insert(0, tmp)
        for i in range(len(tmpList)):
            Q[nbTo - 1].insert(0, tmpList[i])
    print("")
    for queue in Q:
        print(queue[0], end="")

def main():
    Q = [[ "N", "Q", "L", "S", "C", "Z", "P", "T"],
    [ "G", "C", "H", "V", "T", "P", "L"],
    [ "F", "Z", "C", "D"],
    [ "C", "V", "M", "L", "D", "T", "W", "G"],
    [ "C", "W", "P"],
    [ "Z", "S", "T", "C", "D", "J", "F", "P"],
    [ "D", "B", "G", "W", "V"],
    [ "W", "H", "Q", "S", "J", "N"],
    [ "V", "L", "S", "F", "Q", "C", "R"]]

    Qexemple = [[ "N", "Z"],
    [ "D", "C", "M"],
    ["P"]]

    # exStack = buildStack(Qexemple)

    exemple = [
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2"
    ]
    file = open("Day05/input.txt", "r")
    lines = file.read()
    lines = lines.splitlines()
    part2(lines, Q)

if __name__ == "__main__":
    main()