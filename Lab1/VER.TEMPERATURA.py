#Verificar la Temeratura
F=float(input("Digite la temperatura en Farenheith: "))
C=(F-32)/1.8
if C<=16:
    print("Temperatura es fría",round(C,2),"Celsius")
elif 16<C<26:
    print("Temperatura agradable",round(C,2),"Celsius")
else:
    print("Temperatura es Caliente",round(C,2),"Celsius")
