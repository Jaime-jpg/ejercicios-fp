from collections import namedtuple
from math import sqrt, radians
import math


Coordenadas = namedtuple("Coordenadas", "latitud, longitud")


def calcular_distancia(coordenada1: Coordenadas, coordenada2: Coordenadas) -> float:
    return sqrt(
        (coordenada1.latitud - coordenada2.latitud) ** 2
        + (coordenada1.longitud - coordenada2.longitud) ** 2
    )


def calcular_media_coordenadas(coordenadas: list[Coordenadas]) -> Coordenadas:
    return Coordenadas(
        sum(i.latitud for i in coordenadas) / len(coordenadas),
        sum(i.longitud for i in coordenadas) / len(coordenadas),
    )


def distancia_harvesine(coordenada1: Coordenadas, coordenada2: Coordenadas) -> float:
    RADIO_TIERRA_METROS = 6371e3

    φ1 = radians(coordenada1.latitud)
    φ2 = radians(coordenada2.longitud)
    Δφ = radians(coordenada2.latitud - coordenada1.latitud)
    Δλ = radians(coordenada2.longitud - coordenada1.longitud)

    a = (
        math.sin(Δφ / 2) * math.sin(Δφ / 2)
        + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ / 2) * math.sin(Δλ / 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return RADIO_TIERRA_METROS * c
