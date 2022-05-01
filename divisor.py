from cgi import print_directory


num = int(input())
for r in range(1, num+1):
    if num % r == 0:
        print(r)