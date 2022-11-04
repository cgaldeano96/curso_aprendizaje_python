#Una lista es una de las estructuras mas importantes de python
#Vamos a poder almacenar y organizar un monton de valores dentro de lista

numeros_suerte = [4, 8, 15, 16, 23, 42]
amigos = ["seba", "brian", "gise", "oscar", "oscar", "toby"]

#se puede extender la lista original:
amigos.extend(numeros_suerte)
amigos.append("creed")
print(amigos)

#si quiero cambiar algun lugar dentro de la lista, voy a tener en cuenta dos parametros, primero el n° que quiero cambiar y luego el elemento que quiero cambiar
#va a agregar a kevin a la lista moviendo hacia a la derecha el resto de la lista
amigos.insert(1, "kevin")
print(amigos)

#para eliminar algo de la lista uso la funcion remove, a partir de ahora gise no viene mas en la lista
amigos.remove("gise")
print(amigos)

#con la funcion index me va a decir en que posición esta cada nombre
print(amigos.index("oscar"))
print(amigos.index("toby"))

#con un count puedo ver cuantas veces esta un nombre, por ejemplo oscar esta 2 veces
print(amigos.count("oscar"))

#con un sort va a ordenar la lista de forma ascendente, en este caso alfabeticamente

#para copiar una lista puedo hacer:
amigos2 = amigos.copy()
print(amigos2)

#la funcion pop lo que hace es sacar un elemento de la lista:
amigos.pop()
print(amigos)

#para limpiar toda la lista con un clear se va a limpiar toda:
amigos.clear()
print(amigos)