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
    juegos_j1, juegos_j2 = cadena_parcial.split("-")
    return Parcial(int(juegos_j1), int(juegos_j2))


def lee_partidos_tenis(ruta_csv: str) -> list[PartidoTenis]:
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
    return min(partidos, key=lambda x: x.errores_nf1 + x.errores_nf2)


def jugador_mas_partidos(partidos: list[PartidoTenis]) -> tuple[str, int]:
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
    jugadores_por_superficie = typing.DefaultDict(set[str])
    for i in partidos:
        jugadores_por_superficie[i.superficie].update((i.jugador1, i.jugador2))

    return {i: len(j) for i, j in jugadores_por_superficie.items()}


def superficie_con_mas_tenistas_distintos(
    partidos: list[PartidoTenis],
) -> tuple[str, int]:
    return max(
        num_tenistas_distintos_por_superficie(partidos).items(), key=lambda x: x[1]
    )


def mas_errores_por_jugador(partidos: list[PartidoTenis]) -> dict[str, PartidoTenis]:
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
    partidos_filtrados = [i for i in partidos if jugador in (i.jugador1, i.jugador2)]
    diferencia_de_dias = []
    for i, j in zip(partidos_filtrados, partidos_filtrados[1:]):
        diferencia_de_dias.append((j.fecha - i.fecha).days)
    
    return max(diferencia_de_dias)
