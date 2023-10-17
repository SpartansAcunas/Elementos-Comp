#Crear funciones para trabajar con matrices numericas
import random
#Funcion para llenar matriz de numeros aleatorios

def Crearmatriz(N,M):
    Matriz = []
    #Ciclo para recorrer la cantidad de filas
    for i in range(N):
        Fila=[]
        #Ciclo para incluir los elementos de la fila
        for j in range(M):
            X= random.randint(-99,99)
            Fila.append(X)
        Matriz.append(Fila)
    return Matriz

def Muestramatriz(Matriz):
    S= ""
    for fila in Matriz:
        for e in fila:
            S += str(e).rjust(5)
        S += "\n"
    return S

def Multiplicamatriz(Matriz, X):
    M=[]
    for fila in Matriz:
        F=[]
        for e in fila:
            F.append(e*X)
        M.append(F)
    return M
def Calculomatriz(Matriz):
    Suma=0
    Promedio=0
    Cantidad=0
    for Fila in Matriz:
        for e in Fila:
            Suma+= e
            Cantidad +=1
    Promedio= Suma / Cantidad
    #Promedio = Suma / (len(Matriz)*len(Matriz[0]))
    return Suma,Promedio



def Sumaporfila(Matriz):
    M=[]
    for fila in Matriz:
        F=[]
        Suma=0
        for e in fila:
            F.append(e)
            Suma+= e
        F.append(Suma)
        M.append(F)
    return M

def Sumaporcolumna(Matriz):
    filafinal=[0]*len(Matriz[0])
    M= []
    for fila in Matriz:
        F=[]
        i=0
        for e in fila:
            filafinal[i]+=e
            F.append(e)
            i+=1
        M.append(F)
    M.append(filafinal)
    return M

N=int(input("Digite la cantidad de filas"))

M=int(input("Digite la cantidad de columnas"))

X=int(input("Digite el Valor a Multiplicar"))

Matriz=Crearmatriz(N,M)

print(Muestramatriz(Matriz))
print(Muestramatriz(Multiplicamatriz(Matriz,X)))
print("Suma: %d\nPromedio: %.2f"%Calculomatriz(Matriz)) 
print(Muestramatriz(Sumaporfila(Matriz)))
print(Muestramatriz(Sumaporcolumna(Matriz)))


