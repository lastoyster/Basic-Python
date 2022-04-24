def linear_search(a,key,size):
    flag = 0
    for i in range(size):
        if (a[i] == key):
            flag = 1
            pos =i +1
        if flag == 1:
            print("Number not found at",pos,"position")
        else:
            print("Number not found")
        a =[]
        size= int(input("Enter size of the list:"))
        print(size)
        for i in range(size):
            val = int (input("Enter number:"))
            print(val)
            a.append(val)
        key =int(input("Enter number to search"))
        print(key)
        linear_search (a,key,size)