#tengo que poner el float lo que va a ser que tenga que poner si o si un numero sino va a fallar

num1 = float(input("ingresar el primer numero: "))
op = input("ingresar operador: ")
num2 = float(input("ingresar el segundo numero: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("operador invalido")