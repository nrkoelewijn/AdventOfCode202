# Import regex module
import re

# Function to check the validity of the document values.
def checkBYR(byr):
    if int(byr) in range (1920,2002):
        return 1
    else:
        return 0
    
def checkIYR(iyr):
    if int(iyr) in range (2010,2020):
        return 1
    else:
        return 0
    
def checkEYR(eyr):
    if int(eyr) in range (2020,2030):
        return 1
    else:
        return 0
    
def checkHGT(hgt):
    cm = re.match(r'(\d+)[cm]', hgt)
    inch = re.match(r'(\d+)[in]', hgt)
    if cm:
        if int(cm[1]) in range (150,193):
            return 1
        else:
            return 0
    elif inch:
        if int(inch[1]) in range (59,76):
            return 1
        else:
            return 0
    else:
        return 0
    
def checkHCL(hcl):
    color = re.match(r'#[a-z0-9]{6}$', hcl)
    if color:
        return 1
    else:
        return 0
    
def checkECL(ecl):
    list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl in list:
        return 1
    else:
        return 0
    
def checkPID(pid):
    id = re.match(r'[\d]{9}', pid)
    if id:
        return 1
    else:
        return 0

# Split batch into document entries
with open('AoC/Day4p1input.txt') as file:
    batch = file.read().split("\n\n")
    file.close()

# Clean up any remaining newlines and split into fields on space.
documents = []
for doc in batch:
    newdoc = doc.replace("\n", " ")
    documents.append(newdoc.split(" "))
    
valid = len(documents)

# Investigate each document and put in dictionary format.
for doc in documents:     
    attr = {}
    # Create a reference fields dictionary with corresponding check functions, without country ID.
    fields = {"byr":checkBYR,"iyr":checkIYR,"eyr":checkEYR,"hgt":checkHGT,"hcl":checkHCL,"ecl":checkECL,"pid":checkPID}
    
    # Only if document has enough attributes, then try validate further.
    if len(doc) >= len(fields):
        # Read attributes of document.
        for d in doc:
            # Add attribute type and value to dictionary.
            attr.update({d.split(':')[0] : d.split(':')[1]})

        # Check validity document and remove if invalid.
        for field in fields:
            # Check if document has all required fields.
            if field not in attr:
                valid -= 1
                break
            else:
                # Check values by variable function call with value of attribute and function dependent on attribute type.
                if not fields.get(field)(attr.get(field)):
                # Check value validity.
                    valid -= 1
                    break
    else:
        valid -= 1

# Print total number of valid documents.
print("Leftover valid documents:",valid)