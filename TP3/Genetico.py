import numpy as np
import pandas as pd
import random
import copy

cantCromosomas = 50
cantGenes = 23
poblacion = []
pCross = 0.75
pMut = 0.20
cantCiclos = 2000
tc = pd.read_excel('Archivos\TablaCapitales.xlsx')
matriz_distancias = tc.to_numpy()
ciudades = list(tc.columns)

class cromosoma:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0
        
    def dist(self):
        self.distancia = sum(matriz_distancias[self.genes[i], self.genes[i+1]] for i in range(23)) + matriz_distancias[self.genes[-1], self.genes[0]]

def fitness(poblacion):
    aux = 0
    for crom in poblacion:
        #if np.isnan(crom.distancia):
        #    print('hay un nan')
        aux += crom.distancia
    for crom in poblacion:
        crom.fitness = crom.distancia/aux

def crossover(p1, p2):
    hijo1 = cromosoma([-1]*24)
    hijo2 = cromosoma([-1]*24)
    hijo1.genes[0] = p1.genes[0]
    hijo2.genes[0] = p2.genes[0]
    repite = False
    i = 0
    while repite == False:
        if p2.genes[i] not in hijo1.genes:    
            hijo1.genes[p1.genes.index(p2.genes[i])] = p2.genes[i]
            i = p1.genes.index(p2.genes[i])
        else: repite = True
    for x in range(24):
        if hijo1.genes[x] == -1:
            hijo1.genes[x] = p2.genes[x]
    repite = False
    i = 0
    while repite == False:
        if p1.genes[i] not in hijo2.genes:    
            hijo2.genes[p2.genes.index(p1.genes[i])] = p1.genes[i]
            i = p2.genes.index(p1.genes[i])
        else: repite = True
    for x in range(24):
        if hijo2.genes[x] == -1:
            hijo2.genes[x] = p1.genes[x]
    return [hijo1, hijo2]

def mutacion(nuevaGen):
    for crom in nuevaGen:
        if random.uniform(0, 1) < pMut:
            i = random.randint(0,23)
            j = random.choice(list(range(1, i)) + list(range(i+1, 24)))
            aux = crom.genes[i]
            crom.genes[i] = crom.genes[j]
            crom.genes[j] = aux
            #crom.genes[i], crom.genes[j] = crom.genes[j], crom.genes[i]

def crearGeneracion(cantSeleccion):
    nuevaGen = poblacion[0: cantSeleccion]#Metodo de seleccion basado en el rango
    padres = copy.deepcopy(nuevaGen)
    while len(nuevaGen) < cantCromosomas:
        p1, p2 = random.sample(padres, 2)
        if random.uniform(0, 1) < pCross:
            nuevaGen += crossover(p1, p2)
            padres.remove(p1)
            padres.remove(p2)
    mutacion(nuevaGen)
    poblacion.clear()
    for crom in nuevaGen:
        poblacion.append(crom)

def metodoGenetico():
    #Poblacion inicial
    while len(poblacion) < cantCromosomas:
        lista = range(24)
        genes = random.sample(lista, 24)
        crom = cromosoma(genes)
        crom.dist()
        poblacion.append(crom)
    fitness(poblacion)
    poblacion.sort(key=lambda poblacion: poblacion.distancia)

    c = 0
    while c < cantCiclos:
        crearGeneracion(34)
        for crom in poblacion:
            crom.dist()
        fitness(poblacion)
        poblacion.sort(key=lambda poblacion: poblacion.distancia)
        c += 1
    

    #for crom in poblacion:
    #    print('recorrido: ', crom.genes, '\ndistancia: ', crom.distancia, '   fitness: ', crom.fitness)
    #print(sum(crom.fitness for crom in poblacion))

    elElegido = poblacion[0]
    elElegido.genes.append(elElegido.genes[0])
    arr_distancias = []
    for i in range(24):
        arr_distancias.append(matriz_distancias[elElegido.genes[i], elElegido.genes[i+1]])
    cities = []
    for x in elElegido.genes:
        cities.append(ciudades[x])
    print('recorrido: ', elElegido.genes, '\ndistancias: ' , arr_distancias,'\nCiudades: ',  cities,'\ndistancia: ', elElegido.distancia, '   fitness: ', elElegido.fitness)
    poblacion.clear()