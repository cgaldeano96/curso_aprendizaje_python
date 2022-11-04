#Las declaraciones son una estructura especial de python donde podemos ayudar a nuestros programas a hacer decisiones
#Ciertas condiciones son verdaderas y puedo ejecutar otro codigo cuando otras son verdaderas
#si la accion es verdadera la hago, si es falsa se omite y se sigue
#por ejemplo, si tengo hambre, desayuno. Si no tengo hambre, sigo a la siguiente accion
#otro ejemplo es, salgo de mi casa, SI llueve, llevo paraguas, en otro caso, llevo lentes de sol

#Vamos a crear un booleano:

es_hombre = True

if es_hombre:
    print("tu eres un hombre")

#Si lo paso a falso no va a imprimir nada

es_hombre = False
if es_hombre:
    print("tu eres un hombre")

#Else va a usarse para decir "por lo contrario", como si fuera un negativo del IF

es_hombre = False
if es_hombre:
    print("tu eres un hombre")
else:
    print("tu no eres un hombre")

es_hombre = True
if es_hombre:
    print("tu eres un hombre")
else:
    print("tu no eres un hombre")

#Si agregamos una variable como por ejemplo es alto habria que usar ambas variables, con un or va a ser verdadero cuando se cumpla una de las condiciones:
#Si pongo una sola en false me va a seguir diciendo True, para que sea el else ambas deberian ser falsas
es_hombre = True
es_alto = True

if es_hombre or es_alto:
    print("tu eres un hombre o alto o ambas")
else:
    print("tu no eres un hombre ni alto")

es_hombre = False
es_alto = False

if es_hombre or es_alto:
    print("tu eres un hombre o alto o ambas")
else:
    print("tu no eres un hombre ni alto")

#Vamos a usar and y ambas condiciones deben cumplirse, si es una true y otra false me seguira dando falso
es_hombre = False
es_alto = False

if es_hombre and es_alto:
    print("tu eres un hombre alto")
else:
    print("tu no eres un hombre alto")


es_hombre = False
es_alto = True

if es_hombre and es_alto:
    print("tu eres un hombre alto")
else:
    print("tu no eres un hombre alto")

#otra funcion es elif y es para hacer alguna aclaración aparte, cuando uso un and not va a negar lo que hay adentro
es_hombre = True
es_alto = True

if es_hombre and es_alto:
    print("tu eres un hombre alto")
elif es_hombre and not(es_alto):
    print("tu eres un hombre bajo")
elif not(es_hombre) and es_alto:
    print("tu no eres un hombre pero eres alto")
else:
    print("tu no eres un hombre alto")

es_hombre = False
es_alto = True

if es_hombre and es_alto:
    print("tu eres un hombre alto")
elif es_hombre and not(es_alto):
    print("tu eres un hombre bajo")
elif not(es_hombre) and es_alto:
    print("tu no eres un hombre pero eres alto")
else:
    print("tu no eres un hombre alto")

es_hombre = False
es_alto = False

if es_hombre and es_alto:
    print("tu eres un hombre alto")
elif es_hombre and not(es_alto):
    print("tu eres un hombre bajo")
elif not(es_hombre) and es_alto:
    print("tu no eres un hombre pero eres alto")
else:
    print("tu no eres un hombre alto")

es_hombre = True
es_alto = False

if es_hombre and es_alto:
    print("tu eres un hombre alto")
elif es_hombre and not(es_alto):
    print("tu eres un hombre bajo")
elif not(es_hombre) and es_alto:
    print("tu no eres un hombre pero eres alto")
else:
    print("tu no eres un hombre alto")