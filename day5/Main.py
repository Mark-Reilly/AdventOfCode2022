# Initializing stack lists
stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9 = \
    [], [], [], [], [], [], [], [], []

# Populating the stacks
with open('input.txt', 'r') as f:
    for i in f:
        if i[1] == '1':
            break
        stack_1.append(i[1])
        stack_2.append(i[5])
        stack_3.append(i[9])
        stack_4.append(i[13])
        stack_5.append(i[17])
        stack_6.append(i[21])
        stack_7.append(i[25])
        stack_8.append(i[29])
        stack_9.append(i[33])


def clean_list(list_name):
    """Remove blanks after initializing the stacks"""
    while list_name[0] == " ":
        del list_name[0]


clean_list(stack_1)
clean_list(stack_2)
clean_list(stack_3)
clean_list(stack_4)
clean_list(stack_5)
clean_list(stack_6)
clean_list(stack_7)
clean_list(stack_8)
clean_list(stack_9)


def move_crates(quantity, source_stack_number, destination_stack_number):
    """Function to move the crates"""
    source_stack_name = f'stack_{source_stack_number}'
    destination_stack_name = f'stack_{destination_stack_number}'
    while quantity > 0:
        crate_to_move = globals()[source_stack_name][0]
        globals()[destination_stack_name].insert(0, crate_to_move)
        del globals()[source_stack_name][0]
        quantity -= 1


def move_stacked(quantity, source_stack_number, destination_stack_number):
    """Function to model 9001 mover. Move in the same order, rather than one at a time"""
    print(f' Quantity: {quantity}, Source: {source_stack_number}, Destination: {destination_stack_number}')
    source_stack_name = f'stack_{source_stack_number}'
    print(f'Current source list: {globals()[source_stack_name]}')
    destination_stack_name = f'stack_{destination_stack_number}'
    moving_list = []
    while quantity > 0:
        crate_to_move = globals()[source_stack_name][0]
        moving_list.append(crate_to_move)
        del globals()[source_stack_name][0]
        quantity -= 1
    print(f'Crates to be moved: {moving_list}')
    moving_list.reverse()
    for crate in moving_list:
        globals()[destination_stack_name].insert(0, crate)
    print(f'Destination after move: {globals()[destination_stack_name]}')


# Solution to part 1
# with open('moves.txt', 'r') as f:
#    for i in f:
#        numbers = [int(new_string) for new_string in str.split(i) if new_string.isdigit()]
#        this_quantity, this_source, this_destination = numbers[0], numbers[1], numbers[2]
#        move_crates(this_quantity, this_source, this_destination)


# Solution to part 2
with open('moves.txt', 'r') as f:
    for i in f:
        numbers = [int(new_string) for new_string in str.split(i) if new_string.isdigit()]
        this_quantity, this_source, this_destination = numbers[0], numbers[1], numbers[2]
        move_stacked(this_quantity, this_source, this_destination)


print(stack_1[0])
print(stack_2[0])
print(stack_3[0])
print(stack_4[0])
print(stack_5[0])
print(stack_6[0])
print(stack_7[0])
print(stack_8[0])
print(stack_9[0])
