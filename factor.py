num = int(input("Enter the Number "))
mid = num//2
print("The Divisors Of ", num, "Are:")
for a in range(2, mid+1):
    if num%a == 0:
        print('\n', a,end=' ')
print("\n_END_")