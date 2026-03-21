#ALGORITMO
#1 PEDIR EL NOMBRE DEL USUARIO
#2 PEDIR EL CONSUMO MENSUAL EN METROS CUBICOS DEL USUARIO
#3 SI CONSUMO ESTA ENTRE 1 Y 15 ESCRIBIR ¡Excelente! Eres un usuario responsable del agua
#4 SI CONSUMO ESTA ENTRE 16 Y 30 ESCRIBIR Tu consumo está dentro del promedio del hogar
#5 SI CONSUMO ES DE MAS DE 30 METROS CUBICOS ESCRIBIR Atención: tu consumo es alto, revisa posibles fugas
#6 SI CONSUMO ES 0 O NEGATIVO ESCRIBIR Error: el consumo debe ser mayor a 0

nombre=input("Ingrese su nombre:")
consumo=int(input("Ingrese su consumo mensual en metros cubicos(número entero):"))
if consumo >= 1 and consumo <= 15:
    print(nombre, "¡Excelente! Eres un usuario responsable del agua")
elif consumo >= 16 and consumo <= 30:
    print(nombre, "Tu consumo está dentro del promedio del hogar")
elif consumo > 30:
    print(nombre, "Atención: tu consumo es alto, revisa posibles fugas")
else:
    print(nombre, "Error: el consumo debe ser mayor a 0")
