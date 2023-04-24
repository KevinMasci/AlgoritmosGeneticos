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
#Se crea la clase Cromosoma con las propiedades genes, objetivo y fitness
class cromosoma:
    def __init__(self, genes, objetivo, fitness): 
        self.genes = genes
        self.objetivo = objetivo
        self.fitness = fitness

#Crea la poblacion inicial
#Se pasa la cantidad de cromosomas(individuos) que se quieren 
# y la cantidad de genes que va a tener cada uno
def crearPoblacionInicial(cantCromosomas, cantGenes): 
    poblacion = []
    while (len(poblacion) < cantCromosomas):
        genes = ''.join(map(str, random.choices([0,1], k= cantGenes)))
        #La funcion objetivo y la fitness se setean en cero
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
        #La funcion fitness es la funcion objetivo de un individuo 
        # dividido la suma de todas las
        # funciones objetivo de todos los individuos

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
    for x in poblacion: #Para cada cromosoma en la poblacion
        #El maximo valor del acumulador es 1 porque la 
        # sumatoria de todas las fitness es 1
        acum += x.fitness 
        if acum >= eleccion: 
            return x 

#Seleccion de un individuo de una poblacion por torneo
def torneo(poblacion):  
    #Se seleccionan de manera random dos individuos de la poblacion
    participante1 = random.choice(poblacion) 
    participante2 = random.choice(poblacion)
    #Se compara cual es mas apato dependiendo de su fitness
    if participante1.fitness > participante2.fitness: 
        ganador = participante1
    else: ganador = participante2
    return ganador

#Calcula si se hace y realiza crossover
#Se le pasa la pareja de padres, y la probabilidad de crossover
def crossover(individuos, pCross): 
    #Se compara la probabilidad de crossover contra 
    # un numero random entre 0 y 1,
    # si es mayor a la probabilidad de crossover no hay
    if pCross >= random.uniform(0, 1):  
        #Se tira un numero random para saber a partir 
        # de que gen se va a hacer el crossover
        gen = random.randint(0, 29) 
        #Se hace una copia de los individuos
        hijo1, hijo2 = individuos[0].genes, individuos[1].genes 
        #Se toman los genes del hijo 1 hasta el gen generado de 
        # manera random y en el hijo 2 se toman a partir del gen.
        individuos[0].genes = hijo1[:gen] + hijo2[gen:] 
        individuos[1].genes = hijo2[:gen] + hijo1[gen:] 
    else: return individuos
    return individuos

#Recibe la pareja seleccionada, calcula y realiza mutacion
#Se le pasa la pareja, y la probabilidad de mutacion
def mutacion(individuos, pMut): 
    #Para cada cromosoma en los individuos.
    for crom in individuos: 
         #Si la probabilidad de mutacion es mayor o 
         # igual al numero random
        if pMut >= random.uniform(0, 1):
            #Se tira un numero random para saber a partir 
            # de que gen se va a hacer la mutacion
            gen = random.randint(0, 29) 
            #Se convierte el individuo en una lista.
            cromosoma = list(crom.genes) 
            if cromosoma[gen] == "0":
                 cromosoma[gen] = "1"
            else:
                 cromosoma[gen] = "0"
            crom.genes = ''.join(map(str, cromosoma)) 
    return individuos

#Elitismo
def elitismo(poblacion):
    #Se seleccionan los dos mejores, 
    #como estan ordenados de menor a mayor los 
    #mejores son el ultimo y el anteultimo siempre
    newGen = [] 
    newGen.append(poblacion[8])
    newGen.append(poblacion[9])
    #Los dos mejores pasan derecho a la nueva generacion
    return newGen 

#Creo una nueva generacion enviando como argumentos 
#la poblacion y las probabilidades de crossover y mutacion
def crearGeneracion(poblacion, pCross, pMut):
    newGen = []
    #Con elitismo
    #newGen = elitismo(poblacion)
    ##
    while len(newGen) < 10 : #Esto se va a correr 5 veces
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
    #Se vuelve a ordenar de menor a mayor
    newGen.sort(key = lambda newGen: newGen.objetivo)
    minimos.append(newGen[0].objetivo)
    maximos.append(newGen[9].objetivo)
    promedios.append(funcionPromedio(newGen))
    return newGen

#Poblacion inicial

#Se crea la poblacion inicial pasandole 
#la cantidad de cromosomas y la cantidad de genes
poblacion = crearPoblacionInicial(10, 30) 
#Se calcula la funcion objetivo de cada uno de los individuos
objetivo(poblacion) 
#Se calcula la funcion fitness de cada uno de los individuos
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
cantGen = 20
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