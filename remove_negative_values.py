list = [11, -12, 13, -14]
i = 0
for i in range(len(list)):
    if list[i] < 0:
        del list[i]
    else:
        i = i + 1
    print(list)