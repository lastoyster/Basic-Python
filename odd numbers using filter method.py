def oddval (x):
    return x% 2==1

odds=filter(oddval, range(1,30))
print(list(odds))