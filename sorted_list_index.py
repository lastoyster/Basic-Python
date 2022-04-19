
list = list(set([__import__('random').randint(1,100) for i in range(10)]))

print(f"unsorted list: {list}\n",*[f'element: {j},index: {str(list.index(j))}' for j in sorted(list)],sep='\n')
