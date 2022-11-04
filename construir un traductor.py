#vamos a inventar un idioma, entonces vamos a hacer que todas las vocales cambien por la letra g

#vocales -> g
#dog -> dgg
#cat -> cgt

#en la siguiente formula vamos a poner la frase que queremos traducir:
def translate(frase):
    traduccion = ""
    for letra in frase:
        if letra in "AEIOUaeiou":
            if letra.isupper():
                traduccion = traduccion + "G"
            else:
                traduccion = traduccion + "g"
        else:
            traduccion = traduccion + letra
    return traduccion

print(translate(input("ingresa la frase: ")))