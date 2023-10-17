#CALCULO INTERES MENSUAL

S=float(input("Introduzca Salario Promedio: "))

if S<100000 :
    print("el valor con interes mensual es: ",(((S*12*0.03)/12)+S),)
elif 100000<S<500000:
    print("el valor con interes mensual es: ",(((S*12*0.05)/12)+S))
else:
    print("el valor con interes mensual es: ",(((S*12*0.1)/12)+S))
