#Mostrar n impares:

def Impares(N):
    Numero = 1
    for i in range(N-1):
        print(Numero, end=", ")
        Numero += 2
    print (Numero)
N=int(input("Digite la Cantidad de impares: "))
Impares(N)

