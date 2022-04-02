#Lists are mutable, meaning their elements can be changed unlike string or tuple.

# Correcting mistake values in a list
odd = [2,4,6,8]

#change the 1st item 
odd[0] = 1

print(odd)

#change the 2nd to 4th items
odd[1:4] = [3,5,7]

print(odd)