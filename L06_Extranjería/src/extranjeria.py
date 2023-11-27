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
    with open(ruta_fichero, encoding="utf-8") as f:
        archivo = csv.reader(f)
        next(archivo)  # saltamos la cabecera
        return [
            RegistroExtranjeria(i[0], i[1], i[2], i[3], int(i[4]), int(i[5]))
            for i in archivo
        ]


def numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> int:
    return len({i.pais for i in registros})


def secciones_distritos_con_extranjeros_nacionalidades(
    registros: list[RegistroExtranjeria], paises: set[str]
) -> list[tuple[str, str]]:
    # no hace falta "key=" porque por defecto se selecciona el primer elemento de la tupla
    return sorted(
        {(i.distrito, i.seccion) for i in registros if i.pais.upper() in paises}
    )


def total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> dict[str, int]:
    extranjeros_por_pais = typing.DefaultDict(int)
    for i in registros:
        extranjeros_por_pais[i.pais] += i.hombres + i.mujeres

    return extranjeros_por_pais


def top_n_extranjeria(
    registros: list[RegistroExtranjeria], n: int = 3
) -> list[tuple[str, int]]:
    poblacion_por_pais = typing.DefaultDict(int)
    for i in registros:
        poblacion_por_pais[i.pais] += i.hombres + i.mujeres

    return sorted(
        ((pais, poblacion) for pais, poblacion in poblacion_por_pais.items()),
        key=lambda x: x[1],
        reverse=True,
    )[:n]


def barrio_mas_multicultural(registros: list[RegistroExtranjeria]) -> str:
    paises_por_barrio = typing.DefaultDict(set[str])

    for i in registros:
        paises_por_barrio[i.barrio].add(i.pais)

    return max(paises_por_barrio.items(), key=lambda x: len(x[1]))[0]


def barrio_con_mas_extranjeros(
    registros: list[RegistroExtranjeria],
    tipo: typing.Literal["HOMBRES", "MUJERES", None] = None,
) -> str:
    extranjeros_por_barrio = typing.DefaultDict(int)

    if tipo is None:
        for i in registros:
            extranjeros_por_barrio[i.barrio] += i.hombres + i.mujeres
    elif tipo == "HOMBRES":  # no hace falta usar .upper() al tipar con typing.Literal
        for i in registros:
            extranjeros_por_barrio[i.barrio] += i.hombres
    else:
        for i in registros:
            extranjeros_por_barrio[i.barrio] += i.mujeres

    return max(extranjeros_por_barrio.items(), key=lambda x: x[1])[0]


def pais_mas_representado_por_distrito(
    registros: list[RegistroExtranjeria],
) -> dict[str, str]:
    distritos = sorted({i.distrito for i in registros})
    pais_por_distrito = {}

    for distrito in distritos:
        personas_por_pais_en_el_distrito = typing.DefaultDict(int)

        personas_en_el_distrito = [
            (i.pais, i.hombres + i.mujeres) for i in registros if i.distrito == distrito
        ]

        for i in personas_en_el_distrito:
            personas_por_pais_en_el_distrito[i[0]] += i[1]

        pais_por_distrito[distrito] = max(
            personas_por_pais_en_el_distrito.items(), key=lambda x: x[1]
        )[0]

    return pais_por_distrito
