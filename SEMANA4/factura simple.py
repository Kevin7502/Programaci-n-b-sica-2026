#ALGORITMO
#1 PEDIR EL NOMBRE DEL PRODUCTO
#2 PEDIR EL PRECIO UNITARIO DEL PRODUCTO
#3 PEDIR LA CANTIDAD DEL PRODUCTO
#4 CALCULAR EL SUBTOTAL
#5 CALCULAR EL TOTAL
#6 MOSTRAR EL PRODUCTO, PRECIO, CANTIDAD, SUBTOTAL, TOTAL
#7 COMPARAR SI EL TOTAL ES MAYOR QUE 50.000 
#8 MOSTRAR SI APLICA DESCUENTO ESPECIAL

#PSEUDOCODIGO
#INICIO
 #LEER producto
 #LEER precio
 #LEER cantidad
 #subtotal <- precio * cantidad
 #iva <- subtotal * 0.19
 #total <- subtotal + iva
 #ESCRIBIR "Producto:", producto
 #ESCRIBIR "Precio:", precio
 #ESCRIBIR "Cantidad:", cantidad
 #ESCRIBIR "Subtotal:", subtotal
 #ESCRIBIR "IVA:", iva
 #ESCRIBIR "Total:", total
 #descuento <- total > 50000
 #ESCRIBIR "Aplica descuento especial?: ", total>=50.000
#FIN

producto = input("Ingrese el producto: ")
precio = float(input("Ingrese precio unitario: "))
cantidad = int(input("Ingrese cantidad: "))
subtotal = precio * cantidad
iva = subtotal * 0.19
total = subtotal + iva
print("Producto:", producto)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Subtotal:", subtotal)
print("IVA (19%):", iva)
print("Total:", total)
print("Aplica descuento especial?:", total > 50000)
