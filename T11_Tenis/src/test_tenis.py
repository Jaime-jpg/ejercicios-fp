import tenis
import pathlib
from datetime import date


def test_lee_partidos_tenis(datos) -> None:
    print(f"Numeros total de partidos leídos: {len(datos)}")
    print("Tres primeros registros:")
    for i, partido in enumerate(datos[:3], 1):
        print(f"{i}.- {partido}")


def test_partidos_menos_errores(datos) -> None:
    resultado = tenis.partidos_menos_errores(datos)
    print(f"Partido con menos errores {resultado}")


def test_jugador_mas_partidos(datos) -> None:
    resultado = tenis.jugador_mas_partidos(datos)
    print(f"Jugador que ha jugado más partidos: {resultado}")


def test_tenista_mas_victorias(datos) -> None:
    print(f"{tenis.tenista_mas_victorias(datos, None, None) = }")
    print(f"{tenis.tenista_mas_victorias(datos, None, date(2020, 1, 1)) = }")
    print(f"{tenis.tenista_mas_victorias(datos, date(2020, 1, 1), None) = }")
    print(f"{tenis.tenista_mas_victorias(datos, date(2013, 1, 1), date(2020, 1, 1)) = }")


def test_media_errores_por_jugador(datos) -> None:
    resultado = tenis.media_errores_por_jugador(datos)
    print("Errores no provocados de cada jugador:")
    for i, errores in enumerate(resultado, 1):
        print(f"{i}.- {errores}")


def test_jugadores_mayor_porcentaje_victorias(datos) -> None:
    resultado = tenis.jugadores_mayor_porcentaje_victorias(datos)
    print("Porcentaje de victorias de cada jugador:")
    for i, victorias in enumerate(resultado, 1):
        print(f"{i}.- {victorias}")


def test_n_tenistas_con_mas_errores(datos) -> None:
    print(f"{tenis.n_tenistas_con_mas_errores(datos, n=5) = }")
    print(f"{tenis.n_tenistas_con_mas_errores(datos, n=None) = }")


def test_fechas_ordenadas_por_jugador(datos) -> None:
    # OJO: el test del enunciado (README.md) no está bien, las fechas no están ordenadas
    resultado = tenis.fechas_ordenadas_por_jugador(datos)
    print("Fechas de los partidos de cada jugador:")
    for jugador, fechas in resultado.items():
        print(jugador)
        for i in fechas:
            print(i.strftime(r"%d/%m/%Y"), end="  ")
        print()


def test_num_partidos_nombre(datos) -> None:
    print(f"{tenis.num_partidos_nombre(datos, "Rafael Nadal") = }")
    print(f"{tenis.num_partidos_nombre(datos, "Carlos Alcaraz") = }")


def test_num_tenistas_distintos_por_superficie(datos) -> None:
    print(f"{tenis.num_tenistas_distintos_por_superficie(datos) = }")


def test_superficie_con_mas_tenistas_distintos(datos) -> None:
    print(f"{tenis.superficie_con_mas_tenistas_distintos(datos) = }")


def test_mas_errores_por_jugador(datos) -> None:
    resultado = tenis.mas_errores_por_jugador(datos)
    print("Partido con más errores de cada jugador:")
    for i, j in resultado.items():
        print(f"{i} -> {j}")
        


def test_partido_mas_errores_por_mes(datos) -> None:
    resultado = tenis.partido_mas_errores_por_mes(datos, ["Sintética"])
    for i, j in resultado.items():
        print(f"{i} -> {j}")    
    
    resultado = tenis.partido_mas_errores_por_mes(datos, ["Sintética", "Tierra"])
    for i, j in resultado.items():
        print(f"{i} -> {j}")

    resultado = tenis.partido_mas_errores_por_mes(datos, None)
    for i, j in resultado.items():
        print(f"{i} -> {j}")


def test_n_partidos_mas_errores_por_jugador(datos) -> None:
    resultado = tenis.n_partidos_mas_errores_por_jugador(datos, 3)
    for i, j in resultado.items():
        print(f"{i} -> {j}")


def test_mayor_numero_dias_sin_jugar(datos) -> None:
    jugador = "Carlos Alcaraz"
    resultado = tenis.mayor_numero_dias_sin_jugar(datos, jugador)
    print(f"{jugador}: {resultado}")


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
