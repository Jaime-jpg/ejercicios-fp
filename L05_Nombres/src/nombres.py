# ADVERTENCIA:
# ESTE PROYECTO LO HE REALIZADO TOMÁNDOME LIBERTADES RESPECTO A LOS ENUNCIADOS
# Y, EN OCASIONES UTILIZANDO LOS MÉTODOS QUE CONSIDERO MEJORES EN VEZ DE LOS ESPECIFICADOS
# EN DICHOS ENUNCIADOS

import typing
import csv

# FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')


class FrecuenciaNombre(typing.NamedTuple):
    año: int
    nombre: str
    frecuencia: int
    genero: str


def leer_frecuencias_nombres(archivo_csv: typing.TextIO) -> list[FrecuenciaNombre]:
    datos = csv.reader(archivo_csv)
    next(datos)  # omitimos la cabecera

    return [FrecuenciaNombre(int(i[0]), i[1], int(i[2]), i[3]) for i in datos]


def filtrar_por_genero(
    frecuencias_nombre: list[FrecuenciaNombre], genero: str
) -> list[FrecuenciaNombre]:
    return [i for i in frecuencias_nombre if i.genero == genero]


def calcular_nombres(
    frecuencias_nombre: list[FrecuenciaNombre], genero: typing.Optional[str] = None
) -> set[str]:
    if genero is None:
        return {i.nombre for i in frecuencias_nombre}

    return {i.nombre for i in frecuencias_nombre if i.genero == genero}


def calcular_top_nombres_de_año(
    frecuencias_nombre: list[FrecuenciaNombre],
    año: int,
    limite: int = 10,
    genero: typing.Optional[str] = None,
) -> list[tuple[str, int]]:
    filtro = lambda x: (x.año == año) and ((genero is None) or (x.genero == genero))
    return sorted(
        ((i.nombre, i.frecuencia) for i in frecuencias_nombre if filtro(i)),
        key=lambda x: x[1],
        reverse=True,
    )[:limite]


with open("L05_Nombres/data/frecuencias_nombres.csv", encoding="utf-8") as f:
    print(calcular_top_nombres_de_año(leer_frecuencias_nombres(f), 2002))


def calcular_nombres_ambos_generos(
    frecuencias_nombre: list[FrecuenciaNombre],
) -> set[str]:
    nombres_hombre = {i.nombre for i in frecuencias_nombre if i.genero == "Hombre"}
    nombres_mujer = {i.nombre for i in frecuencias_nombre if i.genero == "Mujer"}
    return nombres_hombre & nombres_mujer


def calcular_nombre_mas_frecuente_por_año(
    frecuencias_nombre: list[FrecuenciaNombre], genero: typing.Optional[str] = None
) -> list[tuple[int, str, int]]:
    ...
