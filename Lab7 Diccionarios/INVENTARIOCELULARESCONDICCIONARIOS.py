#Inventario con diccionarios
Tienda={"Sam001" : ["Samsung S10",400000,4],
"Sam002" : ["Samsung S8",250000,0],
"Ipn001" : ["Iphone 8",500000,5] }

def Ingresar(Tienda):
    Codigo=input("Digite el Codigo: ")
    Estilo=input("Digite el estilo / Marca: ")
    Precio=input("Digite Precio")
    Cantidad=input("Digite cantidad")
    if Tienda.get(Codigo.capitalize())==None:
        Tienda[Codigo.capitalize()]=[Estilo,Precio,Cantidad]
        return "Producto Agregado"
    else:
        "Producto ya Existente"

def Modificar(Tienda):
    Codigo=input("Digite el Producto: ")
    if Tienda.get(Codigo.capitalize())!= None:
        Can=int(input("Digite la cantidad: "))
        Tienda[Codigo.capitalize()][2]=Can
        return "Producto Actualizado"
    else:
        return "Producto no existente"

def Consultar(Tienda):
    Codigo=input("Digite el Producto: ")
    if Tienda.get(Codigo.capitalize())!=None:
        Salida= "Estilo: "+str(Tienda[Codigo.capitalize()][0])
        Salida+= "Precio: "+str(Tienda[Codigo.capitalize()][1])
        Salida+= "Cantidad: "+str(Tienda[Codigo.capitalize()][2])
        return Salida
    else:
        return "Producto no existente"

def Mostrar(Tienda):
    Salida="Código".center(10)
    Salida+="Estilo".center(10)
    Salida+="Precio".center(10)
    Salida +="Cantidad".center(10)+"\n"
    for e in Tienda.items():
        Salida+= e[0].ljust(10)
        Salida+= e[1][0].ljust(10)+"  "
        Salida+= str(e[1][1]).center(10)+"  "
        Salida+= str(e[1][2]).center(10)+"\n"
    return Salida

def Mostrar2(Tienda):
    Salida="Código".center(10)
    Salida+="Estilo".center(10)
    Salida+="Precio".center(10)
    Salida +="Cantidad".center(10)+"\n"
    for e in Tienda.items():
        if e[1][2]==0:
            Salida+= e[0].ljust(10)
            Salida+= e[1][0].ljust(10)+"  "
            Salida+= str(e[1][1]).center(10)+"  "
            Salida+= str(e[1][2]).center(10)+"\n"
    return Salida

while True:
    print("""1. Ingresar producto
2. Actualizar cantidad producto existente
3. Consultar un producto
4. Listar todos los productos
5. Listar todos los productos que tengan cantidad en 0
6. Salir""" )
    op= int(input("Digite su opcion: "))

    if op == 1:
        print(Ingresar(Tienda))
    if op == 2:
        print(Modificar(Tienda))
    if op == 3:
        print(Consultar(Tienda))
    if op == 4:
        print(Mostrar(Tienda))
    if op ==5:
        print(Mostrar2(Tienda))
    if op == 6:
        break  

