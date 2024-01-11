import f1
import pathlib


def test_lee_carreras(datos) -> None:
    print(f"Total registros leídos: {len(datos)}")
    print("Mostrando los dos primeros registros:")
    print(datos[0])
    print(datos[1])


def test_media_tiempo_boxes(datos) -> None:
    resultado = f1.media_tiempo_boxes(datos, "Barcelona")
    print(f"La media de tiempo en boxes en la ciudad de Barcelona es de {resultado} segundos")


def test_pilotos_menor_tiempo_medio_vueltas_top(datos) -> None:
    n = 4
    resultado = f1.pilotos_menor_tiempo_medio_vueltas_top(datos, n)
    print(f"Los {n} pilotos con menor tiempo medio son: {resultado}")


def test_ratio_tiempo_boxes_total(datos) -> None:
    resultado = f1.ratio_tiempo_boxes_total(datos)
    print("Los ratios del tiempo en boxes son:")
    for i, j, k in resultado:
        print(f"{i}, {j:%d/%m/%y}, {k:.3f}")


def test_puntos_piloto_anyos(datos) -> None:
    resultado = f1.puntos_piloto_anyos(datos)
    print("Puntos por año de cada uno de los pilotos:")
    for i, j in resultado.items():
        print(i, j)


def test_mejor_escuderia_anyo(datos) -> None:
    resultado = f1.mejor_escuderia_anyo(datos, 2022)
    print(f"La mejor escudería en el año 2022 ha sido {resultado}.")


def main() -> None:
    TESTS = (
        test_lee_carreras,
        test_media_tiempo_boxes,
        test_pilotos_menor_tiempo_medio_vueltas_top,
        test_ratio_tiempo_boxes_total,
        test_puntos_piloto_anyos,
        test_mejor_escuderia_anyo,
    )
    ruta_csv = pathlib.Path(__file__).parents[1] / "data" / "f1.csv"
    datos = f1.lee_carreras(str(ruta_csv))

    for test in TESTS:
        print("=" * 10, test.__name__, "=" * 10)
        test(datos)
        print()

if __name__ == "__main__":
    main()
