import baloncesto
import pathlib


def test_lee_partidos(datos):
    resultado = baloncesto.lee_partidos(datos)
    print("Total registros leídos:", len(resultado))
    print("Tres primeros:", resultado[:3])
    print("Tres últimos:", resultado[-3:])
    return resultado


def test_equipo_con_mas_faltas(datos):
    resultado = baloncesto.equipo_con_mas_faltas(datos)
    print(resultado)


def test_media_puntos_por_equipo(datos):
    resultado = baloncesto.media_puntos_por_equipo(datos, "Copa del Rey")
    print("(Competicion='Copa del Rey'):")
    print(*(resultado.items()), sep="\n")


def test_diferencia_puntos_anotados(datos):
    resultado = baloncesto.diferencia_puntos_anotados(datos, "Barcelona")
    print("(Equipo='Barcelona')")
    print(resultado)


def test_victorias_por_equipo(datos):
    resultado = baloncesto.victorias_por_equipo(datos)
    print(resultado)


def test_equipos_minimo_victorias(datos):
    resultado = baloncesto.equipos_minimo_victorias(datos, 8)
    print("(n=8)")
    print(resultado)


def test_equipos_mas_victorias_por_año(datos):
    resultado = baloncesto.equipos_mas_victorias_por_año(datos, 8)
    print("(n=8)")
    print(resultado)


def main() -> None:
    TESTS = (
        test_equipo_con_mas_faltas,
        test_media_puntos_por_equipo,
        test_diferencia_puntos_anotados,
        test_victorias_por_equipo,
        test_equipos_minimo_victorias,
        test_equipos_mas_victorias_por_año,
    )

    RUTA_ARCHIVO = (
        pathlib.Path(__file__).parents[1] / "data" / "resultados_baloncesto.csv"
    )
    datos = test_lee_partidos(RUTA_ARCHIVO)

    for test in TESTS:
        print("=" * 10, test.__name__, "=" * 10)
        test(datos)


if __name__ == "__main__":
    main()
