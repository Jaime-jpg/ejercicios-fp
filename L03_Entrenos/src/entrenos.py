import csv
from collections import namedtuple
from datetime import datetime, date, time
from typing import Union

Entreno = namedtuple(
    "Entreno",
    "tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido",
)


def _a_booleano(compartido: str) -> bool:
    """Funcion inutil (pues es solo una línea de código) que hago porque me lo indica el enunciado"""
    return compartido == "S"


def lee_entrenos(ruta_archivo: str) -> list[Entreno]:
    with open(ruta_archivo, encoding="utf-8") as f:
        archivo = csv.reader(f)
        next(archivo)  # quitamos la cabecera
        return [
            Entreno(
                i[0],
                datetime.strptime(i[1], "%d/%m/%Y %H:%M"),
                i[2],
                int(i[3]),
                int(i[4]),
                float(i[5]),
                int(i[6]),
                _a_booleano(i[7]),  # i[7] == "S" es más corto y rápido
            )
            for i in archivo
        ]


def filtra_por_ubicacion(entrenos: list[Entreno], ubicacion: str) -> list[Entreno]:
    return [i for i in entrenos if i.ubicacion == ubicacion]


def _fecha_en_intervalo(
    fecha: date,
    fecha_inicio: date,
    fecha_fin: date,
) -> bool:
    return fecha_inicio <= fecha < fecha_fin


def tipos_entrenamiento(
    entrenos: list[Entreno],
    fecha_inicio: Union[date, None],
    fecha_fin: Union[date, None],
) -> int:
    fecha_inicio = fecha_inicio or date.min  # eliminamos los None
    fecha_fin = fecha_fin or date.max

    return sum(
        1
        for i in entrenos
        if _fecha_en_intervalo(i.fechahora.date(), fecha_inicio, fecha_fin)
    )


def _momento_dia(entreno: Entreno) -> str:
    if time(7) <= entreno.fechahora.time() < time(14):
        return "MAÑANA"
    if time(14) <= entreno.fechahora.time() < time(21):
        return "TARDE"

    return "NOCHE"


def distancia_total_de_momento_dia(
    entrenos: list[Entreno],
    var_momento_dia: str,  # para este parámetro sería más conveniente usar un Enum
):
    return sum(i.distancia for i in entrenos if _momento_dia(i) == var_momento_dia)
