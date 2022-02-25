import numpy as np



'''
Part 1
'''
# Get input
inp = np.loadtxt('input.txt', dtype='str')

# Wire input signals
wire_signals = inp[:, 0:10]
# Display output segments
disp_signals = inp[:, 11:]

'''
Count all occurrences of strings in the display signals with length 2 (a one), 
3 (a seven), 4 (a four) and 7 (an eight)
'''
disp_lengths = [len(disp_signal) for disp_signal in disp_signals.flatten()]
number, frequency = np.unique(disp_lengths, return_counts=True)

print(f"Number of ones, fours, sevens and eights: {frequency[0]+frequency[1]+frequency[2]+frequency[5]}")
