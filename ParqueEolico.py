from math import log, sqrt
import numpy as np
import random
import copy

anchoCromosoma = 10
largoCromosoma = 10
aerogenMax = 25
cantCromosomas = 50
prob_cross = 0.85
prob_mut = 0.05
parque = []
arr_potencias = []
arr_fitness = []
pot_total_poblacion = 0
tam_celda = 100
velm = 7.5
k = 1/(2 * log(100/0.694))
diam_rotor = 83
rango_estela = 18 * diam_rotor

##DIRECCION DEL VIENTO
# => [0,0,0,0,0,0,0,0,0,0]
# => [0,0,0,0,0,0,0,0,0,0]
# => [0,0,0,0,0,0,0,0,0,0]
# => [0,0,0,0,0,0,0,0,0,0]
# => [0,0,0,0,0,0,0,0,0,0]
# => [0,0,0,0,0,0,0,0,0,0]
# => [0,0,0,0,0,0,0,0,0,0]
# => [0,0,0,0,0,0,0,0,0,0]
# => [0,0,0,0,0,0,0,0,0,0]
# => [0,0,0,0,0,0,0,0,0,0]


#Velocidad minima para el funcionamiento de un aerogenerador 3 m/s


def crearParque():
    parque = np.zeros((anchoCromosoma, largoCromosoma), dtype=int)
    for x in range(aerogenMax):
        n = random.randint(0,1)
        if n == 1:
            i = random.randint(0,largoCromosoma-1)
            j = random.randint(0,anchoCromosoma-1)
            parque[i,j] = 1
    return parque

def crearPoblacionInicial(cantCromosomas):
    poblacion = []
    while len(poblacion) < cantCromosomas:
        poblacion.append(crearParque())
    return poblacion

def calcularPotencia(parque, velm):
    Ptot = 0
    columna_anterior = 0
    for fila in range(10):
        primer_gen = False
        dist = 0
        for columna in range(10):
            if parque[fila, columna] == 1:
                if primer_gen == False:
                    vel = velm
                    primer_gen = True
                    pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
                else:
                    dist = (columna - columna_anterior) * tam_celda
                    if dist <= rango_estela:
                        vel = vel * (1-(1-sqrt(1-0.889))/(k * dist/41.5)**2)
                        if vel >= 3:
                            pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
                        else:
                            pot_gen = 0
                    else:
                        pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
                Ptot += pot_gen
                columna_anterior = columna
    return Ptot

def fitness(arr_potencias):
    pot_total_poblacion = sum(arr_potencias)
    arr_fitness = []
    for pot in arr_potencias:
        arr_fitness.append(round(pot/pot_total_poblacion, 10))
    return arr_fitness

def ruleta(poblacion, arr_fitness):
    eleccion = random.uniform(0, 1)
    acum = 0
    for x in range(50):
        acum += arr_fitness[x]
        if acum >= eleccion:
            return poblacion[x]

def calcPotenciaFila(fila):
    Ptot = 0
    columna_anterior = 0
    primer_gen = False
    dist = 0
    for columna in range(10):
        if fila[columna] == 1:
            if primer_gen == False:
                vel = velm
                primer_gen = True
                pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
            else:
                dist = (columna - columna_anterior) * tam_celda
                if dist < 1494:
                    vel = vel * (1-(1-sqrt(1-0.889))/(k * dist/41.5)**2)
                    if vel >= 3:
                        pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
                    else:
                        pot_gen = 0
                else:
                    pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
            Ptot += pot_gen
            columna_anterior = columna
    return Ptot

