#para crear listas bidimensionales podemos hacer una lista de numeros:

grilla_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#forme una lista de 4 lineas, la primera es 0, la segunda 1 y asi
#luego para leerlos de izquierda a derecha el primero es 0, el segundo 1 y asi
#por ejemplo 0, 0 va a ser el 1, si hago 2 y 1 va a ser el 8
#para acceder a algun numero en particular de la lista:

print(grilla_numeros[0][0])
print(grilla_numeros[2][1])

#puedo hacer un bucle dentro de esto, para obtener todos los valores:

for fila in grilla_numeros:
    print(fila)

#si quiero que me imprima todos los numeros en fila:
for fila in grilla_numeros:
    for columna in fila:
        print(columna)

