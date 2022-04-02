#lamda function 

x = lambda a: a*a
print(x(5))
#25

def multiplier(n):
  return lambda x: x*n
  
mul_by_5 = multiplier(5)
print(mul_by_5(175))
#875