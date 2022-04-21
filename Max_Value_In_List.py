List = [66,67,64,37,96,64,18,86,32,98]
print(max(List))

Max = List[0]
for i in List:
  if(i >Max):
      Max = i
print(Max)

list = sorted(List, reverse=True)
print(list[0])