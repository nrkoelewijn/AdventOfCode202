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
        # Count occurunces of char in password
        #print(txt)
        #print(match.group(1))
        #print(match.group(2))
        #print(match.group(3))
        #print(match.group(4))
        counter = match.group(4).count(match.group(3))
        #print("counter:", counter)
        # Check if this amount is in the stated allowed range of occurences
        if counter >= int(match.group(1)) and counter <= int(match.group(2)):
            valids += 1
            #print("nr. of valids now:", valids)
        #print("-------------")
    else:
        print("pattern not found")
    
print("nr, of valid passwords:",valids)