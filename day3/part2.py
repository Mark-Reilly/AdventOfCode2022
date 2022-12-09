import string
total = 0

with open('input.txt', 'r') as f:
    data = f.read().strip().splitlines()
    i = 0
    while i < len(data):
        this_set = data[i:i+3]
        elf_1 = set(this_set[0])
        elf_2 = set(this_set[1])
        elf_3 = set(this_set[2])

        common = elf_1.intersection(elf_2).intersection(elf_3)
        common = (str(common))[2]

        if common in string.ascii_lowercase:
            total += string.ascii_lowercase.index(common) + 1
        if common in string.ascii_uppercase:
            total += string.ascii_uppercase.index(common) + 27
        i += 3

print(total)
