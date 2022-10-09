
from math import log, sqrt

lista = [1,0,0,0,0,0,0,0,0,0]
velm = 7.5
tam_celda = 100
k = 1/2 * log(100/0.694)

def calPotFila():
    Ptot = 0
    columna_anterior = 0
    primer_gen = False
    dist = 0
    for columna in range(10):
        if lista[columna] == 1:
            if primer_gen == False:
                vel = velm
                primer_gen = True
                pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
            else:
                dist = (columna - columna_anterior) * tam_celda
                if dist < 1494:
                    vel = vel * (1-(1-sqrt(1-0.889))/(k * dist/41.5)**2)
                    if vel >= 3:
                        pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
                    else:
                        pot_gen = 0
                else:
                    pot_gen = 5411 * 0.5 * 1.15 * (vel ** 3)
            Ptot += pot_gen
            columna_anterior = columna
    return Ptot