
import random

#Crear lista de numeros aleatorios

def Crearaleatorios(N):
    Lista = []
    for i in range(N):
        X=random.randint(-99,99)
        if X not in Lista:
            Lista.append(X)
    return Lista


N=int(input("Digite la cantidad de numeros: "))
Lista = Crearaleatorios(N)
print ("Lista Original:\n",Lista)

#Crear lista de numeros sin negativos

def MostrarSinnegativos(Lista):
    L=[]
    for e in Lista:
        if e <0:
            L.append(0)
        else:
            L.append(e)
    return L

print("Lista sin negativos:\n",MostrarSinnegativos(Lista))

#Crear lista de numeros de 1 a 50 unicamente

def Mostrarhasta50(Lista):
    L=[]
    for e in Lista:
        if e >0 and e<50:
            L.append(e)
    return L

print("Lista de 0 a 50 :\n",Mostrarhasta50(Lista))

#Muestra el calculo de suma de positivos y negativos

def Sumador(Lista):
    Sumaa=0
    Sumab=0
    for e in Lista:
        if e>0:
            Sumaa+=e
        if e<0:
            Sumab+=e
    return Sumaa, Sumab

print("Suma positiva: %d \nSuma negativa: %d"%Sumador(Lista))


#Crear lista sin indices pares 

def Mostrarsinindice(Lista):
    L=[]
    for i in range (len(Lista)):
        if i%2==1:
            L.append(Lista[i])
    return L

print("Listas sin indice par :\n",Mostrarsinindice(Lista))



