phrase = "academia de estudios"

#Phrase sirve para que te lea la frase de ahora en mas
#Lower es para que te aparezca todo en minuscula y upper todo en mayuscula
#Si agrego un + " " puedo sumar algo puntual a la frase
#Si hago un \n de ahi para adelante me bajara el texto una linea
print(phrase.lower())
print(phrase.upper())
print(phrase + " esta piola")
print("academia\nde estudios")

#Len Sirve para leer la cantidad de letras/digitos
print(len(phrase))

#Si pongo entre corchetes un numero va a ser la letra que me va a traer segun su posición, por ejemplo el 0 me va a traer la a de academia de estudios, esto es una FUNCION DE INDICE.
print(phrase[0])
#Por ejemplo con el .index va a ser al reves, vamos a buscar una letra y sobre eso nos va a decir en que n° esta de la phrase (la C es 1)
print(phrase.index("c"))

#El replace sirve para cambiar de la phrase una palabra por otra, por ejemplo reemplazo estudios por cualquier otra y la va a cambiar
print(phrase.replace("estudios", "inservible"))
