import numpy as np

'''
Part 1
'''

# Load coordinates
C = np.loadtxt('input.txt', delimiter=',')

# x are columns, y are rows
X = np.array([C[:,0], C[:,2]], dtype='int')
Y = np.array([C[:,1], C[:,3]], dtype='int')

# Select coordinates where either x1=x2 or y1=y2
# vent_inds = np.where((X[0]==X[1]) | (Y[0]==Y[1]))

# x = np.array([X[0][vent_inds], X[1][vent_inds]], dtype='int')
# y = np.array([Y[0][vent_inds], Y[1][vent_inds]], dtype='int')
x = np.copy(X)
y = np.copy(Y)

# Map of vents
vents = np.zeros([int(y.max())+1, int(x.max())+1])

for x1, x2, y1, y2 in zip(x[0], x[1], y[0], y[1]):
    # Line along x-axis
    if x1==x2:
        y1_coord = np.copy(y1)
        y2_coord = np.copy(y2)
        if y1>y2: 
            y1_coord = np.copy(y2)
            y2_coord = np.copy(y1)
        
        vents[y1_coord:y2_coord+1, x1] += 1
    # Line along y-axis
    elif y1==y2:
        x1_coord = np.copy(x1)
        x2_coord = np.copy(x2)
        if x1>x2: 
            x1_coord = np.copy(x2)
            x2_coord = np.copy(x1)
        vents[y1, x1_coord:x2_coord+1] += 1
    # Diagonal line
    else:
        if x1>x2: 
            x_array = np.arange(x1, x2-1, -1)
        elif x1<x2:
            x_array = np.arange(x1, x2+1)
        
        if y1>y2: 
            y_array = np.arange(y1, y2-1, -1)
        elif y1<y2:
            y_array = np.arange(y1, y2+1)
        # Create array of coordinates
        # y_array = np.arange(y1_coord, y2_coord+1)
        # x_array = np.arange(x1_coord, x2_coord+1)
        # Add 1 to each coordinate point
        vents[y_array, x_array] += 1
            
        
# Calculate number of points where lines overlap
n_points = (vents>1).sum()
print(f'Lines cross at {n_points} points.')

'''
Part 2
'''

















