import typing
import collections
from datetime import datetime, date
import csv

Parcial = typing.NamedTuple("Parcial", [("juegos_j1", int), ("juegos_j2", int)])

PartidoTenis = typing.NamedTuple(
    "PartidoTenis",
    [
        ("fecha", date),
        ("jugador1", str),
        ("jugador2", str),
        ("superficie", str),
        ("resultado", list[Parcial]),
        ("errores_nf1", int),
        ("errores_nf2", int),
    ],
)


def parsea_set(cadena_parcial: str) -> Parcial:
    # Toma una cadena con el resultado de un set o parcial y devuelve una tupla de tipo Parcial que representa ese set. La cadena de entrada se espera que tenga los juegos del set del primer jugador, seguido de un guión y los juegos del set del segundo jugador, es decir, int-int.
    juegos_j1, juegos_j2 = cadena_parcial.split("-")
    return Parcial(int(juegos_j1), int(juegos_j2))


def lee_partidos_tenis(ruta_csv: str) -> list[PartidoTenis]:
    # lee un fichero de entrada en formato CSV codificado en UTF-8 y devuelve una lista de tuplas de tipo PartidoTenis conteniendo todos los datos almacenados en el fichero. Le puede ser de ayuda la función datetime.strptime(cadena, '%d/%m/%Y') para el parseo de fechas. Para implementar esta función defina la siguiente función auxiliar:
    partidos = []

    with open(ruta_csv, encoding="utf-8") as f:
        archivo = csv.reader(f, delimiter=";")

        for i in archivo:
            (
                fecha,
                jugador1,
                jugador2,
                superficie,
                *parciales,  # equivale a escribir: parcial_1, parcial_2, parcial_3,
                errores_nf1,
                errores_nf2,
            ) = i

            partidos.append(
                PartidoTenis(
                    datetime.strptime(fecha, r"%d/%m/%Y").date(),
                    jugador1,
                    jugador2,
                    superficie,
                    [parsea_set(i) for i in parciales],
                    int(errores_nf1),
                    int(errores_nf2),
                )
            )
    return partidos


def partidos_menos_errores(partidos: list[PartidoTenis]) -> PartidoTenis:
    # recibe una lista de tipo PartidoTenis y devuelve el partido con mayor némero de errores no forzados entre los dos jugadores.
    return min(partidos, key=lambda x: x.errores_nf1 + x.errores_nf2)


def jugador_mas_partidos(partidos: list[PartidoTenis]) -> tuple[str, int]:
    # recibe una lista de tipo PartidoTenis y devuelve una tupla con el nombre del jugador que más partidos ha jugado y el némero de partidos.
    partidos_por_jugador = typing.DefaultDict(int)
    for i in partidos:
        partidos_por_jugador[i.jugador1] += 1
        partidos_por_jugador[i.jugador2] += 1

    return max(partidos_por_jugador.items(), key=lambda x: x[1])


def ganador(partido: PartidoTenis) -> str:
    victorias_jugador1 = sum(i.juegos_j1 > i.juegos_j2 for i in partido.resultado)
    return partido.jugador1 if victorias_jugador1 >= 2 else partido.jugador2


def tenista_mas_victorias(
    partidos: list[PartidoTenis], inicio: date | None = None, fin: date | None = None
) -> tuple[str, int] | None:
    # recibe una lista de tuplas de tipo PartidoTenis, y dos fechas, ambas de tipo date, y con valor por defecto None. Devuelve el nombre del tenista que ha tenido más victorias en los partidos jugados entre las fechas (ambas inclusive). Si la primera fecha es None, la función devuelve el tenista con más victorias hasta esa fecha (inclusive). Si la segunda fecha es None, la función devuelve el tenista con más victorias desde esa fecha (inclusive). Finalmente, si las dos fechas son None, la función devuelve el tenista con más victorias de toda la lista, independientemente de la fecha. Para implementar esta función defina la siguiente función auxiliar: a. ganador:** recibe una tupla de tipo PartidoTenis y devuelve el nombre del jugador que ganó ese partido.
    partidos_entre_fechas = (
        i
        for i in partidos
        if ((inicio is None) or (inicio <= i.fecha))
        and ((fin is None) or (i.fecha <= fin))
    )

    if not partidos_entre_fechas:
        return None

    victorias_por_tenista = typing.DefaultDict(int)
    for partido in partidos_entre_fechas:
        victorias_por_tenista[ganador(partido)] += 1

    return max(victorias_por_tenista.items(), key=lambda x: x[1])


