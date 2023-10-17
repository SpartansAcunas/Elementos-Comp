#Alfredo Acuña Chacón 2015183035 Lab 4
def contarvocales(M):
    v="AEIOUaeiouáéíóúÁÉÍÓÚ"
    Cantidad = 0
    for c in M:
        if c in v:
            Cantidad +=1
    return Cantidad

def contarpalabras(M,C):
    L=M.split()
    Cantidad=0
    for p in L:
        if len(p)==C:
            Cantidad+=1
    return Cantidad

def esalfabetica(M):
    T=len(M)
    for i in range(T-1):
        if M[i]>M[i+1]:
            return "No es alfabetica"
    return "Es alfabetica"

def eliminarruido(M):
    v="1234567890"
    for i in v:
        M=M.replace(i,"")
    return M
    

while True:
    Op=int(input("1.Contar Vocales\n2.Contar Palabras\n3.Palabra alfabetica\n4.Eliminar ruidos\n5.Salir del Programa\nDigite la Opcion: "))

    if Op==1:
        M=str(input("Agregue una palabra: "))       
        print("Resultado: ",contarvocales(M))

    if Op==2:
        M=str(input("Agregue una frase: "))
        C=int(input("Digite K: "))
        print("Hay",contarpalabras(M,C),"Palabra con",C,"de longitud")

    if Op==3:
        M=str(input("Agregue una frase: "))       
        esalfabetica(M)

    if Op==4:
        M=str(input("Agregue una frase: "))       
        print(eliminarruido(M))

    if Op==5:break
