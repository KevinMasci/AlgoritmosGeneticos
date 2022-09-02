import random
import math
import copy
import pandas as pd
import matplotlib.pyplot as plt

#Probabilidades
pCrossover = 0.75
pMutacion = 0.05

#Variables
maximos = []
minimos = []
promedios = []

#Clases
class cromosoma:
    def __init__(self, genes, objetivo, fitness):
        self.genes = genes
        self.objetivo = objetivo
        self.fitness = fitness

#Crea la poblacion inicial
def crearPoblacionInicial(cantCromosomas, cantGenes):
    poblacion = []
    while (len(poblacion) < cantCromosomas):
        genes = ''.join(map(str, random.choices([0,1], k= cantGenes)))
        individuo = cromosoma(genes, 0, 0)
        poblacion.append(individuo)
    
    return poblacion

#Calcula la funcion objetivo de cada individuo
def objetivo(poblacion):
    for individuo in poblacion:
        individuo.objetivo = round(math.pow((int(individuo.genes, 2)/round(math.pow(2,30))-1),2), 8)

#Calcula la funcion fitness de cada individuo
def fitness(poblacion):
    suma = 0
    for individuo in poblacion:
        suma += individuo.objetivo
    for individuo in poblacion:
        individuo.fitness = round((individuo.objetivo / suma), 4)

#Busca promedio de una poblacion.
def funcionPromedio(individuos):
    prom = 0
    acumobj = 0
    for x in individuos:
        acumobj += x.objetivo
    prom = round((acumobj / 10),4)
    return prom

#Selecicon de un individuo de una poblacion por ruleta
def funcionRuleta(poblacion):
    eleccion = random.uniform(0, 1)
    acum = 0
    for x in poblacion:
        acum += x.fitness
        if acum >= eleccion:
            return x

#Seleccion de un individuo de una poblacion por torneo   #un 0.40 de la poblacion
def torneo(poblacion):
    cantParticipantes = round(len(poblacion) * 0.4)
    participantes = []
    while len(participantes) < cantParticipantes:
        participante = random.choice(poblacion)
        participantes.append(participante)
    participantes.sort(key = lambda participantes: participantes.fitness)
    return participantes[-1]

#Calcula si se hace y realiza crossover
def crossover(individuos, pCross):
    if pCross >= random.uniform(0, 1):
        gen = random.randint(0, 29)
        hijo1, hijo2 = individuos[0].genes, individuos[1].genes
        individuos[0].genes = hijo1[:gen] + hijo2[gen:]
        individuos[1].genes = hijo2[:gen] + hijo1[gen:]
    else: return individuos
    return individuos

#Recibe la pareja seleccionada, calcula y realiza mutacion
def mutacion(individuos, pMut):
    for crom in individuos:
        if pMut >= random.uniform(0, 1):
            gen = random.randint(0, 29)
            cromosoma = list(crom.genes)
            if cromosoma[gen] == "0":
                 cromosoma[gen] = "1"
            else:
                 cromosoma[gen] = "0"
            crom.genes = ''.join(map(str, cromosoma))
    return individuos

#Elitismo
def elitismo(poblacion):
    newGen = []
    newGen.append(poblacion[8])
    newGen.append(poblacion[9])
    return newGen

#Creo una nueva generacion enviando como argumentos la poblacion y las probabilidades de crossover y mutacion
def crearGeneracion(poblacion, pCross, pMut):
    newGen = []
    #Con elitismo
    newGen = elitismo(poblacion)
    ##
    while len(newGen) < 10 :
        #Con ruleta
        #pares = [copy.deepcopy(funcionRuleta(poblacion)), copy.deepcopy(funcionRuleta(poblacion))]
        #Con torneo
        pares = [copy.deepcopy(torneo(poblacion)), copy.deepcopy(torneo(poblacion))]
        pares = crossover(pares, pCross)
        pares = mutacion(pares, pMut)
        sujeto1, sujeto2 = pares
        newGen.append(sujeto1)
        newGen.append(sujeto2)
    objetivo(newGen)
    fitness(newGen)
    newGen.sort(key = lambda newGen: newGen.objetivo)
    minimos.append(newGen[0].objetivo)
    maximos.append(newGen[9].objetivo)
    promedios.append(funcionPromedio(newGen))
    return newGen

#Poblacion inicial
poblacion = crearPoblacionInicial(10, 30)
objetivo(poblacion)
fitness(poblacion)
poblacion.sort(key=lambda poblacion: poblacion.objetivo)
tabla = pd.DataFrame({'Generacion': [1],
                       'Minimo': [poblacion[0].objetivo],
                       'Maximo': [poblacion[9].objetivo],
                       'Cromosoma maximo': [int(poblacion[9].genes, 2)],
                       'Cromosoma maximo binario': [poblacion[9].genes],
                       'Promedio': [funcionPromedio(poblacion)]
                    })
minimos.append(poblacion[0].objetivo)
maximos.append(poblacion[9].objetivo)
promedios.append(funcionPromedio(poblacion))

#Ejecucion
i = 1
cantGen = 100
while i < cantGen:
    poblacion = crearGeneracion(poblacion, pCrossover, pMutacion)
    newRow = {'Generacion':i+1, 
              'Minimo':poblacion[0].objetivo, 
              'Maximo':poblacion[9].objetivo, 
              'Cromosoma maximo': int(poblacion[9].genes, 2), 
              'Cromosoma maximo binario': poblacion[9].genes, 
              'Promedio': funcionPromedio(poblacion)}
    tabla = tabla.append(newRow, ignore_index=True)
    i += 1
tabla.to_excel(r'tabla.xlsx', index = False, header=True)

#Grafica
generaciones = list(range(1, cantGen+1))
plt.plot(generaciones, maximos, label='maximos')
plt.plot(generaciones, minimos, label='minimos')
plt.plot(generaciones, promedios, label='promedios')
plt.xlabel('Generaciones')
plt.ylabel('Valor de funcion objetivo')
plt.title('Maximos, minimos y promedios')
plt.legend()
#plt.xticks(generaciones)
plt.show()