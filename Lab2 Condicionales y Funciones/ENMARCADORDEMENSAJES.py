
def EnmarcarMensaje(Mensaje, Simbolo = "*"):
    Tam = len(Mensaje)
    print(Simbolo*2+Simbolo*Tam+Simbolo*2)
    print(Simbolo+ " " + " "*Tam + " " +Simbolo)
    print(Simbolo+" "+Mensaje+ " " +Simbolo)
    print(Simbolo+ " " + " "*Tam+ " " +Simbolo)
    print(Simbolo*2+Simbolo*Tam+Simbolo*2)

M=input("Digite un mensaje:")
S=input("Digite el Simbolo:")

EnmarcarMensaje(M,S)
