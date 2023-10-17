#Vertificar dos restas
a=int(input("digite el primer numero: "))
b=int(input("digite el segundo numero: "))
if a-b>0:
    print("resta es positiva",a-b)
elif b-a>0:
    print("resta es positiva",b-a)
else:
    print("numeros iguales")
