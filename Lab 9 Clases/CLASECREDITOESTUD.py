# Clase para Credito de estudiantes

class claseCompra:
    def __init__(self, Fecha, Hora, Precio):
        self.aFecha = Fecha
        self.aHora = Hora
        self.aPrecio = Precio

class claseCredito:
    def __init__(self, Iden, Nombre, Correo):
        self.aIdentificacion = Iden
        self.aNombre = Nombre
        self.aCorreo = Correo
        self.aSaldo = 0
        self.aEstado = "En Proceso"
        self.aListaCompras = []

    def mIngresarCompra(self, Fecha, Hora, Precio):
        oCompra = claseCompra(Fecha, Hora, Precio)
        self.aListaCompras.append(oCompra)
        self.aSaldo += Precio
        self.aEstado = "En Proceso"
        return "Compra ingresada"

    def mCancelarCredito(self):
        if self.aEstado == "En Proceso":
            self.aSaldo = 0
            self.aEstado = "Cancelado"
            return "Credito cancelado"
        else:
            return "Factura ya se encuentra cancelada"

    def mImprimirCredito(self):
        S = "Identificacion: " + str(self.aIdentificacion)+"\n"
        S += "Nombre: "+ self.aNombre+"\n"
        S += "Correo: " +self.aCorreo+"\n"
        S += "Saldo: " + str(self.aSaldo)+"\n"
        S += "Estado: " + self.aEstado +"\n"
        S += "Fecha".center(15)+ "Hora".center(10)+ "Precio".center(10)+"\n"
        for e in self.aListaCompras:
            S += e.aFecha.center(15)
            S += e.aHora.center(10)
            S += str(e.aPrecio).rjust(10)+"\n"
        return S

    
    
