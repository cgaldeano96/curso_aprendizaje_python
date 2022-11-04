#almacenaremos una variable con una palabra secreta
palabra_secreta = "jirafa"
adivinar = ""
contar_adivinanza = 0
limite_adivinar = 3
fuera_de_juego = False

while adivinar != palabra_secreta and not (fuera_de_juego):
    if contar_adivinanza < limite_adivinar:
        adivinar = input("ingresar la adivinanza:")
        contar_adivinanza += 1
    else:
        fuera_de_juego = True

if fuera_de_juego:
    print("fuera de juego, perdiste!")
else:
    print("haz ganado!")

#mientras no pongamos la palabra correcta nos hara seguir intentando, cuando pongamos la palabra clave nos va a decir que hemos ganado

#podemos limitar la cantidad de fallos que tenga el user

