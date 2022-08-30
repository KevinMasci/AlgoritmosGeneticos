import numpy as np
from random import randint

anchoCromosoma = 10
largoCromosoma = 10
aerogenMax = 25
crossover = 0.85
mutacion = 0.05
poblacion = []


def parquenuevo():
    arrayvacio = np.zeros(anchoCromosoma, largoCromosoma)
    for x in range(0, aerogenMax):
        i = randint(0, 1)
        if i == 1:
            posicion1 = randint(0, largoCromosoma)
            posicion2 = randint(0, anchoCromosoma)
            if arrayvacio[posicion1][posicion2] == 0:
                arrayvacio[posicion1][posicion2] = 1
    poblacion.append(arrayvacio)
