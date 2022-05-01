
lista = ['AABBCCDCDAABB']

new_lista = lista[0][0]

for i in range(1, len(lista[0])):
    if lista[0][i] != lista[0][i-1]:
        new_lista += lista[0][i]

print(new_lista)