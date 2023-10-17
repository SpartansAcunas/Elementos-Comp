#Lista de articulos en la refrigeradora.

#Lista inicial (mas adelante sera un archivo)

ArticulosRefri=[["Queso",1],["Natilla",2],["Refresco",3],["Mantequilla",1]]


#Agregar un nuevo producto

def Agregarunproducto(ArticulosRefri):
    Nombre = input("Digite el nombre del producto: ")
    Cantidad =int( input("Digite la cantidad del producto: "))
    ArticulosRefri.append([Nombre,Cantidad])
    return "Producto Agregado"

def Aumentarunproducto(ArticulosRefri):
    Nombre=input("Digite el nombre del  del producto: ")
    Cantidad=int(input("digite la cantidad a sumar"))
    for elemento in ArticulosRefri:
        if elemento[0] ==Nombre:
            elemento[1] += Cantidad
            return "Cantidad Agregada"
    return "Producto No Encontrado"

def disminuircantidades(ArticulosRefri):
    Nombre = input("Digite el nombre del producto: ")
    Cantidad = input("Digite la cantidad del producto: ")
    for elemento in ArticulosRefri:
        if elemento[0]==nombre:
            if elemento >=Cantidad:
                elemento[1]-= Cantidad
                return "Cantidad disminuida"
            else:
                return "No hay suficiente para disminuir"
    return "Producto no encontrado"

def MostrarListaProductos(ArticulosRefri):
    S=" "
    S+="Nombre".ljust(15)
    S+="Cantidad".ljust(10)
    for e in ArticulosRefri:
        S+=e[0].ljust(15)
        S+= str(e[1]).rjust(10)+"\n"
    return S

while True:
    print("""Mostrar Productos
2.Agregar Nuevo Producto,3.Aumentar Cantidad,4.Disminuir Cantidad, 5.Salir""")
    op=int(input("Digite su opcion: "))

    if op==1:
        print(MostrarListaProductos(ArticulosRefri))
    if op==2:
        print(Agregarunproducto(ArticulosRefri))
    if op==3:
        print(Aumentarunproducto(ArticulosRefri))
    if op==4:
        print(disminuircantidades(Articulosrefri))
    if op==5:
        break
