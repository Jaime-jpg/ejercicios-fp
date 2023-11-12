import csv
from datetime import date, time, datetime
from typing import NamedTuple


class Vuelo(NamedTuple):
    destino: str
    precio: float
    num_plazas: int
    num_pasajeros: int
    código: str
    fecha: date
    duración: int
    hora: time
    velocidad: float
    escalas: list[str]
    económico: bool


# no me gusta
#
# from collections import namedtuple
# Vuelo = namedtuple(
#     "Vuelo",
#     "destino, precio, num_plazas, num_pasajeros, código, fecha, duración, hora, velocidad, escalas, económico",
# )


def lee_vuelos(ruta: str) -> list[Vuelo]:
    vuelos = []
    with open(ruta, encoding="utf-8") as file:
        lector = csv.reader(file, delimiter=";")
        next(lector)  # saltar línea de la cabecera
        for línea in lector:
            (
                destino,
                precio,
                num_plazas,
                num_pasajeros,
                código,
                fecha,
                duración,
                hora,
                velocidad,
                escalas,
                económico,
            ) = línea
            destino = destino.strip()
            fecha = datetime.strptime(fecha.strip(), "%d/%m/%Y").date()
            hora = time.fromisoformat(hora.strip())
            duración = int(duración.strip())
            velocidad = float(velocidad.strip())
            precio = float(precio.replace(",", ".").strip())
            num_plazas = int(num_plazas.strip())
            num_pasajeros = int(num_pasajeros.strip())
            escalas = [i.strip() for i in escalas.split("-")[1:]]
            económico = económico.strip() == "S"
            vuelo = Vuelo(
                destino,
                precio,
                num_plazas,
                num_pasajeros,
                código,
                fecha,
                duración,
                hora,
                velocidad,
                escalas,
                económico,
            )
            vuelos.append(vuelo)
    return vuelos


def filtra_vuelos_a(vuelos: list[Vuelo], destino: str) -> list[Vuelo]:
    return [v for v in vuelos if v.destino == destino]


def vuelos_mas_velocidad_que(
    vuelos: list[Vuelo], velocidad_media: float
) -> list[tuple[str, date, float]]:
    return [
        (v.destino, v.fecha, v.velocidad)
        for v in vuelos
        if v.velocidad > velocidad_media
    ]


def todos_vuelos_mas_velocidad_que(vuelos: list[Vuelo], velocidad_media: float) -> bool:
    return all(v.velocidad > velocidad_media for v in vuelos)


def vuelos_más_velocidad(vuelos: list[Vuelo]) -> Vuelo:
    return max(vuelos, key=lambda v: v.velocidad)


def vuelos_por_horario(
    vuelos: list[Vuelo], mes: int
) -> list[tuple[str, float, date, time]]:
    return sorted(
        (
            (v.destino, v.precio, v.fecha, v.hora)
            for v in vuelos
            if v.fecha.month == mes
        ),
        key=lambda x: x[3],
    )


def distintas_escalas(vuelos: list[Vuelo]) -> list[str]:
    escalas_set = set()
    for v in vuelos:
        escalas_set.update(v.escalas)
    return sorted(escalas_set)


def vuelos_con_escalas_en(
    vuelos: list[Vuelo], ciudad_escala: str
) -> list[tuple[str, float, int]]:
    filtered_vuelos = [
        (v.destino, v.precio, v.num_plazas)
        for v in vuelos
        if ciudad_escala in v.escalas or ciudad_escala == v.destino
    ]
    return sorted(filtered_vuelos, key=lambda x: x[1])


def número_de_vuelo_por_destino(vuelos: list[Vuelo]) -> dict:
    destinos_count = {}
    for v in vuelos:
        if v.destino in destinos_count:
            destinos_count[v.destino] += 1
        else:
            destinos_count[v.destino] = 1
    return destinos_count


def suma_de_pasajeros_por_fechas(vuelos: list[Vuelo]) -> dict:
    pasajeros_por_fecha = {}
    for v in vuelos:
        if v.fecha in pasajeros_por_fecha:
            pasajeros_por_fecha[v.fecha] += v.num_pasajeros
        else:
            pasajeros_por_fecha[v.fecha] = v.num_pasajeros
    return pasajeros_por_fecha


def lista_destinos_por_compañía(vuelos: list[Vuelo]) -> dict:
    destinos_por_compañía = {}
    for v in vuelos:
        compañía = v.código[:3]
        if compañía in destinos_por_compañía:
            destinos_por_compañía[compañía].append(v.destino)
        else:
            destinos_por_compañía[compañía] = [v.destino]
    return destinos_por_compañía


def vuelos_entre_fechas(
    vuelos: list[Vuelo], fecha_inicio: date, fecha_fin: date
) -> list[tuple[str, float, list[str]]]:
    return sorted(
        (
            (v.destino, v.precio, v.escalas)
            for v in vuelos
            if (fecha_inicio is None or v.fecha >= fecha_inicio)
            and (fecha_fin is None or v.fecha <= fecha_fin)
        ),
        key=lambda x: x[1],
    )
