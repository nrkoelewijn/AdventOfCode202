# See array as repeating in the x direction. Hashtags are trees, else is open space.
with open('AoC/Day3p1input.txt') as f:
    myList = [line.rstrip('\n') for line in f]
    
# Starting point in array.
pos = [0,0]
trees = 0

# Ride the defined slope along the array.
def rideSlope(pos):
    # Positive x is to the right.
    # Positive y is down.
    pos[0] += 3
    pos[1] += 1
    # Modulo to fake continuous grid of arrays in x direction.
    if pos[0] > (len(myList[0])-1):
        pos[0] %= (len(myList[0]))

# Continue sledding as long as bottom is not reached.
while pos[1] < len(myList):
    # Ride the slope.
    rideSlope(pos)
    #Check and tally if new location is a tree.
    if pos[1] < len(myList) and myList[pos[1]][pos[0]] == '#':
        trees += 1

print("Number of trees encountered:", trees)





