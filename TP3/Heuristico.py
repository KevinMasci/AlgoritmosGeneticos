import pandas as pd
import numpy as np
from Genetico import mapa

tc = pd.read_excel('Archivos\TablaCapitales.xlsx')
matriz_distancias = tc.to_numpy()
ciudades = list(tc.columns)

def buscarCiudadMasCercana(matriz_distancias, ciudades, c):
    dist_min = np.nanmin(matriz_distancias[: , c])
    i_ciudad = np.where(matriz_distancias[:,c] == dist_min)[0][0]
    nom_ciudad = ciudades[i_ciudad]
    return [i_ciudad, nom_ciudad, dist_min]


def rutaHeuristica(distancias_ciudad_origen, c):
    lista_ciudades = []
    total_recorrido =[]
    indices_ciudades = []
    ciudades = list(tc.columns)
    ciudades_back = list(tc.columns)
    lista_ciudades.append(ciudades[c])
    matriz_distancias = tc.to_numpy()
    for x in range(23):
        ciudad_distancia = buscarCiudadMasCercana(matriz_distancias, ciudades, c) #Busco indice ciudad, nombre ciudad y dist min
        lista_ciudades.append(ciudades[ciudad_distancia[0]])    #Guardo la ciudad
        total_recorrido.append(ciudad_distancia[2]) #Guardo la distancia
        del ciudades[c]
        matriz_distancias = np.delete(matriz_distancias, c, axis=1)
        matriz_distancias = np.delete(matriz_distancias, c, 0)
        c = ciudades.index(ciudad_distancia[1]) #Guardo el nuevo indice
    ciudad_final = lista_ciudades[-1]   #nombre de la ultima ciudad
    i_ciudad_final = ciudades_back.index(ciudad_final)  #indice original de la ultima ciudad
    dist_final = distancias_ciudad_origen[i_ciudad_final]
    lista_ciudades.append(lista_ciudades[0])
    total_recorrido.append(dist_final)
    for x in lista_ciudades:
        indices_ciudades.append(ciudades_back.index(x))
    return [sum(total_recorrido), lista_ciudades, indices_ciudades]

def rutaConCiudad():
    for x in range(24):
        print(x+1, ')', ciudades[x])
    c = int(input('Ingrese una ciudad (1 - 24)')) - 1
    distancias_ciudad_origen = matriz_distancias[:,c]
    total, recorrido, ruta = rutaHeuristica(distancias_ciudad_origen, c)
    print(recorrido, total, ruta)
    mapa(ruta)

def rutaMasCorta():
    ruta = []
    total = 0
    for c in range(24):
        distancias_ciudad_origen = matriz_distancias[:,c]
        viaje = rutaHeuristica(distancias_ciudad_origen, c)
        if total == 0:
            total = viaje[0]
            ruta = viaje[1]
            recorrido = viaje[2]
        elif viaje[0] < total:
            total = viaje[0]
            ruta = viaje[1]
            recorrido = viaje[2]
    print(ruta, total, recorrido)
    mapa(recorrido)