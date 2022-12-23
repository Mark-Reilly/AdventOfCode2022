with open('test.txt', 'r') as f:
    data = [row.strip() for row in f.readlines()]
    print(data[0])

    ROWS = len(data)
    COLUMNS = len(data[0])

    # Testing how '[data[row][column]] works
    this_row = 2
    this_col = 1

    this_one = [data[this_row][this_col]]
    print(this_one)

    # Testing how the iteration works
    for row in range(1, ROWS - 1):
        for col in range(1, COLUMNS - 1):
            tree = data[row][col]
            print("This tree is:", tree)
            # Testing how the left/right/up/down lists work
            left = [data[row][col - i] for i in range(1, col + 1)]
            print(left)
