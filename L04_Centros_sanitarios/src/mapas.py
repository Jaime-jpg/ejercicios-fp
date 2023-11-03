# -*- coding: utf-8 -*-

import folium
from coordenadas import Coordenadas
import webbrowser
import os


def crea_mapa(coordenadas: Coordenadas, zoom=9) -> folium.Map:
    """
    Función que crea un mapa folium que está centrado en la latitud y longitud
    dados como parámetro y mostrado con el nivel de zoom dado.
    @param coordenadas: latitud y longitud del centro del mapa en pantalla
    @type coordenadas: Coordenadas (float, float)
    @param zoom: nivel del zoom con el que se muestra el mapa
    @type zoom:int
    @return: objeto mapa creado
    @rtype: folium.Map
    """
    mapa = folium.Map(
        location=[coordenadas.latitud, coordenadas.longitud], zoom_start=zoom
    )
    return mapa


def agrega_marcador(
    mapa: folium.Map, coordenadas: Coordenadas, etiqueta: str, color: str
) -> folium.Marker:
    """
    Función que agrega un marcador del color dado como parámetro con un icono de tipo señal de información
    al mapa dado como parámetro. El marcador se mostrará en el punto del mapa dado por la latitud y longitud de las coordenadas dadas
    como parámetro y cuandos se mueva el ratón sobre él, se mostrará una etiqueta con el texto
    dado por el parámetro etiqueta
    @param mapa: objeto mapa al que se le van a agregar el marcador
    @type: folium.Map
    @param coordenadas: latitud y longitud del centro del mapa en pantalla
    @type coordenadas: Coordenadas (float, float)
    @param etiqueta: texto de la etiqueta que se asociará al marcador
    @type etiqueta: str
    @param color: color del marcador
    @type color: str
    @return: objeto marcador creado
    @rtype: folium.Marker
    """
    marcador = folium.Marker(
        [coordenadas.latitud, coordenadas.longitud],
        popup=etiqueta,
        icon=folium.Icon(color=color, icon="info-sign"),
    )
    marcador.add_to(mapa)
    return marcador


def guarda_mapa(mapa: folium.Map, ruta_fichero: str) -> None:
    """Guard un mapa como archivo html

    :param mapa: Mapa a guardar
    :type mapa: folium.Map
    :param ruta_fichero: Nombre y ruta del fichero
    :type ruta_fichero: str
    """
    mapa.save(ruta_fichero)
    # Abre el fichero creado en un navegador web
    webbrowser.open("file://" + os.path.realpath(ruta_fichero))
