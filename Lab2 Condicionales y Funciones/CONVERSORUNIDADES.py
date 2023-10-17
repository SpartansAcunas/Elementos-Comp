#Lab 2 2015183035 Alfredo Acuña Chacón
#Conversiones
def FaC(X):
    return X-32/1.8
def GaL(X):
    return X*0.2642
def MaP(X):
    return X*3.281
def MaY(X):
    return X*1.09361329833771
def cmap(X):
    return X*2.54
def kmam(X):
    return X*0.6214
def kgal(X):
    return X*2.204


def Menu():
    print("1. Fahrenheith a Celsius")
    print("2. Litros a Galones")
    print("3. Metros a Pies")
    print("4. Metros a Yardas")
    print("5. Centimetros a Pulgadas")
    print("6. Kilometros a Millas")
    print("7. Kilogramos a Libras")
    print("8. Salir")

    Op=int(input("digite la Opcion: "))
    
    if Op==1 :
        X=int(input("digite el valor: "))
        print("El resultado es: " , FaC(X))

    if Op==2 :
        X=int(input("digite el valor: "))
        print("El resultado es: " , GaL(X))

    if Op==3 :
        X=int(input("digite el valor: "))
        print("El resultado es: " , MaP(X))

    if Op==4 :
        X=int(input("digite el valor: "))
        print("El resultado es: " , MaY(X))

    if Op==5 :
        X=int(input("digite el valor: "))
        print("El resultado es: " , cmap(X))

    if Op==6 :
        X=int(input("digite el valor: "))
        print("El resultado es: " , kmam(X))

    if Op==7 :
        X=int(input("digite el valor: "))
        print("El resultado es: " , kgal(X))
        

    if Op!=8 :
        Menu()


Menu()
