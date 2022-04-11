str= 'hello lovely friends'
longest = ''
length = 0
for i in str.split():
    if len(i) > length:
        longest = i
        length = len(longest)

print(longest, length)
