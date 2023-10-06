from collections import namedtuple
import csv


Persona = namedtuple(
    "Persona", "dni, nombre, apellidos, edad, estatura, peso, localidad, provincia"
)

Persona2 = namedtuple(
    "Persona2",
    "dni, nombre, apellidos, edad, estatura, peso, localidad, provincia, esmujer",
)

Persona3 = namedtuple(
    "Persona2",
    "dni, nombre, apellidos, edad, estatura, peso, localidad, provincia, esmujer, hobbies",
)


def filtrar_por_edad(personas: list[Persona], edad: int) -> list[Persona]:
    return [i for i in personas if i.edad < edad]


def obtener_nombre_y_dni(personas: list[Persona]) -> list[Persona]:
    return [(i.dni, i.nombre) for i in personas]


def obtiene_edades_distintas(personas: list[Persona]) -> list[Persona]:
    """Solución sencilla"""
    return len({i.edad for i in personas})


def obtiene_edades_distintas2(personas: list[Persona]) -> list[Persona]:
    """
    Solución optimizada (en realidad es más lenta en Python, pero
    en lenguajes de programación de bajo nivel es mucho más rápida)
    """
    edades = 0
    for i in personas:
        edades |= 1 << (i.edad)

    return edades.bit_count()


def lee_datos_personales(ruta_archivo: str) -> list[Persona]:
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        no_cabecera = csv.reader(f, delimiter=";")
        next(no_cabecera)
        return [
            Persona(i[0], i[1], i[2], int(i[3]), float(i[4]), float(i[5]), i[6], i[7])
            for i in no_cabecera
        ]


def lee_datos_personales2(ruta_archivo: str) -> list[Persona2]:
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        no_cabecera = csv.reader(f, delimiter=";")
        next(no_cabecera)
        return [
            Persona2(
                i[0],
                i[1],
                i[2],
                int(i[3]),
                float(i[4]).replace(",", "."),
                float(i[5].replace(",", ".")),
                i[6],
                i[7],
                i[8] == "SI",
            )
            for i in no_cabecera
        ]
        

def lee_datos_personales3(ruta_archivo: str) -> list[Persona3]:
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        no_cabecera = csv.reader(f, delimiter=";")
        next(no_cabecera)
        return [
            Persona3(
                i[0],
                i[1],
                i[2],
                int(i[3]),
                float(i[4]),
                float(i[5].replace(",", ".")),
                i[6],
                i[7],
                i[8] == "SI",
                i[9].split("/"),
            )
            for i in no_cabecera
        ]


