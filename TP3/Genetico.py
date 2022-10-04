import pandas as pd
import random
import copy
from matplotlib import pyplot as plt
from matplotlib import image as img

#Declaracion de constantes y variables
cantCromosomas = 50
cantGenes = 23
poblacion = []
pCross = 0.75
pMut = 0.05
cantCiclos = 200
cantSeleccion = 34
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
        aux += crom.distancia
    for crom in poblacion:
        crom.fitness = crom.distancia/aux

#Crossover ciclico
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

#Mutacion intercambia dos genes
def mutacion(nuevaGen):
    for crom in nuevaGen:
        if random.uniform(0, 1) < pMut:
            i = random.randint(0,23)
            j = random.choice(list(range(1, i)) + list(range(i+1, 24)))
            aux = crom.genes[i]
            crom.genes[i] = crom.genes[j]
            crom.genes[j] = aux

def crearGeneracion():
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

#Funcion para graficar el recorrido
def mapa(recorrido):
    coordenadas=[[541,599],[333,455],[543,273],[560,207],[547,614],[241,381],
    [169,527],[201,800],[479,470],[655,279],[316,1002],[530,262],
    [229,1393],[265,322],[288,252],[290,129],[282,146],[174,468],
    [256,536],[464,455],[335,699],[339,264],[277,1526],[377,888]]
    image = img.imread("Archivos\Argentina.png")
    fig = plt.figure(1)
    ax = fig.gca()
    plt.imshow(image)
    figure = ax.plot(coordenadas[recorrido[0]][0], coordenadas[recorrido[0]][1], marker= "o", color= "b")
    for i in range(24):
        desde = recorrido[i]
        hacia = recorrido[i + 1]
        coordx = [coordenadas[desde][0], coordenadas[hacia][0]]
        coordy = [coordenadas[desde][1], coordenadas[hacia][1]]
        figure = ax.plot(coordx, coordy, c= 'r')
    plt.show()

#Funcion principal
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

    #Corrida de ciclos
    c = 0
    while c < cantCiclos:
        crearGeneracion()
        for crom in poblacion:
            crom.dist()
        fitness(poblacion)
        poblacion.sort(key=lambda poblacion: poblacion.distancia)
        c += 1

    elElegido = poblacion[0]
    elElegido.genes.append(elElegido.genes[0])
    arr_distancias = []
    for i in range(24):
        arr_distancias.append(matriz_distancias[elElegido.genes[i], elElegido.genes[i+1]])
    cities = []
    for x in elElegido.genes:
        cities.append(ciudades[x])
    print('recorrido: ', elElegido.genes,'\nCiudades: ',  cities,'\nDistancia: ', elElegido.distancia, '   Fitness: ', elElegido.fitness)
    mapa(elElegido.genes)
    poblacion.clear()
  