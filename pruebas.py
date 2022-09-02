import random
import numpy as np
def terreno(arrTerreno):
    i = 0
    j = 0
    for i in range(5):
        for j in range(5):
            if (j != 3 and i!= 4) and (j != 4 and i !=3) and (j != 5 and i !=5):
                arrTerreno[i,j] = random.randint(0,1)
    
    return arrTerreno





terrenoInic = np.zeros(shape=(5,5),dtype=int)
Tlleno = terreno(terrenoInic)
print(Tlleno)
print("hla")
print(terrenoInic)