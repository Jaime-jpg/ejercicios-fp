import typing
import csv

# from collections import namedtuple
# RegistroExtranjeria = namedtuple('RegistroExtranjeria', 'distrito,seccion,barrio,pais,hombres,mujeres')


class RegistroExtranjeria(typing.NamedTuple):
    distrito: str
    seccion: str
    barrio: str
    pais: str
    hombres: int
    mujeres: int


def lee_datos_extranjeria(ruta_fichero: str) -> list[RegistroExtranjeria]:
    # recibe la ruta del fichero CSV, devolviendo una lista de tuplas de tipo RegistroExtranjeria con toda la información contenida en el fichero.
    with open(ruta_fichero, encoding="utf-8") as f:
        archivo = csv.reader(f)
        next(archivo)  # saltamos la cabecera
        return [
            RegistroExtranjeria(i[0], i[1], i[2], i[3], int(i[4]), int(i[5]))
            for i in archivo
        ]


def numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> int:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el número de nacionalidades distintas presentes en los registros de la lista recibida como parámetro.
    return len({i.pais for i in registros})


def secciones_distritos_con_extranjeros_nacionalidades(
    registros: list[RegistroExtranjeria], paises: set[str]
) -> list[tuple[str, str]]:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y un conjunto de cadenas con nombres de países, y devuelve una lista de tuplas (distrito, seccion) con los distritos y secciones en los que hay extranjeros del conjunto de paises dado como parámetro. La lista de tuplas devuelta estará ordenada por distrito.
    # no hace falta "key=" porque por defecto se selecciona el primer elemento de la tupla
    return sorted(
        {(i.distrito, i.seccion) for i in registros if i.pais.upper() in paises}
    )


def total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> dict[str, int]:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve un diccionario de tipo {str:int} en el que las claves son los países y los valores son el número total de extranjeros (tanto hombres como mujeres) de cada país.
    extranjeros_por_pais = typing.DefaultDict(int)
    for i in registros:
        extranjeros_por_pais[i.pais] += i.hombres + i.mujeres

    return extranjeros_por_pais


def top_n_extranjeria(
    registros: list[RegistroExtranjeria], n: int = 3
) -> list[tuple[str, int]]:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve una lista de tuplas (pais, numero_extranjeros) con los n países de los que hay más población extranjera en los registros pasados como parámetros.
    poblacion_por_pais = typing.DefaultDict(int)
    for i in registros:
        poblacion_por_pais[i.pais] += i.hombres + i.mujeres

    return sorted(
        ((pais, poblacion) for pais, poblacion in poblacion_por_pais.items()),
        key=lambda x: x[1],
        reverse=True,
    )[:n]


def barrio_mas_multicultural(registros: list[RegistroExtranjeria]) -> str:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el nombre del barrio en el que hay un mayor número de países de procedencia distintos.
    paises_por_barrio = typing.DefaultDict(set[str])

    for i in registros:
        paises_por_barrio[i.barrio].add(i.pais)

    return max(paises_por_barrio.items(), key=lambda x: len(x[1]))[0]


def barrio_con_mas_extranjeros(
    registros: list[RegistroExtranjeria],
    tipo: typing.Literal["Hombres", "Mujeres", None] = None,
) -> str:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el nombre del barrio en el que hay un mayor número de extranjeros, bien sea en total (tanto hombres como mujeres) si tipo tiene el valor None, bien sea de hombres si tipo es 'Hombres', o de mujeres si tipo es 'Mujeres'.
    extranjeros_por_barrio = typing.DefaultDict(int)

    if tipo is None:
        for i in registros:
            extranjeros_por_barrio[i.barrio] += i.hombres + i.mujeres
    elif tipo.upper() == "Hombres":
        for i in registros:
            extranjeros_por_barrio[i.barrio] += i.hombres
    else:
        for i in registros:
            extranjeros_por_barrio[i.barrio] += i.mujeres
    
    return max(extranjeros_por_barrio.items(), key=lambda x: x[1])[0]
        


def pais_mas_representado_por_distrito(registros):
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve un diccionario de tipo {str:str} en el que las claves son los distritos y los valores los países de los que hay más extranjeros residentes en cada distrito.
    ...
