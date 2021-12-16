import numpy as np


'''
Part 1
'''
# Load input
data = np.loadtxt('input.txt')

# Find differences
diff = np.diff(data)
n_increase = (diff>0).sum()
print(f'The number increased {n_increase} times.')

def sliding_sum(data, n):
    d = np.zeros(len(data)-n+1)
    for i in range(n-1):
        d += data[i:i-n+1]
    # Add final value
    return d+data[n-1:]
    
'''
Part 2
'''
data_summed = sliding_sum(data, 3)
diff_slide = np.diff(data_summed)
n_slide = (diff_slide>0).sum()
print(f'The sliding number increased {n_slide} times.')


