# https://www.youtube.com/watch?v=o6KVs1EgAYk

with open('input.txt', 'r') as f:
    data = [row.strip() for row in f.readlines()]

ROWS = len(data)
COLUMNS = len(data[0])

edges = (ROWS * 2) + ((COLUMNS - 2) * 2)
total = edges
scores = []

# Iterate through trees not on edges

for row in range(1, ROWS - 1):
    for col in range(1, COLUMNS - 1):
        tree = data[row][col]

        # Get all horizontal and vertical trees
        left = [data[row][col-i] for i in range(1, col+1)]
        right = [data[row][col+i] for i in range(1, COLUMNS - col)]
        up = [data[row-i][col] for i in range(1, row+1)]
        down = [data[row+i][col] for i in range(1, ROWS - row)]

        # === PART 1 ===
        # Can the current tree be seen from outside the forest?
        # It can be seen if none of the trees up/down/left/right are greater or equal

        # Check if tallest tree on all sides blocks our view
        if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
            total += 1

        # === PART 2 ===
        # How many trees can be seen by looking up/down/left/right from current tree
        # All trees until equal or greater than current tree can be seen

        score = 1
        for lst in (left, right, up, down):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                elif lst[i] == tree:
                    tracker += 1
                    break
                else:
                    break
            score *= tracker
        scores.append(score)


print("Answer to part 1:", total)
print("Answer to part 2:", max(scores))
