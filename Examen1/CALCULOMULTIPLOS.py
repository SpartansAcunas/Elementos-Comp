def CalculoMultiplos(N,C):
    
    for i in range(1,C+1):
        Suma=N*i
        print(Suma)
    return (Suma)
    
N=int(input("Digite el Numero: "))
C=int(input("Digite la cantidad de multiplos: "))
CalculoMultiplos(N,C)


