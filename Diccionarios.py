#Un diccionario es una estructura especial de python que nos permite almacenar información
#Las almacena en llaves pares de valores
#las llaves no tienen que repetirse sino nos va a tirar un error de valor duplicado
Conversion_de_mes = {
    "ene": "Enero",
    "Feb": "Febrero",
    "mar": "Marzo",
    "abr": "abril",
    "may": "mayo",
    "jun": "junio",
    "jul": "julio",
    "ago": "agosto",
    "sep": "septiembre",
    "oct": "octubre",
    "nov": "noviembre",
    "dic": "diciembre",
}


print(Conversion_de_mes["nov"])
print(Conversion_de_mes.get("dic"))

#si quiero poner algun valor que no este en el diccionario puedo alargar la formula para que me diga que no es un valor valido
print(Conversion_de_mes.get("chu", "no es un valor valido"))