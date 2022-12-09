import string
total = 0

with open('input.txt', 'r') as f:
    for i in f:
        half = len(i) // 2
        set1 = set(i[:half])
        set2 = set(i[half:])

        # https://java2blog.com/find-common-elements-in-two-lists-python/
        common = set(set1).intersection(set2)
        common = (str(common))[2]

        if common in string.ascii_lowercase:
            total += string.ascii_lowercase.index(common) + 1
        if common in string.ascii_uppercase:
            total += string.ascii_uppercase.index(common) + 27

print(total)
