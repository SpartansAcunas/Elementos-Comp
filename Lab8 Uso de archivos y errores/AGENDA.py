#Tarea del Laboratorio 8 2015183035 Alfredo Acuña
import pickle

def Leer(NomArchivo):
    try:
        Archivo = open(NomArchivo,"rb")
        Datos = pickle.load(Archivo)
        Archivo.close()
        return Datos
    except:
        return {}

def Guardar(NomArchivo, Datos):
    Archivo = open(NomArchivo, "wb")
    pickle.dump(Datos,Archivo)
    Archivo.close()
    
def Ingresar(Agenda):
    Nombre=input("Digite el Nombre: ")
    Correo=input("Digite el Corrreo Electronico: ")
    Celular=input("Digite el Numero de Telefono Celuar: ")
    Telefono=input("Digite el Numero de Telefono de Oficina: ")
    Direccion=input("Digite el lugar de residencia: ")
    Trabajo=input("Digite el Trabajo que desempeña: ")
    if Agenda.get(Nombre.capitalize())==None:
        Agenda[Nombre.capitalize()]=[Correo,Celular,Telefono,Direccion,Trabajo]
        return "Persona Agregada"
    else:
        "La persona Ya se encontraba en la Agenda"

def Modificar(Agenda):
    Nombre=input("Digite el Nombre: ")
    if Agenda.get(Nombre.capitalize())!= None:
        Telefono=int(input("Digite el Nuevo Numero Telefonico: "))
        Agenda[Nombre.capitalize()][2]=Telefono
        return "Agenda Actualizada"
    else:
        return "Persona no Existente en la Agenda"

def Consultar(Agenda):
    Nombre=input("Digite el Nombre: ")
    if Agenda.get(Nombre.capitalize())!= None:
        Salida= "Correo: "+str(Agenda[Nombre.capitalize()][0])
        Salida+= "Celular: "+str(Agenda[Nombre.capitalize()][1])
        Salida+= "Telefono: "+str(Agenda[Nombre.capitalize()][2])
        Salida+= "Direccion: "+str(Agenda[Nombre.capitalize()][3])
        Salida+= "Trabajo: "+str(Agenda[Nombre.capitalize()][4])
        return Salida
    else:
        return "Persona no existente en la Agenda"

def Mostrar(Agenda):
    Salida="Nombre".center(10)+"    "
    Salida+="Correo".center(10)+"    "
    Salida+="Celuar".center(10)+"    "
    Salida +="Telefono".center(10)+"    "
    Salida+="Direccion".center(10)+"   "
    Salida+="Trabajo".center(10)+"\n"
    for e in Agenda.items():
        Salida+= e[0].ljust(10)+"  "
        Salida+= e[1][0].ljust(10)+"  "
        Salida+= str(e[1][1]).center(10)+"  "
        Salida+= str(e[1][2]).center(10)+"  "
        Salida+= e[1][3].center(10)+"  "
        Salida+= e[1][4].center(10)+"\n"
    return Salida

NomArchivo ="Agenda.pck"
Agenda = Leer(NomArchivo)

while True:

    print("""1. Ingresar contacto
2. Modificar Teléfono Celular
3. Consultar Contacto
4. Listar Contactos
5. Salir""" )

    op= int(input("Digite su opcion: "))

    if op == 1:
        print(Ingresar(Agenda))
        Guardar(NomArchivo,Agenda)
    if op == 2:
        print(Modificar(Agenda))
        Guardar(NomArchivo,Agenda)
    if op == 3:
        print(Consultar(Agenda))
    if op == 4:
        print(Mostrar(Agenda))
    if op == 5:
        break  




