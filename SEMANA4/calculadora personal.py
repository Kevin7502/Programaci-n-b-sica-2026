#ALGORITMO
 #1 PEDIR AL USUARIO EL PRIMER NUMERO ENTERO
 #2 PEDIR AL USUARIO EL SEGUNDO NUMERO ENTERO
 #3 CALCULAR SUMA
 #4 CALCULAR RESTA
 #5 CALCULAR MULTIPLICACION
 #6 CALCULAR DIVISION 
 #7 CALCULAR DIVISION ENTERA
 #8 CALCULAR RESIDUO
 #9 CALCULAR POTENCIA
 #10 MOSTRAR CADA RESULTADO
 #11 COMPARAR SI LA SUMA ES MAYOR QUE 100

#PSEUDOCODIGO
#INICIO
 # LEER num1
 # LEER num2
 #suma <- num1 + num2
 #resta <- num1 - num2
 #multiplicacion <- num1 * num2
 #division <- num1 / num2
 #division entera <- num1 // num2
 #residuo <- num1 % num2
 #potencia <- num1 ** num2
 #ESCRIBIR "Suma:", suma
 #ESCRIBIR "Resta:", resta
 #ESCRIBIR "Multiplicacion:", multiplicacion
 #ESCRIBIR "Division:", division
 #ESCRIBIR "Division entera:", division_entera
 #ESCRIBIR "Residuo:", residuo
 #ESCRIBIR "Potencia:", potencia
 #ESCRIBIR "La suma es mayor que 100?", suma>100
#FIN

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
residuo = num1 % num2
potencia = num1 ** num2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("Division entera:", division_entera)
print("Residuo:", residuo)
print("Potencia:", potencia)
print("La suma es mayor que 100?:", suma > 100)
