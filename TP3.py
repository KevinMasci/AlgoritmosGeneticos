import pandas as pd
import numpy as np

lista_ciudades = []
total_recorrido =[]

tc = pd.read_excel('Archivos\TablaCapitales.xlsx')

ciudades = list(tc.columns)
ciudades_back = list(tc.columns)
matriz_distancias = tc.to_numpy()

c = int(input('Ingrese una ciudad (1 - 24)')) - 1
distancias_ciudad_origen = matriz_distancias[:,c]

def buscarCiudadMasCercana(matriz, ciudades, c):
    dist_min = np.nanmin(matriz[: , c])
    i_ciudad = np.where(matriz[:,c] == dist_min)[0][0]
    nom_ciudad = ciudades[i_ciudad]
    return [i_ciudad, nom_ciudad, dist_min]

lista_ciudades.append(ciudades[c])

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

print(lista_ciudades)
print(total_recorrido)
print(sum(total_recorrido))
