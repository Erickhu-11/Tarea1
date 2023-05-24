arreglo1 = []
arreglo2 = []

for x in range (5):

    numeros1 = int(input("Ingrese los números del primer arreglo: ".format(x+1)))
    arreglo1.append(numeros1)

for x in range (5):
    numeros2 = int(input("Ingrese los números del segundo arreglo: ".format(x+1)))
    arreglo2.append(numeros2)

    
arreglo3 = arreglo1 + arreglo2

arreglo4 = sorted(arreglo3, reverse=True)

print(arreglo4)
