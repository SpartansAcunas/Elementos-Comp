

def contienedigitos(M):
    Num = "0123456789"
    for c in M:
        if c in Num:
            return "Contiene Digitos"
    return "No Contiene Digitos"

M=str(input("Digite un Mensaje: "))
print("Resultado es: ",contienedigitos(M))
