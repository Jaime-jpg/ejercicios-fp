from collections import namedtuple
from math import sqrt


Coordenadas = namedtuple("Coordenadas", "latitud, longitud")

def calcular_distancia(coordenada1: Coordenadas, coordenada2: Coordenadas) -> float:
    return sqrt(
        (coordenada1.latitud - coordenada2.latitud) ** 2 +
        (coordenada1.longitud - coordenada2.longitud) ** 2
    )


def calcular_media_coordenadas(coordenadas: list[Coordenadas]) -> Coordenadas:
    return Coordenadas(
        sum(i.latitud for i in coordenadas) / len(coordenadas),
        sum(i.longitud for i in coordenadas) / len(coordenadas),
    )


