import timeit

avg = max = cur = 0
min = 100

for i in range(100):
    cur = timeit.timeit(str(2**1000))
    if cur <min: min = cur
    if cur > max: max = cur
    avg += cur

    print ('Min: {0:2f}\nAvg:{1:2f}\nMax: {2:2f}'.format(min. avg/100, max))
   