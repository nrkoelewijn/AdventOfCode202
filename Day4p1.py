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

# Investigate each document
for doc in documents:     
    d = []  
    # Create a reference fields list without country ID.
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    
    # Only if document has enough attributes, then try validate further.
    if len(doc) >= len(fields):
        # Read attributes of document.
        for attr in doc:
            # Add attribute type and value to list.
            d.append(attr.split(':')[0])
    
        # Check validity document and remove if invalid.
        for field in fields:
            if field not in d:
                valid -= 1
                break
    else:
        valid -= 1

# Print total number of valid documents.
print("Leftover valid documents:",valid)
