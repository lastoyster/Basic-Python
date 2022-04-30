def evenVal (x):
    return x%2== 0
    
evens = filter(evenVal, range(9,50))
print(list(evens))