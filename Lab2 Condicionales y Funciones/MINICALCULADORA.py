#minicalculadora

def Suma(X,Y):
    return X+Y
def Resta(X,Y):
    return X-Y
def Multiplica(X,Y):
    return X*Y
def Divide(X,Y):
    if Y!=0:
        return X/Y
    else:
        return "No se puede realizar la operacion"
def Eleva(X,Y):
    return X**Y

def Menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Elevar")
    print("6. Salir")

    Op=int(input("digite la Opcion: "))

    if Op==1 :
        X=int(input("digite un valor: "))
        Y=int(input("digite otro valor: "))
        print("El resultado es: ",Suma(X,Y))

    if Op==2 :
        X=int(input("digite un valor: "))
        Y=int(input("digite otro valor: "))
        print("El resultado es: ",Resta(X,Y))

    if Op==3 :
        X=int(input("digite un valor: "))
        Y=int(input("digite otro valor: "))
        print("El resultado es: ",Multiplica(X,Y))

    if Op==4 :
        X=int(input("digite un valor: "))
        Y=int(input("digite otro valor: "))
        print("El resultado es: ",Divide(X,Y))

    if Op==5 :
        X=int(input("digite un valor: "))
        Y=int(input("digite otro valor: "))
        print("El resultado es: ",Eleva(X,Y))

    if Op!=6 :
        Menu()


Menu()
