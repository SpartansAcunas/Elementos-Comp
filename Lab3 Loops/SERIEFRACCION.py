#Mostrar resultado de la serie de fracciones:

def CalculoSerie(N):
    Suma = 0
    for i in range(1, N+1):
        Suma = Suma+(-1)**(i+1)*1/i
    return Suma
        
N=int(input("Digite un valor entero: "))
print("El resultado es: ", CalculoSerie(N))

