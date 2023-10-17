def Convertir(F):
    C=(F-32/1.8)
    if C<15:
        print("La temperatura es fria",round(C,2))
    elif 15<=C<=25:
        print("La Temperatura es agradable",round(C,2))
    else:
        print("La Temperatura es caliente",round(C,2))

F=float(input("Digite los grados Farenheith: "))

Convertir(F)

\n
