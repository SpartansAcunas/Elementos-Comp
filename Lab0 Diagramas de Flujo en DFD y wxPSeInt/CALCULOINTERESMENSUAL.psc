Algoritmo CALCULOINTERESMENSUAL
	Escribir "Introduzca Salario Promedio: "
	Leer S
	Si S<100000
		A<-((S*12*0.03)/12)+S
		Escribir "el valor con interes mensual es: ",A
	SiNo
		Si 100000<S Y S<500000 Entonces
			B<-((S*12*0.05)/12)+S
			Escribir "el valor con interes mensual es: ",B
		SiNo
			C<-((S*12*0.1)/12)+S
			Escribir "el valor con interes mensual es: ",C
			
		FinSi
	FinSi
FinAlgoritmo
