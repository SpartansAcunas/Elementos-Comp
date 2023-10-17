#Peaje
def Camion(x):

    if x>=2 and x <=3:
        print("El costo del Peaje es de 800 colones")
    if x==4:
        print("El costo del Peaje es de 1200 colones")
    if x>=5:
        print("El costo del Peaje es de 2000 colones")
    if x>0 and x<2:
        print("Su vehiculo no debe pagar el Peaje")

x=int(input("Coloque la cantidad de ejes de su Vehiculo"))
Camion(x)
