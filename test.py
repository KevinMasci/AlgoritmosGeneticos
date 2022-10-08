from math import log, sqrt
import numpy as np
import random
import copy
import matplotlib.pyplot as plt

lista = np.array([[0, 1, 1, 0, 0],
                  [1, 0, 1, 1, 0],
                  [1, 0, 1, 1, 0],
                  [1, 1, 0, 1, 0],
                  [1, 0, 1, 0, 0]])

while np.sum(lista) > 10:
    lista_indices = []
    for i in range(5):
        for j in range(5):
            if lista[i, j] == 1:
                lista_indices.append([i, j])
    x, y = random.choice(lista_indices)
    lista[x, y] = 0

print(lista_indices)
print(lista)