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
potencias = []

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

poblacion = crearPoblacionInicial(cantCromosomas)
for parque in poblacion:
    potencias.append(calcularPotencia(parque, 7.5))
    
for x in range(50):
    print('Parque nro ', x+1, '\n', poblacion[x], '\nPotencia: ', potencias[x], '\n\n')    
    
#for index, x in enumerate(poblacion):
#    print(index+1)
#    print(x)

