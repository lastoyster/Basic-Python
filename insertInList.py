#we can insert one item at a desired location by using the method insert() 
# or insert multiple items by squeezing it into an empty slice of a list.

odd = [1,9]
odd.insert(1,3)

print(odd)

odd[2:2] = [5,7]

print(odd)