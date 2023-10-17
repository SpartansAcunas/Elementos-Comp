Algoritmo CalculoTriangulos
	Escribir "Agregue el digito uno si desea calcular un Area o el digito dos si quiere calcular el Perimetro:"
	Leer D
	Si D=1 Entonces
		Escribir "Agregue el valor de la base:"
		Leer b
		Escribir "Agregue el valor de la altura:"
		Leer h
		A <- b*h/2
		Escribir "La Area del triangulo es: ",A
	SiNo 
		Si D=2 
			Escribir "Agregue el valor del primer lado:"
			Leer LA
			Escribir "Agregue el valor del segundo lado:"
			Leer LB
			Escribir "Agregue el valor del tercer lado:"
			Leer LC
			P <- LA+LB+LC
			Escribir "E Perimetro del triangulo es: ",P
		Sino
			EScribir "No Se puede realizar ninguna accion"
		Fin Si
	Fin si
FinAlgoritmo
