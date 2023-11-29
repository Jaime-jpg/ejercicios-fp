import typing
from datetime import date, datetime
import csv

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


def leer_peliculas(
    nombre_archivo_peliculas: str, nombre_archivo_generos: str
) -> list[Pelicula]:
    generos_por_pelicula = {}

    with open(nombre_archivo_generos, encoding="utf-8") as f:
        archivo = f.readlines()[1:]  # omitimos la cabecera con [1:]

        for i in archivo:
            id_, generos = i.split(": ")
            generos_por_pelicula[id_] = set(generos.split(", "))

    peliculas = []

    with open(nombre_archivo_peliculas, encoding="utf-8") as f:
        archivo = csv.reader(f)
        next(archivo)  # saltamos la cabecera

        for i in archivo:
            (
                id_,
                title,
                original_language,
                release_date,
                vote_average,
                popularity,
                adult,
            ) = i
            peliculas.append(
                Pelicula(
                    id_,
                    title,
                    original_language,
                    # equivalente a: datetime.strptime(release_date, "%Y-%m-%d").date()
                    date.fromisoformat(release_date),
                    float(vote_average),
                    int(popularity),
                    adult == "True",
                    generos_por_pelicula[id_],
                )
            )

    return peliculas


def genero_mas_frecuente():
    pass
