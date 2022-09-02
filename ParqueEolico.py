from cmath import log, sqrt
import numpy as np
import random
import math

anchoCromosoma = 10
largoCromosoma = 10
aerogenMax = 25
cantCromosomas = 50
crossover = 0.85
mutacion = 0.05
parque = []
arr_potencias = []
pot_total_poblacion = 0

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
    k = 1/2 * log(100/0.694)
    columna_anterior = 0
    for fila in range(10):
        primer_gen = False
        x = 0
        for columna in range(10):
            if parque[fila, columna] == 1:
                if primer_gen == False:
                    vel = velm
                    pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
                else:
                    x = (columna - columna_anterior) * 100
                    vel = vel * (1-(1-sqrt(1-0,889) * 1/(k * x/41.5)**2))
                    if vel >= 3:
                        pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
                    else:
                        pot_gen = 0
                Ptot += pot_gen
    return Ptot

def fitness(arr_potencias):
    pot_total_poblacion = sum(arr_potencias)
    return [pot/pot_total_poblacion for pot in arr_potencias]

#Ejecucion
#Los 3 arrays (poblacion, arr_potencias, arr_parques) tienen el mismo indice
#es decir; al parque en poblacion[0] le corresponde la potencia en arr_potencias[0]
#y la fitness en arr_fitness[0]
    
poblacion = crearPoblacionInicial(cantCromosomas) #Array con 50 matrices (parques) de 10x10
for parque in poblacion:
    arr_potencias.append(calcularPotencia(parque, 7.5)) #Array con 50 numeros (POTENCIA de cada parque en el array 'poblacion')

arr_fitness = fitness(arr_potencias) #Array con 50 numeros (FITNESS de cada parque en el array 'poblacion')

pot_total_poblacion = sum(arr_potencias)

for x in range(50):
    print('Parque nro ', x+1, '\n', poblacion[x], '\nPotencia: ', arr_potencias[x], '\nFitness: ', arr_fitness[x], '\n\n')
print('Potencia total de la poblacion: ', pot_total_poblacion)  

