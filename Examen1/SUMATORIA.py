def Sumatoria(N):
    for i in range(1,N+1):
        Suma=(-1)**i*(1/i**3)
        print (Suma)
    return(Suma)
    



N=int(input("Digite el Numero: "))

Sumatoria(N)




