#Archivos

Archivo = open("MiArchivo.txt","w")
Archivo.write("Hoy es un dia soleado")
Archivo.close()



Archivo=open("Miarchivo.txt","r")
Mensaje=Archivo.read()
print (Mensaje)
Archivo.close


