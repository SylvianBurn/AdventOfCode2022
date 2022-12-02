rock, paper, scissors = 1, 2, 3
lost, draw, won = 0, 3, 6


def part1(lines):
    myCombinations = {
        "A": "rock",
        "X": "rock",
        "B": "paper",
        "Y": "paper",
        "C": "scissors",
        "Z": "scissors"
    }
    total = 0
    # print(lines)
    for line in lines:
        pair = line.split(" ")
        if myCombinations[pair[0]] == "rock":
            if myCombinations[pair[1]] == "rock":
                total += rock + draw
            elif myCombinations[pair[1]] == "paper":
                total += paper + won
            elif myCombinations[pair[1]] == "scissors":
                total += scissors + lost
        elif myCombinations[pair[0]] == "paper":
            if myCombinations[pair[1]] == "rock":
                total += rock + lost
            elif myCombinations[pair[1]] == "paper":
                total += paper + draw
            elif myCombinations[pair[1]] == "scissors":
                total += scissors + won
        elif myCombinations[pair[0]] == "scissors":
            if myCombinations[pair[1]] == "rock":
                total += rock + won
            elif myCombinations[pair[1]] == "paper":
                total += paper + lost
            elif myCombinations[pair[1]] == "scissors":
                total += scissors + draw
    print(total)

def part2(lines):
    myCombinations = {
        "A": "rock",
        "X": "lose",
        "B": "paper",
        "Y": "draw",
        "C": "scissors",
        "Z": "win"
    }
    total = 0
    # print(lines)
    for line in lines:
        pair = line.split(" ")
        if myCombinations[pair[0]] == "rock":
            if myCombinations[pair[1]] == "draw":
                total += rock + draw
            elif myCombinations[pair[1]] == "win":
                total += paper + won
            elif myCombinations[pair[1]] == "lose":
                total += scissors + lost
        elif myCombinations[pair[0]] == "paper":
            if myCombinations[pair[1]] == "lose":
                total += rock + lost
            elif myCombinations[pair[1]] == "draw":
                total += paper + draw
            elif myCombinations[pair[1]] == "win":
                total += scissors + won
        elif myCombinations[pair[0]] == "scissors":
            if myCombinations[pair[1]] == "win":
                total += rock + won
            elif myCombinations[pair[1]] == "lose":
                total += paper + lost
            elif myCombinations[pair[1]] == "draw":
                total += scissors + draw
    print(total)

def main():
    file = open("Day02/input.txt", "r")
    lines = file.read()
    lines = lines.splitlines()
    part2(lines)


if __name__ == "__main__":
    main()