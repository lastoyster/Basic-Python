# Enter only integer values separated by space
# in a single line

l = input()
l = l.split()
l = [int(i) for i in l]
print('your list is', l)