#Manejo de errores

while True:

    try:
        X=int(input("digite un numero"))
        Z=int(input("digite otro valor"))
        Y= X/Z
        print ("El resultado es" ,Y)
        break
    except ValueError:
        print("Valor invalido")
    except ZeroDivisionError:
        print("Error division por cero")
    except :
        print("Ocurrio un error")


