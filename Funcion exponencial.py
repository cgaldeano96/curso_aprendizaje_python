#como construir una funcion exponencial, nos va a permitir tomar un numero y elevarlo a una potencia
#la forma mas facil es:

print(2**3)

#pero vamos a ver como con una funcion en bucle for poder crear una funcion como esta:
#el return por cada vez que lo hago lo hace al cuadrado, al cubo, etc
# return base_num * base_num * base_num

def elevar_la_formula(base_num, pow_num):
    resultado = 1
    for index in range(pow_num):
        resultado = resultado * base_num
    return resultado


print(elevar_la_formula(3, 2))
print(elevar_la_formula(3, 4))