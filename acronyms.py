p = str(input("Enter a Phrase: "))
k = p.split()
a = " "
for i in k:
    a = a+str(i[0]).upper()
print(p)
print("Acronyms of your entered phase is :", str(a))