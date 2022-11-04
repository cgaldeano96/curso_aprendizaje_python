#voy a armar dos variables

num1 = input("ingresa un numero: ")
num2 = input("ingresa otro numero: ")

#ahora armo una variable para un rdo:

resultado = num1 + num2

print(resultado)

#no imprime por ejemplo 5+8 = 13, sino que python al recibir datos de un user por defecto python lo va a convertir en una cadena
#hay que convertir a num1 y num2 en numeros, por eso podemos usar el int

resultado = int(num1) + int(num2)

#ahora con esa formula si sumamos 5+8 nos va a dar 13
#el int solo calculara numeros enteros, si le tiro decimales me va a dar error
#para evitar eso puedo hacer la misma formula con float

resultado = float(num1) + float(num2)
