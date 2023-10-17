#Examen 1 Tipo 1
#Carnet:2015183035
#Nombre:Alfredo Acuña Chacón

def Camion(x):

    if x>=2 and x <=3:
        print("El costo del Peaje es de 800 colones")
    if x==4:
        print("El costo del Peaje es de 1200 colones")
    if x>=5:
        print("El costo del Peaje es de 2000 colones")
    if x>0 and x<2:
        print("Su vehiculo no debe pagar el Peaje")
        
def CalculoMultiplos(N,C):
    
    for i in range(1,C+1):
        Suma=N*i
        print(Suma)
    return (Suma)

def Sumatoria(N):
    for i in range(1,N+1):
        Suma=(-1)**i*(1/i**3)
        print (Suma)
    return(Suma)


def Fibonacci(N):
    if N <= 0:
        return
    elif N == 1:
        print(0)
        return
    else:
        a, b = 0, 1
        print(a)
        print(b)
        for i in range(N - 2):  # Restamos 2 porque ya imprimimos los primeros dos números
            a, b = b, a + b
            print(b)

while True:
    Op=int(input("1.Peaje\n2.Multiplos\n3.Sumatoria\n4.Fibonacci\n5.Salir del Programa\nDigite la Opcion: "))

    if Op==1:
        x=int(input("Coloque la cantidad de ejes de su Vehiculo"))
        Camion(x)

    if Op==2:
        N=int(input("Digite el Numero: "))
        C=int(input("Digite La cantidad de multiplos: "))
        print("Los multiplos serian: ")
        CalculoMultiplos(N,C)

    if Op==3:
        N=int(input("Digite el Numero: "))
        Sumatoria(N)
    if Op==4:
        N = int(input("Digite el número de términos de la secuencia de Fibonacci que desea generar: "))
        Fibonacci(N)

    if Op==5:break


