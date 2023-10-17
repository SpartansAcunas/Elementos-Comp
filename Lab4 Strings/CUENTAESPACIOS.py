#Contar espacios en blanco

def contarespacios(M):
    Cantidad = 0
    for c in M:
        if c==" ":
            Cantidad+= 1
    return Cantidad


#Contar con metodo

def contarespacios2(M):
    Cantidad = M.count(" ")
    return Cantidad

M=input("Digite un Mensaje")
print("Resultado 1: " ,contarespacios(M))
print("Resultado 2: " ,contarespacios2(M))
