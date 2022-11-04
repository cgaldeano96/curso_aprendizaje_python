#para abrir un txt o colocamos la ruta o lo abrimos en python
#el simbolo r es para lectura solamente, no va a modificarlo ni nada
#el simbolo w significa que puedo cambiar lo que hay adentro del archivo
#el simbolo a significa que puedo agregar información al final del archivo pero no modificar lo que ya tenga adentro
#el simbolo r+ que significa lee y le escribe encima

file_empleados = open("venv\empleados.txt", "r")

print(file_empleados.read())

