#calculos de la comision de un vendedor
Venta=int(input("Digite comision de vendedor:"))
if 200000<Venta<500000:
    print("La comision del vendedor es :",Venta*0.10)
elif Venta >= 500000:
    print("La comision del vendedor es:",Venta*0.20)
else:
    print("el vendedor no cuenta con comision")
