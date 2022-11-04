#tenemos que ponerle un nombre que identifique lo que va a haber dentro de la lista:
#vamos a hacer una lista de amigos, con los corchetes python entiende que quiero almacenar muchas variables
amigos = ["seba", "brian", "gise", "oscar", "toby"]
print(amigos)

#ahi va a imprimir toda la lista, si quisiera imprimir solo un valor dentro de la lista voy a poner el indice
#el primer elemento siempre es 0, el segundo es 1 y el ultimo 2
print(amigos[0])
print(amigos[2])

#si pongo indices negativos empezara por la ultima parte de la lista
print(amigos[-1])

#si quiero poner mas de un caracter puedo poner : que significa que pondra todo lo que esta por delante de eso:
print(amigos[1:])

#si quiero poner un rango puedo poner por ej de la posición 1 a 3, no incluira el tercero, sino 1 y 2
print(amigos[1:3])

#para cambiar algun valor de la lista puedo hacer esto y me lo cambia de ahora en mas
amigos[1] = "mike"
print(amigos[1:3])