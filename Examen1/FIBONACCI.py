
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

N = int(input("Digite el número de términos de la secuencia de Fibonacci que desea generar: "))

Fibonacci(N)
