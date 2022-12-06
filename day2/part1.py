score = 0

elf_rock = 'A'
elf_paper = 'B'
elf_scissors = 'C'
me_rock = 'X'
me_paper = 'Y'
me_scissors = 'Z'

with open('input.txt', 'r') as f:
    for i in f:
        [elf, me] = i.strip().split(' ')
        if me == me_rock:
            score += 1
            if elf == elf_rock:
                score += 3
            elif elf == elf_scissors:
                score += 6
        if me == me_paper:
            score += 2
            if elf == elf_rock:
                score += 6
            elif elf == elf_paper:
                score += 3
        if me == me_scissors:
            score += 3
            if elf == elf_paper:
                score += 6
            elif elf == elf_scissors:
                score += 3

    print(score)
