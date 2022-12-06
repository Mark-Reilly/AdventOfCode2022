test = 4

stack_4 = ['M', 'N', 'C', 'D', 'G', 'L', 'S', 'P']
stack_4.reverse()
print(stack_4)
test_stack_name = f'stack_{test}'

print(test_stack_name)
output = locals()[test_stack_name][1]

print(output)
locals()[test_stack_name].insert(0, 'TEN')
print(stack_4[0])


