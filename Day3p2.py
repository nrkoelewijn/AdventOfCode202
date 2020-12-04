
# See array as repeating in the x direction. Hashtags are trees, else is open space.
with open('AoC/Day3p1input.txt') as f:
    myList = [line.rstrip('\n') for line in f]

# Define all the slopes.
slopes = ([1,1],[3,1],[5,1],[7,1],[1,2])

# Ride the defined slope along the array.
def rideSlope(i,pos):
    # Positive x is to the right.
    # Positive y is down.
    pos[0] += i[0]
    pos[1] += i[1]
    # Modulo to fake continuous grid of arrays in x direction.
    if pos[0] > (len(myList[0])-1):
        pos[0] %= (len(myList[0]))

product = 1

# For each slope tally sum of trees.
for i in slopes:
    # Starting point in array.
    pos = [0,0]
    trees = 0

    # Continue sledding as long as bottom is not reached.
    while pos[1] < len(myList):
        # Ride the slope.
        rideSlope(i,pos)
        #Check and tally if new location is a tree.
        if pos[1] < len(myList) and myList[pos[1]][pos[0]] == '#':
            trees += 1
    
    product *= trees

print("Product of trees encountered:", product)
    