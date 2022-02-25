import numpy as np
import matplotlib.pyplot as plt
import sys
def arithmetic_sum(a1, a2):
    n = np.abs(a1-a2)
    return np.arange(1, n).sum()
    

'''
Part 1
'''

# Get input positions
crab_positions = np.loadtxt('input.txt', dtype='int', delimiter=',')

# Test all stop positions
stop_positions = np.arange(0, np.max(crab_positions)+1)
fuel_cost = [np.abs(crab_positions-stop).sum() for stop in stop_positions]

print(f'Minimal fuel cost is {np.min(fuel_cost)}')

'''
Part 2 - Calculate the arithmetic series instead
'''
# 2D array of number of steps to move each crab to a given position
steps = [np.abs(crab_positions - stop_position) for stop_position in stop_positions]

# Create dictionary with arithmetic sums
arithmetic_sums = {n_steps:np.arange(0, n_steps+1).sum() for n_steps in range(0, crab_positions.max()+1)}

# Calculate fuel costs
fuel_costs = np.zeros(crab_positions.max()+1)
for i, row in enumerate(steps):
    # Find number of occurrences of a given step length
    n_steps, n_occurrences = np.unique(row, return_counts=True)
    
    # Calculate fuel cost for moving crabs to position
    x = sum([arithmetic_sums[n_step]*n_occurrence for n_step, n_occurrence in zip(n_steps, n_occurrences)])
    fuel_costs[i] = x

print(f'Minimal fuel cost is {np.min(fuel_costs)}')
