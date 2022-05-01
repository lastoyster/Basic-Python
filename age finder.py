import  calendar
print('Enter your birth year:')
a = int(input())
age = 2022-a
print('Your age in 2022 is',age)
print('_'*40)
if a<1 or a > 9999:
    print('Invalid input')
else:
    for b in range(12):
        print(calendar.month(a, b+1))
        
print('Thanks for your info')