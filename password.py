def conv(x):
    if x==2055:
        return "WELCOME! Access granted"
    else:
        return "Access denied!\n Please enter again"
n = int (input("Enter password: "))
print(conv(n))