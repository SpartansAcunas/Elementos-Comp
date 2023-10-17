#Resolucion de Ecuacion de primer grado
import math
a=float(input("introduzca el valor de la pendiente o constante que acompaña la X: "))
b=float(input("introduzca el valor de la constante: "))



if a!=0 :
    x=-b/a
    print("la ecuacion tiene solucion y esta es:",x)
elif a==0 and b==0:
    print ("Solucion indeterminada")
else:
    print ("Solucion imposible")
