#con clases y objetos podemos crear nuestros propios tipos de datos
#cree datos al azar sobre un estudiante en la solapa estudiante y me voy a traer de ahi los datos

from estudiante import Estudiante

estudiante1 = Estudiante("chris", 9.5,  "contador", False)
estudiante2 = Estudiante("seba", 8.2,  "abogado", True)

print(estudiante1.nombre)
print(estudiante1.promedio)
print(estudiante1.escolarizacion)

print(estudiante2.escolarizacion)

