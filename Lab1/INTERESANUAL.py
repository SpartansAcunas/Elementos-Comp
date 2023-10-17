#Calculo de interes por  años

C=float(input("INGRESE EL CAPITAL ACTUAL: "))
n=float(input("INGRESE LA CANTIDAD DE AÑOS: "))
x=float(input("INGRESE EL INTERES: "))

if x>0 and n>0:
    CapitalFinal=C*(1+x/100)*n
    print("Su monto final seria de: ",CapitalFinal)
else:
    print("El calculo no se puede realizar debido a que ingreso valores negativos o nulos")
