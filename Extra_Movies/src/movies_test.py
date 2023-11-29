import pathlib
import movies


RUTA_DATA = pathlib.Path(__file__).parents[1] / "data"
RUTA_GENEROS = RUTA_DATA / "movies_fp_genres.csv"
RUTA_PELICULAS = RUTA_DATA / "movies_fp.csv"


def test_leer_peliculas() -> None:
    datos = movies.leer_peliculas(str(RUTA_PELICULAS), str(RUTA_GENEROS))
    print(len(datos))
    print(f"Primera: {datos[0]}")
    print(f"Última: {datos[-1]}")


def test_genero_mas_frecuente() -> None:
    datos = movies.leer_peliculas(str(RUTA_PELICULAS), str(RUTA_GENEROS))
    resultado = movies.genero_mas_frecuente(datos)
    print(f"El género más frecuente es {resultado}")


def test_mejor_valorada_por_idioma() -> None:
    datos = movies.leer_peliculas(str(RUTA_PELICULAS), str(RUTA_GENEROS))
    resultado = movies.mejor_valorada_por_idioma(datos)
    print(f"Mejor en español (es): {resultado['es']}")


def test_media_calificaciones() -> None:
    datos = movies.leer_peliculas(str(RUTA_PELICULAS), str(RUTA_GENEROS))

    resultado_1 = movies.media_calificaciones(datos, {"Action", "Adventure", "Fake"})
    print("'Action', 'Adventure', 'Fake'", resultado_1, sep=": ")

    resultado_2 = movies.media_calificaciones(datos, {"Action", "Adventure"})
    print("'Action', 'Adventure'", resultado_2, sep=": ")


def test_top_n_por_genero() -> None:
    datos = movies.leer_peliculas(str(RUTA_PELICULAS), str(RUTA_GENEROS))
    resultado = movies.top_n_por_genero(datos, 2)

    print("Top 2 peliculas de 'Fake'", resultado["Fake"], sep=": ")
    print("Top 2 peliculas de 'Action'", resultado["Action"], sep=": ")


def main() -> None:
    TESTS = (
        test_leer_peliculas,
        test_genero_mas_frecuente,
        test_mejor_valorada_por_idioma,
        test_media_calificaciones,
        test_top_n_por_genero,
    )

    for test in TESTS:
        print("=" * 10, test.__name__, "=" * 10)
        test()
        print()


if __name__ == "__main__":
    main()
