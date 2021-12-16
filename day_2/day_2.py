import numpy as np

'''
Part 1
'''

# Load input
data = np.loadtxt('input.txt', dtype='str')
directions = data[:, 0]
values = np.array(data[:, 1], dtype='int')

# Find all forward, down and up positions
up_bool = directions=='up'
sum_up = values[up_bool].sum()
down_bool = directions=='down'
sum_down = values[down_bool].sum()
forward_bool = directions=='forward'
sum_forward = values[forward_bool].sum()

depth = sum_down-sum_up

print(f'Horizontal position is {sum_forward}, with depth {depth}.')
print(f'Depth times horizontal position is {depth*sum_forward}')

'''
Part 2
'''
# Calculate aim
delta_aim = np.zeros(len(values))
delta_aim[directions=='up'] = -values[up_bool]
delta_aim[directions=='down'] = values[down_bool]

# Aim at all given times
aim = np.cumsum(delta_aim)

# Change in depth
delta_depth = aim[forward_bool]*values[forward_bool]
total_depth = delta_depth.sum()
print(f'\nHorizontal position is still {sum_forward}, but with depth {total_depth}.')
print(f'Depth times horizontal position is now {total_depth*sum_forward}')

