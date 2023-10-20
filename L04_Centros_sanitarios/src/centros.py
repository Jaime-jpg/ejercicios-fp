from collections import namedtuple
import csv
from coordenadas import Coordenadas, calcular_distancia, calcular_media_coordenadas
import folium
from mapas import crea_mapa, agrega_marcador, guarda_mapa

CentroSanitario = namedtuple(
    "CentroSanitario",
    "nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci",
)


def leer_centros(ruta_archivo: str) -> list[CentroSanitario]:
    with open(ruta_archivo, encoding="utf-8") as f:
        archivo = csv.reader(f, delimiter=";")
        next(archivo)  # omitimos cabecera

        return [
            CentroSanitario(
                i[0],
                i[1],
                Coordenadas(float(i[2]), float(i[3])),
                i[4],
                int(i[5]),
                i[6] == "true",
                i[7] == "true",
            )
            for i in archivo
        ]


def calcular_total_camas_centros_accesibles(centros: list[CentroSanitario]) -> int:
    return sum(i.num_camas for i in centros if i.acceso_minusvalidos)


def obtener_centros_con_uci_cercanos_a(
    centros: list[CentroSanitario], punto_central: Coordenadas, umbral: float
) -> tuple[str, str, Coordenadas]:
    return [
        (i.nombre, i.localidad, i.coordenadas)
        for i in centros
        if calcular_distancia(i.coordenadas, punto_central) <= umbral
    ]


def generar_mapa(centros: tuple[str, str, Coordenadas]) -> folium.Map:
    mapa = crea_mapa(calcular_media_coordenadas([i[2] for i in centros]))
    for i in centros:
        agrega_marcador(mapa, i[2], i[0], "red")
    guarda_mapa(mapa, r"C:\Users\jaime\Documents\ProyectosPython\L04_Centros_sanitarios\data\mapa")
    
    
