# Split batch into document entries
with open('AoC/Day4p1input.txt') as file:
    batch = file.read().split("\n\n")
    file.close()

# Clean up any remaining newlines and split into fields on space.
documents = []
for doc in batch:
    newdoc = doc.replace("\n", " ")
    documents.append(newdoc.split(" "))
    
print("start size:",len(documents))

# Investigate each document and put in dictionary format.
for doc in documents:   
    #print("\n")
    docDict = {} 
    
    # Create a reference fields list without country ID.
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    
    # Only if document has enough attributes, then try validate further.
    if len(doc) >= len(fields)-1:
        #print("Try validate: \n",doc)
        # Read attributes of document.
        for attr in doc:
            # Add attribute type and value to document dictionary.
            docDict.update({attr.split(':')[0] : attr.split(':')[1]})
    
        # Check validity document and remove if invalid.
        for field in fields:
            if field not in docDict:
                #print("This field is missing:", field)
                documents.remove(doc)
                break
    else:
        documents.remove(doc)

# Print total number of valid documents.
print("Leftover valid documents:",len(documents))
