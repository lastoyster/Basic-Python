a= [[0]*2]*3
print(a)
a[0][0] =5
print(a)
a[1][1] =2
print(a)

b =[5]*3
print(b)
b[0] =4
print(b)

#Elements of the outer list are pointers
#and can be changed to refer another list

a[0]= b
print(a)
b[0] = 9
print(a)