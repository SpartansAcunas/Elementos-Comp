#Laboratorio 3 Alfredo Acuña
def Pares(N):
    Numero = 2
    for i in range(N-1):
        print(Numero, end=", ")
        Numero += 2
    print (Numero)

def Sum(N):
    Suma = 0
    for i in range(1, N+1):
        Suma =  Suma+i*2
    return Suma


def Triangulares(N):
    Numero = 1
    for i in range(1,N+1):
        Numero =int( i*(i+1)/2)
        print(Numero, end=", ")
    print (Numero)


def Sum1(N):
    Suma = 0
    for i in range(1,N+1):
        Suma =  Suma + (i)**i
    return Suma



def Sum2(N):
    Suma = 0
    for i in range(1,N+1):
        Suma = Suma+(2*i-1)
    return Suma



while True:
    print("1. Muestra y suma pares")
    print("2. Números triangulares")
    print("3. Calcula sumatoria 1")
    print("4. Calculo sumatoria 2")
    print("5. Salir")

    Op=int(input("digite la Opcion: "))
    
    if Op==1 :
        N=int(input("Digite la Cantidad de pares: "))
        Pares(N)
        print("el resultado de la suma de los numeros pares es: ",Sum(N))

    if Op==2 :
        N=int(input("Digite la Cantidad de valores: "))
        Triangulares(N)
              
    if Op==3 :
        N=int(input("Digite la Cantidad de valores: "))
        print("el resultado de la suma de Potencias: ",Sum1(N))

    if Op==4 :
        N=int(input("Digite la Cantidad de valores: "))
        print("el resultado de la sumatoria: ",Sum2(N))
        

    if Op==5 :
        break

