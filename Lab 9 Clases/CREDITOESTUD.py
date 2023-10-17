# Programa credito estudiante

import pickle
import CREDITOESTUD

def Leer(NomArchivo):
    try:
        Archivo = open(NomArchivo, "rb")
        Datos = pickle.load(Archivo)
        Archivo.close()
        return Datos
    except:
        return{}

def Guardar(NomArchivo, Datos):
    Archivo = open(NomArchivo, "wb")
    pickle.dump(Datos, Archivo)
    Archivo.close()



def IngresarCredito(Creditos):
    Identificacion = input("Digite la identificacion: ")
    Nombre = input("Digite el nombre del Estudiante: ")
    Correo = input("Digite el corre: ")
    oCredito = ClaseCredEstudSolucion.claseCredito(Identificacion, Nombre, Correo)
    Creditos[Identificacion] = oCredito
    return "Credito agregado"



def IngresarCompra(Creditos):
    Identificacion = input("Digite la identificacion: ")
    if Creditos.get(Identificacion) != None:
        Fecha = input("Digite la fecha: ")
        Hora = input("Digite la hora: ")
        Precio = int(input("Digite el precio total de la compra: "))
        return Creditos[Identificacion].mIngresarCompra(Fecha,Hora,Precio)
    else:
        return "Credito de estudiante no existe"
    
def Cancelar(Creditos):
    Identificacion = input("Digite la identificacion: ")
    if Creditos.get(Identificacion) != None:
        return Creditos[Identificacion].mCancelarCredito()
    else:
        return "Credito de estudiante no existe"


def ImprimirCredito(Creditos):
    Identificacion = input("Digite la identificacion: ")
    if Creditos.get(Identificacion) != None:
        return Creditos[Identificacion].mImprimirCredito()
    else:
        return "Credito de estudiante no existe"

def Listar(Creditos):
    S = "Identificacion".center(10)
    S += "Nombre".center(20)
    S += "Correo".center(20)
    S += "Saldo".center(20)
    S += "Estado".center(20) + "\n"
    for e in Creditos.values():
        S += str(e.aIdentificacion).center(10)
        S += e.aNombre.center(20)
        S += e.aCorreo.center(20)
        S += str(e.aSaldo).center(20)
        S += e.aEstado.center(20) + "\n"
    return S

NomArchivo = "Creditos.pck"
Creditos = Leer(NomArchivo)

while True:
    print("""
    1.Ingresar Credito
    2.Ingresar Compra
    3.Cancelar Credito
    4.Imprimir Credito
    5.Listar Creditos
    6.Salir""")

    op = int(input("Digite la opción: "))
    if op == 1:
        print(IngresarCredito(Creditos))
        Guardar(NomArchivo, Creditos)
    if op == 2:
        print(IngresarCompra(Creditos))
        Guardar(NomArchivo, Creditos)
    if op == 3:
        print(Cancelar(Creditos))
        Guardar(NomArchivo, Creditos)
    if op == 4:
        print(ImprimirCredito(Creditos))
    if op == 5:
        print(Listar(Creditos))
    if op == 6:
        break
