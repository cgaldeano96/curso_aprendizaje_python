#Esto va a tomar 3 parametros como entrada y las va a imprimir, estamos comparando 3 valores distintos

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(50, 80, 500))

#no importa cual de los numeros termina siendo el mas grande, va a terminar agarrando ese la formula
#se puede usar un != que significa no es igual, o un == que significa que es igual