# me niego a usar los métodos obsoletos del módulo typing para tipar
import collections
import datetime
import typing
from datetime import date, datetime
import csv

Equipo = typing.NamedTuple(
    "Equipo", [("nombre", str), ("puntos", int), ("faltas", int)]
)

PartidoBasket = typing.NamedTuple(
    "PartidoBasket",
    [("fecha", date), ("competicion", str), ("equipo1", Equipo), ("equipo2", Equipo)],
)


def parsea_y_suma_resultados(resultados: str) -> tuple[int, int]:
    puntos_por_cuarto = [i.split("-") for i in resultados.split("*")]
    puntos_equipo_1 = sum(int(i[0]) for i in puntos_por_cuarto)
    puntos_equipo_2 = sum(int(i[1]) for i in puntos_por_cuarto)
    return (puntos_equipo_1, puntos_equipo_2)


def lee_partidos(ruta_archivo: str) -> list[PartidoBasket]:
    equipos = []

    with open(ruta_archivo, encoding="utf-8") as f:
        archivo = csv.reader(f, delimiter=";")
        next(archivo)  # omitimos la cabecera
        for fecha, equipo_1, equipo_2, torneo, cuartos, faltas_1, faltas_2 in archivo:
            puntos = parsea_y_suma_resultados(cuartos)
            equipo_1 = Equipo(equipo_1, puntos[0], int(faltas_1))
            equipo_2 = Equipo(equipo_2, puntos[1], int(faltas_2))
            equipos.append(
                PartidoBasket(
                    datetime.strptime(fecha, r"%d/%m/%Y"),
                    torneo,
                    equipo_1,
                    equipo_2,
                )
            )

    return equipos


def equipo_con_mas_faltas(
    partidos: list[PartidoBasket], equipos: set[str] | None = None
) -> tuple[str, int]:
    # me confundí con el enunciado -_-
    # 
    # partido_equipo_1_mas_faltas = max(partidos, key=lambda x: x.equipo1.faltas)
    # partido_equipo_2_mas_faltas = max(partidos, key=lambda x: x.equipo2.faltas)
    # equipo_1_mas_faltas = (
    #     partido_equipo_1_mas_faltas.equipo1.nombre,
    #     partido_equipo_1_mas_faltas.equipo1.faltas,
    # )
    # equipo_2_mas_faltas = (
    #     partido_equipo_2_mas_faltas.equipo2.nombre,
    #     partido_equipo_2_mas_faltas.equipo2.faltas,
    # )
    # return max(equipo_1_mas_faltas, equipo_2_mas_faltas, key=lambda x: x[1])

    # esto está bien:
    faltas_por_equipo = typing.DefaultDict(int)
    for i in partidos:
        if equipos is None or i.equipo1.nombre in equipos:
            faltas_por_equipo[i.equipo1.nombre] += i.equipo1.faltas

        if equipos is None or i.equipo2.nombre in equipos:
            faltas_por_equipo[i.equipo2.nombre] += i.equipo2.faltas

    return max(faltas_por_equipo.items(), key=lambda x: x[1])


def media_puntos_por_equipo(
    partidos: list[PartidoBasket], competicion: str
) -> dict[str, float]:
    puntos_por_equipo = typing.DefaultDict(list[int])
    for i in partidos:
        if i.competicion == competicion:
            puntos_por_equipo[i.equipo1.nombre].append(i.equipo1.puntos)
            puntos_por_equipo[i.equipo2.nombre].append(i.equipo2.puntos)

    return {i: sum(j) / len(j) for i, j in puntos_por_equipo.items()}


def diferencia_puntos_anotados(partidos: list[PartidoBasket], equipo: str) -> list[int]:
    partidos.sort(key=lambda x: x.fecha)
    puntos_por_partido = []

    for i in partidos:
        if i.equipo1.nombre == equipo:
            puntos_por_partido.append(i.equipo1.puntos)
        elif i.equipo2.nombre == equipo:
            puntos_por_partido.append(i.equipo2.puntos)

    return [j - i for i, j in zip(puntos_por_partido, puntos_por_partido[1:])]


def victorias_por_equipo(partidos: list[PartidoBasket]) -> dict[str, int]:
    n_victorias_por_equipo = typing.DefaultDict(int)
    for i in partidos:
        n_victorias_por_equipo[i.equipo1.nombre] += i.equipo1.puntos > i.equipo2.puntos
        n_victorias_por_equipo[i.equipo2.nombre] += i.equipo2.puntos > i.equipo1.puntos

    return n_victorias_por_equipo


def equipos_minimo_victorias(partidos: list[PartidoBasket], n: int) -> list[str]:
    return [
        i[0]
        for i in sorted(
            victorias_por_equipo(partidos).items(), key=lambda x: x[1], reverse=True
        )
        if i[1] >= n
    ]


def equipos_mas_victorias_por_año(
    partidos: list[PartidoBasket], n: int
) -> dict[int, list[str]]:
    años = tuple({i.fecha.year for i in partidos})
    mejores_por_año = {}
    for año in años:
        partidos_filtrados = [i for i in partidos if i.fecha.year == año]
        mejores_por_año[año] = equipos_minimo_victorias(partidos_filtrados, n)

    return mejores_por_año