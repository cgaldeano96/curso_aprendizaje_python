#vamos a poner for para hacer un bucle con ciertas especificaciones

for letra in "academia jirafa":
    print(letra)

#basicamente el for va a ir por bucle imprimiendo letra por letra de "academia jirafa"

#en este caso le doy una lista de nombres y me los va imprimiendo de 1 en 1
amigos = ["jim", "karen", "kevin"]
for amigos in amigos:
    print(amigos)

#va a imprimir todos los numeros hasta el 9
amigos = ["jim", "karen", "kevin"]
for index in range(10):
    print(index)

#va a imprimir todos los numeros del 3 al 9
amigos = ["jim", "karen", "kevin"]
for index in range(3, 10):
    print(index)

#con la funcion len va a imprimir un rango entre 0 y el numero de amigos (como hay 3 va a ser 0, 1 y 2)
amigos = ["jim", "karen", "kevin"]
len(amigos)
for index in range(len(amigos)):
    print(amigos[index])

#si quiero imprimir la primera iteración y el resto que me tire otro campo puedo hacer:
amigos = ["jim", "karen", "kevin"]
for index in range(5):
    if index == 0:
        print("primera iteración")
    else:
        print("no es la primera iteración")
