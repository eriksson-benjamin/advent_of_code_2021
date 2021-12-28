import numpy as np

class LanternFish:
    def __init__(self, input_ages):
        # Initialize input ages for lantern fish
        n_fish = np.zeros(9)
        for age in range(0, 9):
            n_fish[age] = (input_ages==age).sum()
        # Number of fish in each age group
        self.ages = n_fish

    def advance_day(self):
        new_list = np.zeros(9)
        # Move fish down one age group
        for i in range(1,9):
            new_list[i-1] = self.ages[i]
        
        # Move fish at age 0 to age 6
        new_list[6] += self.ages[0]
        
        # Add new fish to age 8
        new_list[-1] += self.ages[0]
        
        self.ages = np.copy(new_list)
        
            
ages = np.loadtxt('input.txt', dtype='int', delimiter=',')

# Create fish object
fish = LanternFish(ages)

# Advance day
for i in range(256):
    fish.advance_day()
    print(f'Day {i+1}: {fish.ages.sum()} fish in the sea.')
print(f'There are {fish.ages.sum()} fish after 80 days.')