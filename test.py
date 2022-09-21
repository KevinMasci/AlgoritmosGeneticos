import random

lista1 = [9, 8, 2, 1, 7, 4, 5, 10, 6, 3]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def crossover(p1, p2):
    hijo1 = [0]*10
    hijo2 = [0]*10
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
    for x in range(10):
        if hijo1[x] == 0:
            hijo1[x] = p2[x]
    repite = False
    i = 0
    while repite == False:
        if p1[i] not in hijo2:    
            hijo2[p2.index(p1[i])] = p1[i]
            i = p2.index(p1[i])
        else: repite = True
    for x in range(10):
        if hijo2[x] == 0:
            hijo2[x] = p1[x]
    return [hijo1, hijo2]

#hijo1, hijo2 = crossover(lista1, lista2)

i = random.randint(0,23)
j = random.choice(list(range(1, i)) + list(range(i+1, 24)))

print(i)
print(j)
print(list(range(1, i)))
print(list(range(i+1, 24)))