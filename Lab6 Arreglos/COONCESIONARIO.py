#Lista inicial (mas adelante sera un archivo)

Autos = [["Toyota","Corolla", 1999],["Nissan", "Sentra",1995],["Subaru","Impreza",2001],["Mitsubishi","Lancer Evo IV",2002],["Lotus","Elise",1997]]

def MostrarListaAutos(Autos):
    S=" "
    S+="Marca".ljust(15)
    S+="Modelo".ljust(15)
    S+="Año".ljust(15)+"\n"
    for e in Autos:
        S+=e[0].ljust(15)
        S+= e[1].ljust(15)
        S+= str(e[2]).ljust(15)+"\n"
    return S

def AgregarAuto(Autos):
    Marca = input("Digite el nombre del Auto: ")
    Modelo = input("Digite el modelo: ")
    Año = int(input("Digite el año: "))
    
    Autos.append([Marca,Modelo,Año])
    return "Auto Agregado"

def EliminarAuto(Autos):
    Marca = input("Digite el nombre del Auto: ")
    Modelo = input("Digite el modelo: ")
    Año = int(input("Digite el año: "))
    for elemento in Autos:
        if elemento[0] == Marca and elemento [1] == Modelo and elemento[2] == Año:
            Autos.remove([Marca,Modelo,Año])
            return "Auto Removido"
    return "Auto No Encontrado"

def Autosxaño(Autos):
    Año = int(input("Digite el año: "))
    Suma=0
    for elemento in Autos:
        if elemento[2]==Año:
            Suma+=1
        return "Autos con ese Año : ",Suma
    return "Producto no encontrado"

def Autosxmarca(Autos):
    Marca = input("Digite la Marca: ")
    Suma=0
    for elemento in Autos:
        if elemento[0]==Marca:
            Suma+=1
        return "Autos con esa marca : ",Suma
    return "Producto no encontrado"


while True:
    print("""1. Mostrar lista autos \n
2. Incluir nuevo auto\n
3. Sacar Auto\n
4. Cantidad de autos de un año\n
5. Cantidad de autos de una marca\n
6.Salir""")
    op=int(input("Digite su opcion: "))

    if op==1:
        print(MostrarListaAutos(Autos))
    if op==2:
        print(AgregarAuto(Autos))
    if op==3:
        print(EliminarAuto(Autos))
    if op==4:
        print(Autosxaño(Autos))
    if op==5:
        print(Autosxmarca(Autos))
    if op==6:
        break
        
