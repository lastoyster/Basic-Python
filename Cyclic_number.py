
def numberOfPossiblities(number):    
    li = []
    for index in range(len(number)):
        li += [number[index:] + number [:index]]
        return li

numbers_list = [
            "142857",
            "980815"
        ]

counter = 0
for numsstr in numbers_list:
    for mults in range(1,len(numsstr)+1):
        multans = int(numsstr) *mults
        possible = numberOfPossiblities(numsstr)
        if not str(multans) in possible:
            counter = 1
            break
    if counter:
        print (numsstr ,"is not a cycle")

        counter = 0
    else:
        print (numsstr, "is a cyclic")