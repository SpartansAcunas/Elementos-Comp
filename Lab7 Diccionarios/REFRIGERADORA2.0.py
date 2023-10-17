#Refri con diccionarios
Refri={"Mantequilla":[3,"10-10-2019"],
       "Leche":[2,"15-10-2019"],"Refresco":[5,"25-11-2019"]}

def Ingresar(Refri):
    Nombre=input("Digite el producto: ")
    Can=int(input("Digite la cantidad: "))
    Fecha=input("Digite proxima fecha")
    if Refri.get(Nombre.capitalize())==None:
        Refri[Nombre.capitalize()]=[Can,Fecha]
        return "Producto Agregado"
    else:
        return "Producto ya existente"
def Consultar(Refri):
    Nombre=input("Digite el Producto: ")
    if Refri.get(Nombre.capitalize())==None:
        Salida= "Cantidad: "+str(Refri[Nombre.capitalize()[0]])
        Salida+= "Fecha: "+Nombre.capitalize()[1]
        return Salida
    else:
        return "Producto no existente"

def Modificar(Refri):
    Nombre=input("Digite el Producto: ")
    if Refri.get(Nombre.capitalize())==None:
        print("1.Cantidad")
        print("2.Fecha")
        X=int(input("Digite su opcion"))
        if X ==1:
            Can=int(input("Digite la cantidad: "))
            Refri[Nombre.capitalize()[0]]=Can
        return "Cantidad Modificada"
        if X ==2:
           Fecha=input("Digite proxima fecha")
           Refri[Nombre.capitalize()[1]]=Fecha
        return "Fecha Modificada"
    else:
        return "Producto no existente"

def Mostrar(Refri):
    Salida="Nombre".center(15)
    Salida+="Cantidad".center(10)
    Salida+="Fecha".center(10)+"\n"
    for e in Refri.items():
        Salida += e[0].ljust(10)
        Salida+= str(e[1][0]).rjust(10)+"  "
        Salida+= e[1][1].center(10)+"\n"
    return Salida

while True:
    print("""
1.Ingresar Nuevo Producto
2.Consultar Producto
3.Modificar Producto
4.Mostrar Lista de Productos
5.Salir""")
    op= int(input("Digite su opcion: "))

    if op == 1:
        print(Ingresar(Refri))
    if op == 2:
        print(Consultar(Refri))
    if op == 3:
        print(Modificar(Refri))
    if op == 4:
        print(Mostrar(Refri))
    if op == 5:
        break  
