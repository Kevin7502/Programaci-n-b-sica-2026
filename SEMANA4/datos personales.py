#ALGORITMO
#1 PEDIR EL NOMBRE DEL USUARIO
#2 PEDIR LA EDAD DEL USUARIO
#3 PEDIR LA CIUDAD DE RESIDENCIA AL USUARIO
#4 MOSTRAR EL NOMBRE DEL USURAIO
#5 MOSTRAR LA EDAD DEL USUARIO
#6 MOSTRAR LA CIUDAD DE RESIDENCIA DEL USUARIO
#7 COMPARAR SI LA EDAD DEL USUARIO ES MAYOR O IGUAL A 18
#8 MOSTRAR EL RESULTADO "FALSE O TRUE"

#PESUDOCODIGO
#INICIO
  #LEER NOMBRE DEL USUARIO
  #LEER EDAD DEL USUARIO
  #LEER CIUDAD DE RESIDENCIA DEL USUARIO
  #ESCRIBIR "Hola, me llamo", nombre
  #ESCRIBIR "Tengo", edad, "años"
  #ESCRIBIR "Soy de", ciudad
  #ESCRIBIR "¿Es mayor de edad?", edad>18
#FIN

nombre=input("Ingrese su nombre")
edad=int(input("dame tu edad:"))
ciudad=input("Ingrese su ciudad")
print("Hola, me llamo", nombre)
print("Tengo", edad, "años")
print("Soy de", ciudad)
print("¿Es mayor de edad?", edad>18)
