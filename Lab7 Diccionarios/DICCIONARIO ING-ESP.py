#Prueba 30 Septiembre
#Traductor Ing-Esp
DicciIngESpa={'Hello' : 'Hola',
              'My' : 'Mi',
              'Name' : 'Nombre',
              'Is' : 'Es'}


def Agregar(DicciIngESpa):
    Ingles=input("Digite la palabra nueva en ingles: ")
    Español=input("Digite la palabra nueva en Español: ")
    DicciIngESpa[Ingles.capitalize()]=Español.capitalize()
    return "Palabra agregada al diccionario"

def Eliminar(DicciIngESpa):
    Ingles=input("Digite la palabra nueva en ingles: ")
    if DicciIngESpa.get(Ingles.capitalize()) != None:
        del DicciIngESpa[Ingles.capitalize()]
        #DicciIngESpa.pop(Ingles.capitalize())
        return "Palabra eliminada del diccionario"
    return "Palabra no encontrada"

def TraducirFrase(DicciIngESpa):
    Frase=input("Agregue frase en ingles a traducir: ")
    Salida=""
    for p in frase.split():
        if DicciIngESpa.get(p.capitalize()):
            Salida+= DicciIngESpa[P.capitalize()]+" "
        return Salida

def ListaPalabras (DicciIngESpa):
    Salida= "Ingles        Español\n"
    for E in DicciIngESpa.items():
        Salida += E[0].ljust(10)
        Salida += E[1].ljust(10)+"\n"
    return Salida
while True:
    print("""
1.Ingresar Nueva Palabra
2Eliminar Palabra
3.Traducir Frase
4.Mostrar Lista de Palabras
5.Salir""")
    op= int(input("Digite su opcion: "))

    if op == 1:
        print(Agregar(DicciIngESpa))
    if op == 3:
        print(TraducirFrase(DicciIngESpa))
    if op == 4:
        print(ListaPalabras(DicciIngESpa))
    if op == 2:
        print(Eliminar(DicciIngESpa))
    if op == 5:
        break  
