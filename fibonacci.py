
'''
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
££££££££££     Fibonacci Series  £££££££££££££££££
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

'''


Number = int(input("Please Enter the Fibonacci Numbers Range = "))
print("\n")
print("##########################################")
print("#####      Using While Loop       ######")
print("##########################################","\n")
First = 0
Second = 1
Sum = 0
i = 0
while(i <  Number):
    print(First, end = '  ')
    Sum = Sum + First
    Next = First + Second
    First = Second
    Second = Next
    i = i + 1
print("\nThe Sum of Fibonacci Series Numbers = %d" %Sum)
print("\n")
print("##########################################")
print("#####        Using For Loop         ######")
print("##########################################","\n")
First = 0
Second = 1
Sum = 0
for Num in range(0, Number):
    print(First, end = '  ')
    Sum = Sum + First
    Next = First + Second
    First = Second
    Second = Next
print("\nThe Sum of Fibonacci Series Numbers = %d" %Sum)