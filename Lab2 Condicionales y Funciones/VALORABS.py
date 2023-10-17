
def ValorAbsoluto(X):
    if X<0:
        return(-X)
    else:
        return(X)

N=int(input("Digite un Valor: "))
Y=5 **ValorAbsoluto(N)
print("El resultado es :",Y)
