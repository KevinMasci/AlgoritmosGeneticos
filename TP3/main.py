from Genetico import metodoGenetico
from Heuristico import rutaConCiudad, rutaMasCorta

ans = 0
while ans != 5:
    print("1) Ruta mas corta Heuristica\n2) Ruta mas corta Heuristica eligiendo ciudad inicial\n3) Ruta mas corta AG\n4) Salir")
    ans=input("Ingrese una opcion:")
    if ans == "1":
        rutaMasCorta()
    elif ans == "2":
        rutaConCiudad()
    elif ans == "3":
        metodoGenetico()
    elif ans == '4':
        break
    elif ans != "1" and ans != "2" and ans != "3":
        print("Ingrese un numero correcto")
