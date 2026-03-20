#ALGORITMO
#1 PEDIR TEMPERATURA EN GRADOS CELSIUS AL USUARIO
#2 CONVERTIR LA TEMPERATURA A FAHRENHEIT
#3 CONVERTIR LA TEMPERATURA A KELVIN
#4 MOSTRAR LOS RESULTADOS
#5 COMPRARAR SI SUPERA LOS 37°C

#PSEUDOCODIGO
#INCIO
 #LEER celsius
 #fahrenheit <- (celsius * 9/5) + 32
 #kelvin <- celsius + 273.15
 #ESCRIBIR "Celsius:", celsius
 #ESCRIBIR "Fahrenheit:", fahrenheit
 #ESCRIBIR "Kelvin:", kelvin
 #fiebre <- celsius > 37
 #ESCRIBIR "Supera temperatura de fiebre(37°C)?: ", celsius > 37
#FIN

celsius = float(input("Ingrese temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print("Temperatura en Celsius:", celsius)
print("Temperatura en Fahrenheit:", fahrenheit)
print("Temperatura en Kelvin:", kelvin)
print("Supera temperatura de fiebre?:", celsius > 37)
