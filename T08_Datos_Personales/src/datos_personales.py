from collections import namedtuple


Persona = namedtuple("Persona", "dni, nombre, apellidos, edad, ciudad, provincia")


def filtrar_por_edad(personas: list[Persona], edad: int) -> list[Persona]:
    return [i for i in personas if i.edad < edad]


def obtener_nombre_y_dni(personas: list[Persona]) -> list[tuple[str, str]]:
    return [(i.dni, i.nombre) for i in personas]


def obtiene_edades_distintas(personas: list[Persona]) -> int:
    """Solución sencilla"""
    return len({i.edad for i in personas})


def obtiene_edades_distintas2(personas: list[Persona]) -> int:
    """Solución optimizada (en realidad es más lenta en Python, pero en lenguajes de programación de bajo nivel es mucho más rápida)"""
    edades = 0
    for i in personas:
        edades |= (1 << (i.edad))

    return edades.bit_count()
