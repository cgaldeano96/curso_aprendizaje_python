#basicamente lo que digo es si no ingreso un numero por ejemplo, me va a tirar error
#entonces como tira error pongo el except y que salga el error de input invalido

try:
    respuesta = 10/0
    numero = int(input("ingresar un numero"))
    print(numero)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("input invalido")

#el except es muy amplio y para nada especifico, es por eso que se usan except puntuales
#como por ejemplo except zerodivisionerror que hace que la division que da 0 no me la tome como codigo de error de python
#luego esta valueerror y otras.
#como estoy haciendo un resputa = 10/0, lo cual es 0 y es error para el programa me tira como rta division by zero.
