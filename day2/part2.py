score = 0

elf_rock = 'A'
elf_paper = 'B'
elf_scissors = 'C'
lose = 'X'
draw = 'Y'
win = 'Z'

with open('input.txt', 'r') as f:
    for i in f:
        [elf, outcome] = i.strip().split(' ')
        if elf == elf_rock:
            if outcome == lose:
                score += 3
            elif outcome == draw:
                score += 4
            else:
                score += 8
        elif elf == elf_paper:
            if outcome == lose:
                score += 1
            elif outcome == draw:
                score += 5
            else:
                score += 9
        elif elf == elf_scissors:
            if outcome == lose:
                score += 2
            elif outcome == draw:
                score += 6
            else:
                score += 7

    print(score)
