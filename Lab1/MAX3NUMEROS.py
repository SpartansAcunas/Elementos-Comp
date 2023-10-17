#Encontrar el maximo de tres numeros
a=int(input("digite el primer numero: "))
b=int(input("digite el segundo numero: "))
c=int(input("digite el tercer numero: "))

if a>b:
    if a>c:
        print("el maximo de los tres es",a)
    else:
        print("el maximo de los tres es",c)
else:
    if b>c:
        print("el maximo de los tres es",b)
    else:
        print("el maximo de los tres es",c)
