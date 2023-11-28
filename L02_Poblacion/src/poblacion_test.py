# -*- coding: utf-8 -*-
"""
Created on 12 oct. 2018
@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González, Fermín Cruz
ÚLTIMA MODIFICACIÓN: 10/10/2022
"""
from poblacion import *  # >>> comentario de Jaime: es mala idea el "import *"
                         # >>> https://www.geeksforgeeks.org/why-import-star-in-python-is-a-bad-idea/


################################################################
#  Funciones de test
################################################################
def test_lee_poblaciones(datos):
    """
    Muestra el número de elementos de datos, los 3 primeros registros y los 3 últimos registros

    @param datos: lista de tuplas con información de poblaciones
    @type datos: list(RegistroPoblacion)
    """
    print("===> Test de lee_poblaciones")
    print(f"Leídos {len(datos)} registros.")
    print("\nMostrando los 3 primeros:")
    print("\n".join(str(r) for r in datos[:3]))
    print("\nMostrando los 3 últimos:")
    print("\n".join(str(r) for r in datos[-3:]))
    print("#############################################################\n")


def test_calcula_paises(datos):
    """
    Prueba la función calcula_paises

    @param datos: lista de tuplas con información de poblaciones
    @type datos: list(RegistroPoblacion)
    """
    print("===> Test de calcula_paises")
    paises = calcula_paises(datos)
    print("Leidos ", len(paises), "paises distintos")
    print(paises)
    print("#############################################################\n")


def test_filtra_por_pais(datos):
    """
    Prueba la función calcula_paises

    @param datos: lista de tuplas con información de poblaciones
    @type datos: list(RegistroPoblacion)
    """
    print("===> Test de filtra_por_pais")
    poblacion_es = filtra_por_pais(datos, "Spain")
    print("Poblacion españa")
    print("Leidos ", len(poblacion_es), "datos de población de España")
    print(poblacion_es)
    print("#############################################################\n")


def test_filtra_por_paises_y_anyo(datos):
    """
    Prueba la función filtra_por_paises_y_anyo

    @param datos: lista de tuplas con información de poblaciones
    @type datos: list(RegistroPoblacion)
    """
    print("===> Test de filtra_por_paises_y_anyo")
    paises = {"Spain", "Portugal", "France", "Mexico", "China"}
    poblacion_2016 = filtra_por_paises_y_anyo(datos, 2016, paises)
    print(
        "Leidos ",
        len(poblacion_2016),
        "datos del año 2016 para los paises",
        paises,
    )
    print(poblacion_2016)
    print("#############################################################\n")


def test_muestra_evolucion_poblacion(datos):
    """
    Prueba la función muestra_evolucion_poblacion

    @param datos: lista de tuplas con información de poblaciones
    @type datos: list(RegistroPoblacion)
    """
    print("===> Test de muestra_evolucion_poblacion")
    muestra_evolucion_poblacion(datos, "Spain")
    print("#############################################################\n")


def test_muestra_comparativa_paises_anyo(datos):
    """
    Prueba la función muestra_comparativa_paises_anyo

    @param datos: lista de tuplas con información de poblaciones
    @type datos: list(RegistroPoblacion)
    """
    print("===> Test de muestra_comparativa_paises_anyo")
    muestra_comparativa_paises_anyo(
        datos, 2016, ["Spain", "Portugal", "France", "Mexico", "China"]
    )
    print("#############################################################\n")


################################################################
#  Programa principal
################################################################
RUTA_ARCHIVO = "C:/Users/jaime/Documents/ProyectosPython/L02_Poblacion/data/population.csv"

# >>> comentario de Jaime: es mala práctica llamar múltiples funciones dentro del 'if __name__ == "__main__"' (mirar mis otros archivos para ver como se debe hacer)
if __name__ == "__main__":
    # >>> comentario de Jaime: la función escrita por el profesor para obtener la ruta es una cutrada
    # >>> si se desea algo parecido, usar "Pathlib"
    datos = lee_poblaciones(RUTA_ARCHIVO)

    test_lee_poblaciones(datos)
    test_calcula_paises(datos)
    test_filtra_por_pais(datos)
    test_filtra_por_paises_y_anyo(datos)
    test_muestra_evolucion_poblacion(datos)
    test_muestra_comparativa_paises_anyo(datos)
