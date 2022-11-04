#Funciones, basicamente es una coleccion de codigos, te ayuda a organizar y a dividir tu codigo
#para crear una funcion voy a usar el def
#Todo el codigo que venga despues de esta linea va a ser dentro de nuestra funcion
#Una vez puesta esa funcion abajo va a ir con sangria dentro del codigo
#Cuando la sangria deje de existir es que ya no pertenece a esa funcion/codigo

def di_hola():
    print("hola user")

#No va a imprimir nada porque no esta llamando la funcion, para que la llame hay que poner lo mismo que arriba
di_hola()

#por ejemplo vamos a imprimir otras palabras que no esten arriba, en el medio python va a ir a buscar la posición de arriba
#Con esa funcion va a llamar a la linea de arriba y va a imprimir todo el codigo que hayamos puesto
print("top")
di_hola()
print("boton")

#Podemos cambiar para que diga nombre y edad
def di_hola(nombre, edad):
    print("hola" + nombre + ", tu tienes "+ edad)

di_hola("mike", "35")
di_hola("jim", "70")

#esto es bueno para dividir el codigo, cada vez que preciso dividirlo puedo usar estas funciones


