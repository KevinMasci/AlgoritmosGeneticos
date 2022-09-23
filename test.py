import random

lista1 = [9, 8, 2, 1, 7, 4, 5, 10, 6, 3]
lista2 = [9, 2, 3, 4, 5, 6, 7, 8, 1, 10]

lista = range(24)
padre1 = random.sample(lista, 24)
padre2 = random.sample(lista, 24)

def crossover(p1, p2):
    hijo1 = [-1]*24
    hijo2 = [-1]*24
    hijo1[0] = p1[0]
    hijo2[0] = p2[0]
    repite = False
    i = 0
    while repite == False:
        if p2[i] not in hijo1:
            hijo1[p1.index(p2[i])] = p2[i]
            i = p1.index(p2[i])
            print(i)
        else: repite = True
    for x in range(24):
        if hijo1[x] == -1:
            hijo1[x] = p2[x]
    repite = False
    i = 0
    while repite == False:
        if p1[i] not in hijo2:    
            hijo2[p2.index(p1[i])] = p1[i]
            i = p2.index(p1[i])
        else: repite = True
    for x in range(24):
        if hijo2[x] == -1:
            hijo2[x] = p1[x]
    return [hijo1, hijo2]

hijo1, hijo2 = crossover(padre1, padre2)
print('padres\n', padre1, '\n', padre2)
print('hijos')
print(hijo1)
if len(hijo1) != len(set(hijo1)):
    print('hay duplicado')
print(hijo2)
if len(hijo2) != len(set(hijo2)):
    print('hay duplicado')  

#i = random.randint(0,23)
#j = random.choice(list(range(1, i)) + list(range(i+1, 24)))
#
#print(i)
#print(j)
#print(list(range(1, i)))
#print(list(range(i+1, 24)))


#i = random.randint(0,9)
#j = random.choice(list(range(1, i)) + list(range(i+1, 10)))
##aux = lista1[i]
##lista1[i] = lista1[j]
##lista1[j] = aux
#lista1[i], lista1[j] = lista1[j], lista1[i]
#print(i)
#print(j)
#print(lista1)