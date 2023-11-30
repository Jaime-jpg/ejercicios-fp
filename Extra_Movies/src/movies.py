import typing
from datetime import date
import csv
import collections


# import collections
#
# Pelicula = collections.namedtuple(
#     "Pelicula",
#     [
#         "id",
#         "title",
#         "original_language",
#         "release_date",
#         "vote_average",
#         "popularity",
#         "adult",
#         "genres",
#     ],
# )

# prefiero usar < class x(typing.NamedTuple) >,
# pero así es más parecido a como lo piden en el examen
Pelicula = typing.NamedTuple(
    "Pelicula",
    [
        ("id", str),
        ("title", str),
        ("original_language", str),
        ("release_date", date),
        ("vote_average", float),
        ("popularity", int),
        ("adult", bool),
        ("genres", set[str]),
    ],
)


# opinión: usar sets para los géneros me parece una mala idea pues ocupan
# bastante espacio en la memoria y es lento iterar sobre ellos.
# Una mejor solución creo que sería usar tuplas, pues solucionan estos dos
# problemas de los sets y los géneros no son algo que se vaya a modificar
# Adicionalmente, los géneros se deberían representar con un Enum y no como
# cadenas
def leer_diccionario_generos(nombre_archivo_generos: str) -> dict[str, set[str]]:
    generos_por_pelicula = typing.DefaultDict(set[str])

    with open(nombre_archivo_generos, encoding="utf-8") as f:
        archivo = f.readlines()[1:]  # omitimos la cabecera con [1:]

        for linea in archivo:
            # [:-1] elimina el caracter '\n' del final de la linea
            id_, generos = linea[:-1].split(": ")

            # También se prodría hacer con una asignación, es decir,
            # generos_por_pelicula[id_] = set(generos.split(", "))
            # Si no hubiera ids repetidas en el csv.
            # En ese caso, no haría falta DefaultDict
            generos_por_pelicula[id_].update(generos.split(", "))

    return generos_por_pelicula


def leer_peliculas(
    nombre_archivo_peliculas: str, nombre_archivo_generos: str
) -> list[Pelicula]:
    generos_por_pelicula = leer_diccionario_generos(nombre_archivo_generos)

    peliculas = []

    with open(nombre_archivo_peliculas, encoding="utf-8") as f:
        archivo = csv.reader(f)
        next(archivo)  # saltamos la cabecera

        for linea in archivo:
            (
                id_,
                title,
                original_language,
                release_date,
                vote_average,
                popularity,
                adult,
            ) = linea
            peliculas.append(
                Pelicula(
                    id_,
                    title,
                    original_language,
                    # equivalente a:
                    # datetime.strptime(release_date, "%Y-%m-%d").date()
                    date.fromisoformat(release_date),
                    float(vote_average),
                    int(popularity),
                    adult == "True",
                    generos_por_pelicula[id_],
                )
            )

    return peliculas


def genero_mas_frecuente(movies: list[Pelicula]) -> tuple[str, int]:
    # otra forma de generar frecuencia_generos:
    #
    # frecuencia_generos = typing.DefaultDict(int)
    # for pelicula in movies:
    #     for genero in pelicula.genres:
    #         frecuencia_generos[genero] += 1

    frecuencia_generos = collections.Counter(
        (genero for pelicula in movies for genero in pelicula.genres)
    )

    return max(frecuencia_generos.items(), key=lambda x: x[1])


def valoracion(pelicula: Pelicula) -> tuple[int, float]:
    """función auxiliar para ordenar las películas"""
    return pelicula.popularity, pelicula.vote_average


def mejor_valorada_por_idioma(movies: list[Pelicula]) -> dict[str, Pelicula]:
    movies.sort(key=valoracion)
    return {pelicula.original_language: pelicula for pelicula in movies}


def media_calificaciones(movies: list[Pelicula], generos: set[str]) -> float:
    notas = [pelicula.vote_average for pelicula in movies if generos <= pelicula.genres]
    return sum(notas) / len(notas) if len(notas) > 0 else 0.0


def top_n_por_genero(movies: list[Pelicula], n: int) -> dict[str, list[Pelicula]]:
    movies.sort(key=lambda p: p.vote_average, reverse=True)
    peliculas_por_generos = typing.DefaultDict(list[Pelicula])

    for pelicula in movies:
        for genero in pelicula.genres:
            if len(peliculas_por_generos[genero]) < n:
                peliculas_por_generos[genero].append(pelicula)

    return peliculas_por_generos
