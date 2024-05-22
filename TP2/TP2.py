#Clases y Variables
class Elemento:
    def __init__(self, codigo, volumen, valor):
        self.codigo = codigo
        self.volumen = volumen
        self.valor = valor
        self.proporcion = valor / volumen
        
class Bolsa:
    def __init__(self, numero):
        self.numero = numero
        self.elementos = []
    
    def volumen_total(self):
        self.vol_total = sum(x.volumen for x in self.elementos)

    def valor_total(self):
        self.val_total = sum(x.valor for x in self.elementos)

#Lista de los 10 elementos       
items = []

items.append(Elemento(1, 150, 20))
items.append(Elemento(2, 325, 40))
items.append(Elemento(3, 600, 50))
items.append(Elemento(4, 805, 36))
items.append(Elemento(5, 430, 25))
items.append(Elemento(6, 1200, 64))
items.append(Elemento(7, 770, 54))
items.append(Elemento(8, 60, 18))
items.append(Elemento(9, 930, 46))
items.append(Elemento(10, 353, 28))

#Lista de los 3 elementos
items2= []

items2.append(Elemento(1, 1800, 72))
items2.append(Elemento(2, 600, 36))
items2.append(Elemento(3, 1200, 60))

#Funcion Metodo Exhaustivo
#crea numeros binario del 0 al 1023, los va recorriendo y cuando encuentra un 1
#agrega el elemento de la lista que corresponda a la posicion de ese 1
def MetodoExhaustivo(capacidad, elementos, digitos):
    valor_max = 0
    bolsa_elegida = Bolsa(0)

    for i in range(2 ** len(elementos)):
        binario = format(i, "b")
        numero = ("0000000000" + binario)[digitos:]
        bolsa = Bolsa(i+1)

        for index, digito in enumerate(numero):
            if digito == "1":
                bolsa.elementos.append(elementos[index])
                
        bolsa.volumen_total()
        bolsa.valor_total()
        
        if (bolsa.vol_total <= capacidad) and (bolsa.val_total > valor_max):
            valor_max = bolsa.val_total
            bolsa_elegida = bolsa

    print("Numero de la bolsa elegida: ", bolsa_elegida.numero, "\nContiene:")
    for x in bolsa_elegida.elementos:
        print("item nro ",x.codigo, "\tVolumen: ", x.volumen, "\tValor: ", x.valor)
    print(f"Volumen total de la bolsa: {bolsa_elegida.vol_total} \nValor total de la bolsa: {bolsa_elegida.val_total}")

#Funcion Metodo Greedy
#Por cada item en la lista le calcula su proporcion y almaceno
#en una lista, listp, cada objeto con su determinado prop, 
#ordeno esa lista de mayor a menor y por cada elemento voy sumando
#su volumen en una variable cap, si cap no supera 4200
#el elemento se agrega a la lista bol y asi con los demas hasta
#que se sobrepase el limite y despues se muestra por pantalla la bolsa
def MetodoGreedy(capacidad, elementos):
    prop = 0
    listp = []
    bol = []
    cap = 0
    valor_max = 0

    for x in elementos:
        prop = x.valor / x.volumen
        listp.append([prop, x.codigo, x.volumen, x.valor])

    listp.sort(reverse = True)
    for y in listp:
       cap = cap + y[2]
       if cap < capacidad:
          bol.append([y[1], y[2], y[3], y[0]])
          valor_max = valor_max + y[3]
          ban = cap
    print("\nLa bolsa Greedy Contiene:")
    for x in bol:
       print("item nro ",x[0], "\tVolumen: ", x[1], "\tValor: ", x[2], "\tProporcion :", x[3])
    print(f"Volumen de la bolsa: {ban} \nValor de la bolsa: {valor_max}")
    
#Ejecucion
ans = 0
while ans != 5:
    print("1) 10 elementos Exhaustivo\n2) 10 elementos Greedy\n3) 3 elementos Exhaustivo\n4) 3 elementos Greedy\n5) Salir")
    ans=input("Ingrese una opcion:")
    if ans == "1":
        MetodoExhaustivo(4200, items, -10)
    elif ans == "2":
        MetodoGreedy(4200, items)
    elif ans == "3":
        MetodoExhaustivo(3000, items2, -3)
    elif ans == "4":
        MetodoGreedy(3000, items2)
    elif ans == "5":
        break
    elif ans != "1" and ans != "2" and ans != "3" and ans != "4" and ans != "5":
        print("Ingrese un numero correcto")
