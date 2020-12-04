
with open('AoC/Day2p1input.txt') as f:
    myList = [line.rstrip('\n') for line in f]

# Importeer regex module.
import re

# Pattern is defined as raw string by prepending with r
# Result will have 4 subgroups that can be called with .group(i).
pattern = r'(\d+)-(\d+)\s(\w+):\s(\w+)'
valids = 0

for txt in myList:
    match = re.search(pattern, txt)

    if match:
        # Check if at position group(1) XOR group(2) in the group(4) a char defined in group(3) exists
        found = 0
        if str(match.group(4))[int(match.group(1)) - 1] == match.group(3):
            found += 1
        if str(match.group(4))[int(match.group(2)) - 1] == match.group(3):
            found += 1
        if found == 1:
            valids += 1
    else:
        print("pattern not found")
    
print("nr, of valid passwords:",valids)