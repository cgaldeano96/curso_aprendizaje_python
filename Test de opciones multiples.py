#vamos a hacer un test con opciones multiples
#voy a crear una solapa que sea preguntas y voy a armar el archivo

from preguntas import Preguntas
preguntas_rapidas = [
    "de que color son las manzanas?\n(a) Rojas/Verdes\n(b) Purpuras\n(c) Naranjas\n\n",
    "de que color son las bananas?\n(a) Grises\n(b) Magentas\n(c) Amarillas\n\n",
    "de que color son las frambuesas?\n(a) Amarillas\n(b) Rojas\n(c) Azules\n\n",
]

preguntas = [
    pregunta(preguntas_rapidas[0], "a")
    ]