def crossover(prob_cross):
    p1, p2 = [copy.deepcopy(torneo(poblacion, arr_fitness)), copy.deepcopy(torneo(poblacion, arr_fitness))]
    hijo1 = np.zeros((anchoCromosoma, largoCromosoma), dtype=int)
    hijo2 = np.zeros((anchoCromosoma, largoCromosoma), dtype=int)
    if prob_cross >= random.uniform(0, 1):
        cant_gen = True
        while cant_gen == True:
            for i in range(10):
                if calcPotenciaFila(p1[i]) >= calcPotenciaFila(p1[i]):
                    hijo1[i] = p1[i]
                else:
                    hijo1[i] = p2[i]
                if np.sum(p1[:,i]) >= np.sum(p2[:,i]):
                    hijo2[:,i] = p1[:,i]
                else:
                    hijo2[:,i] = p2[:,i]
            if hijo1.sum() > 25 or hijo2.sum() > 25:
                p1, p2 = [torneo(poblacion, arr_fitness), torneo(poblacion, arr_fitness)]
            else: 
                cant_gen = False
        return [hijo1, hijo2]
    else: return [p1, p2]

#Seleccion de un individuo de una poblacion por torneo
def torneo(poblacion, arr_fitness):
    #Se seleccionan de manera random dos individuos de la poblacion
    p1 = random.randint(0,49)
    p2 = random.randint(0,49)
    #Se compara cual es mas apato dependiendo de su fitness
    if arr_fitness[p1] > arr_fitness[p2]:
        ganador = poblacion[p1]
    else: ganador = poblacion[p2]
    return ganador

def FunMutacion(pares, mutacion):
    i = 0
    if mutacion >= random.uniform(0,1):
        x = random.randint(0,9)
        y = random.randint(0,9)
        if pares[0][x,y] == 0: pares[0][x,y] == 1
        else: pares[0][x,y] == 0
        if pares[1][x,y] == 0: pares[1][x,y] == 1
        else: pares[1][x,y] == 0
    return pares 

#Ordenar los arrays de poblacion potencias y fitness
def ordenarArrays(poblacion, arr_potencias, arr_fitness):
    n = cantCromosomas
    for i in range(n):
        for j in range(n-i-1):
            if arr_fitness[j] > arr_fitness[j + 1]:
                arr_fitness[j], arr_fitness[j + 1] = arr_fitness[j + 1], arr_fitness[j]
                poblacion[j], poblacion[j + 1] = poblacion[j + 1], poblacion[j]
                arr_potencias[j], arr_potencias[j + 1] = arr_potencias[j + 1], arr_potencias[j]

def crearGeneracion(arr_fitness, poblacion, prob_cross, prob_mut):
    arr_potencias = []
    newPoblacion = []
    while len(newPoblacion) < cantCromosomas:
        pares = crossover(prob_cross)
        pares = FunMutacion(pares ,prob_mut)
        newPoblacion.append(pares[0])
        newPoblacion.append(pares[1])
    for parque in poblacion:
        arr_potencias.append(calcularPotencia(parque, velm))
    arr_fitness = fitness(arr_potencias)
    ordenarArrays(newPoblacion, arr_fitness, arr_potencias)
    return newPoblacion

#Ejecucion
#Los 3 arrays (poblacion, arr_potencias, arr_parques) tienen el mismo indice
#es decir; al parque en poblacion[0] le corresponde la potencia en arr_potencias[0]
#y la fitness en arr_fitness[0]
    
poblacion = crearPoblacionInicial(cantCromosomas) #Array con 50 matrices (parques) de 10x10
for parque in poblacion:
    arr_potencias.append(calcularPotencia(parque, velm)) #Array con 50 numeros (POTENCIA de cada parque en el array 'poblacion')
arr_fitness = fitness(arr_potencias) #Array con 50 numeros (FITNESS de cada parque en el array 'poblacion')
ordenarArrays(poblacion, arr_potencias, arr_fitness)

#Acá se debería empezar a crear todas las generaciones
i = 0
x = 0
while i <= 10:
    Poblacion = crearGeneracion(arr_fitness, poblacion, prob_cross, prob_mut)
    #print('poblacion nueva')
    while x < 50:
        print('gen número', x) 
        print(poblacion[x])
        print(arr_potencias[x])
        x +=1
    i +=1



#for x in range(50):
#    print('Parque nro ', x+1, '\n', poblacion[x], '\nPotencia: ', arr_potencias[x], '\nFitness: ', arr_fitness[x], '\n\n')
#
#print(arr_fitness)
#print(arr_potencias)
#print(sum(arr_fitness))
