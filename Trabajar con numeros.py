#Imprimir un numero es asi de sencillo
print(2.089)
print(-2.098)
#para suma, multiplicaciones, etc:
print(3 + 4.5)

#para hacer un calculo primero multiplica y despues suma:
print(3 * 4 + 5)
#para cambiar ese orden puedo agregar (), calcula primero el () y dsps multiplica
print(3 * (4 + 5))
#operador de modulo, va a calcular el numero entero mas cercano y va a largar el resto del rdo, 10/3 es 3 y me sobra 1
print(10 % 3)

#Se puede almacenar estos numeros en variables:

mi_numero1 = 5
print(mi_numero1)

#Tambien puedo hacer cadenas de un n° + texto por ejemplo:
print(str(mi_numero1) + " es mi numero favorito")

#la variante abs vuelve en absoluto mi numero:
mi_numero2 = -10
print(abs(mi_numero2))

#para elevar un numero vamos a usar pow y una , que lo va a elevar
print(pow(3, 2))
print(pow(4, 6))

#la funcion max lo que va a hacer es de los numeros que le reconozco va a darme el mayor, por ejemplo entre 4 y 6 me va a dar 6
#Por el contrario min me va a dar el minimo, en este caso 4
print(max(4, 6))
print(min(4, 6))

#la funcion round nos va a permitir redondear un numero, por ejemplo un 3.2 va a ser 3 o 3,7 va a ser 4
print(round(3.2))
print(round(3.7))

#la funcion floor va a agarrar el mas bajo, por ejemplo 3.2 va a agarrar 3

#Si quiero traer muchos operadores matematicos debo dejar el #from math import bajarlo
