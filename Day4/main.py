count = 0
count_2 = 0

with open('input.txt', 'r') as f:
    for i in f:
        elf_1, elf_2 = i.split(',')
        elf_1_start, elf_1_finish = elf_1.split('-')
        elf_2_start, elf_2_finish = elf_2.split('-')
        elf_1_start, elf_1_finish = int(elf_1_start), int(elf_1_finish)
        elf_2_start, elf_2_finish = int(elf_2_start), int(elf_2_finish)

        if elf_2_start >= elf_1_start and elf_2_start <= elf_1_finish \
                and elf_2_finish >= elf_1_start and elf_2_finish <= elf_1_finish:
            count += 1
        elif elf_1_start >= elf_2_start and elf_1_start <= elf_2_finish \
                and elf_1_finish >= elf_2_start and elf_1_finish <= elf_2_finish:
            count += 1

        # Part 2
        if elf_2_start >= elf_1_start and elf_2_start <= elf_1_finish:
            count_2 += 1
        elif elf_1_start >= elf_2_start and elf_1_start <= elf_2_finish:
            count_2 += 1

print(count)
print(count_2)
