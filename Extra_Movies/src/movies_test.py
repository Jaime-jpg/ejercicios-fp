import pathlib

RUTA_DATA = pathlib.Path(__file__).parents[1] / "data"
RUTA_GENEROS = RUTA_DATA / "movies_fp_genres.csv"
RUTA_PELICULAS = RUTA_DATA / "movies_fp.csv"


def main() -> None:

leer_peliculas( str(RUTA_PELICULAS),str(RUTA_GENEROS))


if __name__ == "__main__":
    main()