def media_errores_por_jugador(partidos: list[PartidoTenis]) -> list[tuple[str, float]]:
    # recibe una lista de tuplas de tipo PartidoTenis y devuelve una lista de tuplas ordenadas con el nombre de cada jugador y su media de errores no forzados. La lista estará ordenada por la media de errores de menor a mayor.
    errores_por_jugador = typing.DefaultDict(list[int])

    for partido in partidos:
        errores_por_jugador[partido.jugador1].append(partido.errores_nf1)
        errores_por_jugador[partido.jugador2].append(partido.errores_nf2)

    return sorted(
        ((i, sum(j) / len(j)) for i, j in errores_por_jugador.items()),
        key=lambda x: x[1],
    )


def jugadores_mayor_porcentaje_victorias(
    partidos: list[PartidoTenis],
) -> list[tuple[str, float]]:
    # recibe una lista de tuplas de tipo PartidoTenis y devuelve una lista de tuplas con el nombre de cada jugador y el porcentaje de victorias. La lista estará ordenada por el porcentaje de victorias de mayor a menor.
    jugadores = set()

    for partido in partidos:
        jugadores.update({partido.jugador1, partido.jugador2})

    partidos_por_jugador = typing.DefaultDict(int)
    victorias_por_jugador = typing.DefaultDict(int)

    for i in partidos:
        partidos_por_jugador[i.jugador1] += 1
        partidos_por_jugador[i.jugador2] += 1
        victorias_por_jugador[ganador(i)] += 1

    return sorted(
        (
            (i, victorias_por_jugador[i] / partidos_por_jugador[i])
            for i in tuple(jugadores)
            # conversión a tupla para que al iterar vaya _un poco_ más rápido,
            # también se podría usar sorted(jugadores) para tenerlos ordenados por
            # orden alfabético
        ),
        key=lambda x: x[1],
        reverse=True,
    )


def n_tenistas_con_mas_errores(
    partidos: list[PartidoTenis], n: int | None
) -> list[tuple[str, int]]:
    # recibe una lista de tuplas de tipo PartidoTenis y un némero n, con valor por defecto None, y devuelve una lista con los nombres de los n tenistas que han acumulado más errores no forzados en el total de partidos que han jugado. Si n es None, entonces devuelve todos los tenistas de la lista de tuplas ordenados de mayor a menor némero de errores no forzados. (2 puntos)
    errores_por_jugador = typing.DefaultDict(int)

    for i in partidos:
        errores_por_jugador[i.jugador1] += i.errores_nf1
        errores_por_jugador[i.jugador2] += i.errores_nf2

    lista_errores_por_jugador = sorted(
        errores_por_jugador.items(), key=lambda x: x[1], reverse=True
    )

    if n is None:
        return lista_errores_por_jugador

    return lista_errores_por_jugador[:n]


def fechas_ordenadas_por_jugador(partidos: list[PartidoTenis]) -> dict[str, list[date]]:
    # recibe una lista de tuplas de tipo PartidoTenis y devuelve un diccionario en el que a cada jugador le hace corresponder una lista ordenada con las fechas de sus partidos.
    partidos.sort(key=lambda x: x.fecha)
    partidos_por_jugador = typing.DefaultDict(list[date])

    for i in partidos:
        partidos_por_jugador[i.jugador1].append(i.fecha)
        partidos_por_jugador[i.jugador2].append(i.fecha)

    return partidos_por_jugador


def num_partidos_nombre(
    partidos: list[PartidoTenis], tenista: str
) -> dict[str, tuple[int, int]]:
    resultados_por_superficie = collections.defaultdict(lambda: (int(), int()))

    for partido in partidos:
        if tenista not in (partido.jugador1, partido.jugador2):
            continue

        es_ganador = ganador(partido) == tenista
        partidos_jugados, partidos_ganados = resultados_por_superficie[
            partido.superficie
        ]
        resultados_por_superficie[partido.superficie] = (
            partidos_jugados + 1,
            partidos_ganados + es_ganador,
        )

    return resultados_por_superficie


