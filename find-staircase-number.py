#Write a program to accept an integer and output whether it's an upward/downward staircase number and print "Not staircase number" if it's not the case. A staircase number have the following pattern:-

✔️ Compose of at least 2 distinct digits (0-9)
✔️ Same digit must be grouped together and occur at least twice

Explanation: We need different digit to build the staircase step and if we plot the number as the y-value, we get a flat line with two or more occurences. So by connecting the lines we will get a staircase-like graph.

✔️ Upward if the unique digits are incerasing left-to-right
✔️ Downward if the unique digits are decreasing left-to-right

def isstaircase(number):
    number = str(number)
    digits = []
    for i in range(len(number)):
        try:
            if number[i] != number[i-1] and number[i] != number[i+1]:
                print("Not Staircase Number")
                return False
            else:
                if number[i] in digits:
                    continue
                else:
                    digits.append(number[i])
        except:
            if number[i] != number[i-1]:
                print("Not Staircase Number")
                return False
            else:
                continue
    if len(digits) <= 1:
        print("Not Staircase Number")
        return False

    sorteddigits = sorted(digits)
    revsorteddigits = sorted(digits, reverse=True)
    if sorteddigits == digits:
        print("Upward Staircase Number")
        return True
    elif revsorteddigits == digits:
        print("Downward Staircase Number")
        return True
    else:
        print("Defective Staircase Number")
        return True

print(isstaircase(int(input())))