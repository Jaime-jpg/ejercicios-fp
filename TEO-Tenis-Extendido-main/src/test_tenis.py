from os import error
import tenis
import pathlib
from datetime import date


def test_lee_partidos_tenis(datos) -> None:
    # lee un fichero de entrada en formato CSV codificado en UTF-8 y devuelve una lista de tuplas de tipo PartidoTenis conteniendo todos los datos almacenados en el fichero. Le puede ser de ayuda la función datetime.strptime(cadena, '%d/%m/%Y') para el parseo de fechas. Para implementar esta función defina la siguiente función auxiliar:
    print(f"Numeros total de partidos leídos: {len(datos)}")
    print("Tres primeros registros:")
    for i, partido in enumerate(datos[:3], 1):
        print(f"{i}.- {partido}")


def test_partidos_menos_errores(datos) -> None:
    # recibe una lista de tipo PartidoTenis y devuelve el partido con mayor némero de errores no forzados entre los dos jugadores.
    resultado = tenis.partidos_menos_errores(datos)
    print(f"Partido con menos errores {resultado}")


def test_jugador_mas_partidos(datos) -> None:
    # recibe una lista de tipo PartidoTenis y devuelve una tupla con el nombre del jugador que más partidos ha jugado y el némero de partidos.
    resultado = tenis.jugador_mas_partidos(datos)
    print(f"Jugador que ha jugado más partidos: {resultado}")


def test_tenista_mas_victorias(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenis, y dos fechas, ambas de tipo date, y con valor por defecto None. Devuelve el nombre del tenista que ha tenido más victorias en los partidos jugados entre las fechas (ambas inclusive). Si la primera fecha es None, la función devuelve el tenista con más victorias hasta esa fecha (inclusive). Si la segunda fecha es None, la función devuelve el tenista con más victorias desde esa fecha (inclusive). Finalmente, si las dos fechas son None, la función devuelve el tenista con más victorias de toda la lista, independientemente de la fecha. Para implementar esta función defina la siguiente función auxiliar: a. ganador:** recibe una tupla de tipo PartidoTenis y devuelve el nombre del jugador que ganó ese partido.
    print(f"{tenis.tenista_mas_victorias(datos, None, None) = }")
    print(f"{tenis.tenista_mas_victorias(datos, None, date(2020, 1, 1)) = }")
    print(f"{tenis.tenista_mas_victorias(datos, date(2020, 1, 1), None) = }")
    print(f"{tenis.tenista_mas_victorias(datos, date(2013, 1, 1), date(2020, 1, 1)) = }")


def test_media_errores_por_jugador(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenis y devuelve una lista de tuplas ordenadas con el nombre de cada jugador y su media de errores no forzados. La lista estará ordenada por la media de errores de menor a mayor.
    resultado = tenis.media_errores_por_jugador(datos)
    print("Errores no provocados de cada jugador:")
    for i, errores in enumerate(resultado, 1):
        print(f"{i}.- {errores}")


def test_jugadores_mayor_porcentaje_victorias(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenis y devuelve una lista de tuplas con el nombre de cada jugador y el porcentaje de victorias. La lista estará ordenada por el porcentaje de victorias de mayor a menor.
    resultado = tenis.jugadores_mayor_porcentaje_victorias(datos)
    print("Porcentaje de victorias de cada jugador:")
    for i, victorias in enumerate(resultado, 1):
        print(f"{i}.- {victorias}")


def test_n_tenistas_con_mas_errores(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenis y un némero n, con valor por defecto None, y devuelve una lista con los nombres de los n tenistas que han acumulado más errores no forzados en el total de partidos que han jugado. Si n es None, entonces devuelve todos los tenistas de la lista de tuplas ordenados de mayor a menor némero de errores no forzados. (2 puntos)
    print(f"{tenis.n_tenistas_con_mas_errores(datos, n=5) = }")
    print(f"{tenis.n_tenistas_con_mas_errores(datos, n=None) = }")


def test_fechas_ordenadas_por_jugador(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenis y devuelve un diccionario en el que a cada jugador le hace corresponder una lista ordenada con las fechas de sus partidos.
    resultado = tenis.fechas_ordenadas_por_jugador(datos)


def test_num_partidos_nombre(datos) -> None:
    # recibe el nombre de un tenista y devuelve un diccionario en el que las claves son las superficies y los valores una tupla con el némero de partidos jugados y ganados por el tenista en la superficie dada como clave.
    resultado = tenis.num_partidos_nombre(datos)


def test_num_tenistas_distintos_por_superficie(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenis, y devuelve un diccionario tal que a cada superficie (clave) le hace corresponder el némero de jugadores distintos que han jugado partidos en ese tipo de superficie. (1,5 puntos)
    resultado = tenis.num_tenistas_distintos_por_superficie(datos)


def test_superficie_con_mas_tenistas_distintos(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenies y devuelve una tupla con la superficie en la que juegan un mayor némero de jugadores distintos, y el némero de jugadores que han jugado en esa superficie.
    resultado = tenis.superficie_con_mas_tenistas_distintos(datos)


def test_mas_errores_por_jugador(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenis y devuelve un diccionario en el que a cada jugador y le hace corresponder el partido en el que ha cometido mayor némero de errores no forzados.
    resultado = tenis.mas_errores_por_jugador(datos)


def test_partido_mas_errores_por_mes(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenis, y una lista de cadenas con tipos de superficie, que toma como valor por defecto None, y devuelve un diccionario que asocia a cada mes, una tupla (fecha del partido, jugador1, jugador2) que representa al partido de ese mes jugado en una de las superficies de la lista dada como parámetro en el que se han cometido más errores no forzados, teniendo en cuenta los errores de ambos jugadores. Si la lista de superficies dada como parámetro tiene como valor None, entonces se tendrán en cuenta todas las superficies para generar el diccionario resultante. (2 puntos).
    resultado = tenis.partido_mas_errores_por_mes(datos)


def test_n_partidos_mas_errores_por_jugador(datos) -> None:
    # recibe una lista de tuplas de tipo PartidoTenis y un valor entero n y devuelve un diccionario en el que a cada jugador le hace corresponder una lista con los n partidos en los que ha cometido más errores no forzados.
    resultado = tenis.n_partidos_mas_errores_por_jugador(datos)


def test_mayor_numero_dias_sin_jugar(datos) -> None:
    # recibe una lista de partidos y un jugador y devuelve el máximo némero de días sin jugar del jugador dado. Si el jugador solo ha disputado un partido devolverá None.
    resultado = tenis.mayor_numero_dias_sin_jugar(datos)


def main() -> None:
    tests = (
        test_lee_partidos_tenis,
        test_partidos_menos_errores,
        test_jugador_mas_partidos,
        test_tenista_mas_victorias,
        test_media_errores_por_jugador,
        test_jugadores_mayor_porcentaje_victorias,
        test_n_tenistas_con_mas_errores,
        test_fechas_ordenadas_por_jugador,
        test_num_partidos_nombre,
        test_num_tenistas_distintos_por_superficie,
        test_superficie_con_mas_tenistas_distintos,
        test_mas_errores_por_jugador,
        test_partido_mas_errores_por_mes,
        test_n_partidos_mas_errores_por_jugador,
        test_mayor_numero_dias_sin_jugar,
    )

    RUTA_CSV = pathlib.Path(__file__).parents[1] / "data" / "tenis.csv"
    datos = tenis.lee_partidos_tenis(str(RUTA_CSV))

    for test in tests:
        print("=" * 10, test.__name__, "=" * 10)
        test(datos)
        print()


if __name__ == "__main__":
    main()
