#Contar Mayusculas
def contarMayusculas(M):
    v="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    Cantidad = 0
    for c in M:
        if c in v:
            Cantidad +=1
    return Cantidad

def contarMayusculas2(M):
    Cantidad = 0
    for c in M:
        if "A"<= c <="Z":
            Cantidad +=1
    return Cantidad

M=str(input("Agregue una palabra"))
print("Resultado: ",contarMayusculas(M))
print("Resultado: ",contarMayusculas2(M))