def num_tenistas_distintos_por_superficie(
    partidos: list[PartidoTenis],
) -> dict[str, int]:
    # recibe una lista de tuplas de tipo PartidoTenis, y devuelve un diccionario tal que a cada superficie (clave) le hace corresponder el némero de jugadores distintos que han jugado partidos en ese tipo de superficie. (1,5 puntos)
    jugadores_por_superficie = typing.DefaultDict(set[str])
    for i in partidos:
        jugadores_por_superficie[i.superficie].update((i.jugador1, i.jugador2))

    return {i: len(j) for i, j in jugadores_por_superficie.items()}


def superficie_con_mas_tenistas_distintos(
    partidos: list[PartidoTenis],
) -> tuple[str, int]:
    # recibe una lista de tuplas de tipo PartidoTenies y devuelve una tupla con la superficie en la que juegan un mayor némero de jugadores distintos, y el némero de jugadores que han jugado en esa superficie.
    return max(
        num_tenistas_distintos_por_superficie(partidos).items(), key=lambda x: x[1]
    )


def mas_errores_por_jugador(partidos: list[PartidoTenis]) -> dict[str, PartidoTenis]:
    # recibe una lista de tuplas de tipo PartidoTenis y devuelve un diccionario en el que a cada jugador y le hace corresponder el partido en el que ha cometido mayor némero de errores no forzados.
    partido_por_jugador = {}
    for i in partidos:
        if i.jugador1 not in partido_por_jugador or (
            i.errores_nf1 > partido_por_jugador[i.jugador1].errores_nf1
        ):
            partido_por_jugador[i.jugador1] = i

        if i.jugador2 not in partido_por_jugador or (
            i.errores_nf2 > partido_por_jugador[i.jugador2].errores_nf2
        ):
            partido_por_jugador[i.jugador2] = i

    return partido_por_jugador


def partido_mas_errores_por_mes(
    partidos: list[PartidoTenis], superficies: list[str] | None
) -> dict[int, tuple[date, str, str]]:
    # recibe una lista de tuplas de tipo PartidoTenis, y una lista de cadenas con tipos de superficie, que toma como valor por defecto None, y devuelve un diccionario que asocia a cada mes, una tupla (fecha del partido, jugador1, jugador2) que representa al partido de ese mes jugado en una de las superficies de la lista dada como parámetro en el que se han cometido más errores no forzados, teniendo en cuenta los errores de ambos jugadores. Si la lista de superficies dada como parámetro tiene como valor None, entonces se tendrán en cuenta todas las superficies para generar el diccionario resultante. (2 puntos).
    partido_por_mes = {}
    max_errores_por_mes = typing.DefaultDict(int)
    for i in partidos:
        errores = i.errores_nf1 + i.errores_nf2
        if (superficies and i.superficie in superficies) and (
            (i.fecha.month not in partido_por_mes)
            or (errores > max_errores_por_mes[i.fecha.month])
        ):
            max_errores_por_mes[i.fecha.month] = errores
            partido_por_mes[i.fecha.month] = (i.fecha, i.jugador1, i.jugador2)

    return partido_por_mes


def n_partidos_mas_errores_por_jugador(
    partidos: list[PartidoTenis], n: int
) -> dict[str, list[PartidoTenis]]:
    # recibe una lista de tuplas de tipo PartidoTenis y un valor entero n y devuelve un diccionario en el que a cada jugador le hace corresponder una lista con los n partidos en los que ha cometido más errores no forzados.
    partidos_por_jugador = typing.DefaultDict(list[tuple[PartidoTenis, int]])

    for i in partidos:
        partidos_por_jugador[i.jugador1].append((i, i.errores_nf1))
        partidos_por_jugador[i.jugador2].append((i, i.errores_nf2))

    for i in partidos_por_jugador.values():
        i.sort(key=lambda x: x[1], reverse=True)

    return {
        i: [partido for partido, _ in j][:n] for i, j in partidos_por_jugador.items()
    }


def mayor_numero_dias_sin_jugar(partidos: list[PartidoTenis], jugador: str) -> int:
    # recibe una lista de partidos y un jugador y devuelve el máximo némero de días sin jugar del jugador dado. Si el jugador solo ha disputado un partido devolverá None.
    partidos_filtrados = [i for i in partidos if jugador in (i.jugador1, i.jugador2)]
    diferencia_de_dias = []
    for i, j in zip(partidos_filtrados, partidos_filtrados[1:]):
        diferencia_de_dias.append((j.fecha - i.fecha).days)
    
    return max(diferencia_de_dias)
