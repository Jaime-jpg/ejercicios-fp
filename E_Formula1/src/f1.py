from collections import namedtuple
import collections
from datetime import date, datetime
import csv
import typing

Carrera = namedtuple(
    "Carrera",
    "nombre,escuderia,fecha_carrera,temperatura_min,vel_max,duracion,posicion_final,ciudad,top_6_vueltas,tiempo_boxes,nivel_liquido",
)


def lee_carreras(ruta: str) -> list[Carrera]:
    carreras = []
    with open(ruta, encoding="utf-8") as f:
        archivo = csv.reader(f, delimiter=";")
        next(archivo)  # omitimos cabecera
        for linea in archivo:
            top_6_vueltas = [
                float(tiempo_vuelta) if tiempo_vuelta != "-" else 0
                for tiempo_vuelta in linea[8].strip("[]").split("/ ")
            ]
            nivel_liquido = linea[10] == "1"
            carrera = Carrera(
                linea[0],
                linea[1],
                datetime.strptime(linea[2], r"%d-%m-%y").date(),
                int(linea[3]),
                float(linea[4]),
                float(linea[5]),
                int(linea[6]),
                linea[7],
                top_6_vueltas,
                float(linea[9]),
                nivel_liquido,
            )
            carreras.append(carrera)
    return carreras


def media_tiempo_boxes(
    carreras: list[Carrera], ciudad: str, fecha: date | None = None
) -> float:
    total_tiempo_boxes = 0
    total_carreras = 0
    for carrera in carreras:
        if ciudad == carrera.ciudad and (
            fecha is None or fecha == carrera.fecha_carrera
        ):
            total_tiempo_boxes += carrera.tiempo_boxes
            total_carreras += 1
    return total_tiempo_boxes / total_carreras if total_carreras else 0


def pilotos_menor_tiempo_medio_vueltas_top(
    carreras: list[Carrera], n: int
) -> list[tuple[str, date, float]]:
    carreras.sort(key=lambda x: sum(x.top_6_vueltas) / len(x.top_6_vueltas))
    pilotos_tiempo_medio = []
    for carrera in carreras:
        if carrera.posicion_final != -1 and len(carrera.top_6_vueltas) >= 6:
            tiempo_medio = sum(carrera.top_6_vueltas) / 6
            pilotos_tiempo_medio.append(
                (carrera.nombre, carrera.fecha_carrera, tiempo_medio)
            )

    pilotos_tiempo_medio.sort(key=lambda x: x[1])
    return [i[:2] for i in pilotos_tiempo_medio][:n]


def ratio_tiempo_boxes_total(carreras: list[Carrera]) -> list[tuple[str, date, float]]:
    fechas = tuple({i.fecha_carrera for i in carreras})
    res = []

    for fecha in fechas:
        carrera_en_fecha = [i for i in carreras if i.fecha_carrera == fecha]
        total_en_boxes = sum(i.tiempo_boxes for i in carrera_en_fecha)
        for i in carrera_en_fecha:
            res.append((i.nombre, fecha, i.tiempo_boxes / total_en_boxes))

    return sorted(res, key=lambda x: x[2], reverse=True)


def puntos_piloto_anyos(carreras: list[Carrera]) -> dict[str, list[int]]:
    puntos_por_piloto_por_año = collections.defaultdict(lambda: typing.DefaultDict(int))
    for carrera in carreras:
        if carrera.posicion_final in (1, 2, 3):
            puntos = (50, 25, 10)[carrera.posicion_final - 1]
            puntos_por_piloto_por_año[carrera.nombre][carrera.fecha_carrera.year] += puntos

    return {
        piloto: [i for _, i in sorted(puntuaciones.items(), key=lambda x: x[0])]
        for piloto, puntuaciones in puntos_por_piloto_por_año.items()
    }


def mejor_escuderia_anyo(carreras: list[Carrera], año: int) -> str:
    victorias_por_escuderia = typing.DefaultDict(int)
    for carrera in carreras:
        if carrera.fecha_carrera.year == año and carrera.posicion_final == 1:
            victorias_por_escuderia[carrera.escuderia] += 1

    if victorias_por_escuderia:
        return max(victorias_por_escuderia, key=victorias_por_escuderia.get)
    else:
        return "No hay victorias en el año especificado"
