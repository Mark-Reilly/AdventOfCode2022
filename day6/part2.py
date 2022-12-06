with open('input.txt', 'r') as f:
    data = f.read()
    start_character = 0
    while start_character < len(data):
        this_window = data[start_character:(start_character+14)]
        print(this_window)
        # https://stackoverflow.com/questions/32090058/testing-whether-a-string-has-repeated-characters
        if len(set(this_window)) == len(this_window):
            print(f'Answer: {start_character+14}')
            break
        start_character += 1
