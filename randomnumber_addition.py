import random

print('Random number between 1 to 100')
print('Enter the random numbers you want')
x = int(input())
#empty values that will be used later
a = []
b = 0
d = []

for i in range(101):
    a.append(i)
    
    for i in range(x):
        c = random.choice(a)
        d.append(c)
        b += c

        print('Your random numbers are', d)
        print('The total of random numbers are',b)
