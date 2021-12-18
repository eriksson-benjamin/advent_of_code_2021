import numpy as np

def binary_to_decimal(bits):
    flipped = np.flip(bits)
    dec = 0
    for i, bit in enumerate(flipped):
        dec += 2**i*bit
    return dec

# Loop over columns
def find_rating(data, mode):
    column = data[:, 0]
    to_keep = np.copy(data)
    i = 1
    while len(to_keep)>1:
        # Find the most common number in the column
        if column.sum()>=len(column)/2: most_common = 1
        else: most_common = 0
        
        # Get indices for the corresponding rows
        if mode=='oxygen': args = column==most_common
        elif mode=='C02':  args = column!=most_common
        
        # Keep the given rows
        to_keep = to_keep[args, :]
        
        # Select next column
        column = to_keep[:, i]
        i += 1
    return to_keep[0]

'''
Part 1
'''

with open('input.txt') as handle:
    inp = handle.read().splitlines()
# Put each bit in array
data = np.array([list(d) for d in inp], dtype='int')

# Sum columns
col_sum = np.sum(data, axis=0)

# Find columns larger than number of rows
gamma_bool = col_sum>(len(data)/2)
gamma_rate = [1 if gb else 0 for gb in gamma_bool]
epsilon_rate = [0 if gb else 1 for gb in gamma_bool]

# Convert to decimal
g_rate = binary_to_decimal(gamma_rate)
e_rate = binary_to_decimal(epsilon_rate)
p_consumption = g_rate*e_rate
print(f'Power consumption is {p_consumption}')

'''
Part 2
'''
oxygen_rating = binary_to_decimal(find_rating(data, 'oxygen'))
c02_rating = binary_to_decimal(find_rating(data, 'C02'))
print(f'Life support rating is {oxygen_rating*c02_rating}')









