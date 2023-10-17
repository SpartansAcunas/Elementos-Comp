#Serie numerico que salta 3 y 2

def MuestreSerie(N):
    Numero = 2
    Salto = 3
    for i in range(N):
        print(Numero,end = ", ")
        Numero += Salto
        if Salto == 3:
            Salto = 2
        else:
            Salto = 3
N=int(input("Digite la  cantidad de numeros de la serie: "))
MuestreSerie(N)
