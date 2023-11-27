import extranjeria
import pathlib


RUTA_CSV = pathlib.Path(__file__).parents[1] / "data" / "extranjeriaSevilla.csv"


def test_lee_datos_extranjeria() -> None:
    # recibe la ruta del fichero CSV, devolviendo una lista de tuplas de tipo RegistroExtranjeria con toda la información contenida en el fichero.
    datos = extranjeria.lee_datos_extranjeria(str(RUTA_CSV))
    print(f"Leídos {len(datos)} registros")
    print("Tres primeros registros:")
    for i in datos[:3]:
        print(i)
    print("Tres últimos registros:")
    for i in datos[-3:]:
        print(i)


def test_numero_nacionalidades_distintas() -> None:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el número de nacionalidades distintas presentes en los registros de la lista recibida como parámetro.
    datos = extranjeria.lee_datos_extranjeria(str(RUTA_CSV))
    resultado = extranjeria.numero_nacionalidades_distintas(datos)
    print(f"Hay {resultado} distintas en los datos.")


def test_secciones_distritos_con_extranjeros_nacionalidades() -> None:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y un conjunto de cadenas con nombres de países, y devuelve una lista de tuplas (distrito, seccion) con los distritos y secciones en los que hay extranjeros del conjunto de paises dado como parámetro. La lista de tuplas devuelta estará ordenada por distrito.
    datos = extranjeria.lee_datos_extranjeria(str(RUTA_CSV))
    resultado = extranjeria.secciones_distritos_con_extranjeros_nacionalidades(
        datos, {"ALEMANIA", "ITALIA"}
    )
    print(
        f"Hay {len(resultado)} secciones de distritos con residentes cuya procedencia es ALEMANIA o ITALIA."
    )
    print("Tres primeras secciones:")
    print(resultado[:3])


def test_total_extranjeros_por_pais() -> None:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve un diccionario de tipo {str:int} en el que las claves son los países y los valores son el número total de extranjeros (tanto hombres como mujeres) de cada país.
    datos = extranjeria.lee_datos_extranjeria(str(RUTA_CSV))
    resultado = extranjeria.total_extranjeros_por_pais(datos)
    print("Mostrando el número de residentes para algunos países de procedencia:")
    for pais, residentes in tuple(resultado.items())[:3]:
        print(f"{pais}: {residentes}")


def test_top_n_extranjeria() -> None:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve una lista de tuplas (pais, numero_extranjeros) con los n países de los que hay más población extranjera en los registros pasados como parámetros.
    datos = extranjeria.lee_datos_extranjeria(str(RUTA_CSV))
    resultado = extranjeria.top_n_extranjeria(datos, 5)
    print("Mostrando los 5 países de los que proceden más residentes:")
    print(resultado)


def test_barrio_mas_multicultural() -> None:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el nombre del barrio en el que hay un mayor número de países de procedencia distintos.
    datos = extranjeria.lee_datos_extranjeria(str(RUTA_CSV))
    resultado = extranjeria.barrio_mas_multicultural(datos)
    print(f"El barrio más multicultural de Sevilla es {resultado}")


def test_barrio_con_mas_extranjeros() -> None:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el nombre del barrio en el que hay un mayor número de extranjeros, bien sea en total (tanto hombres como mujeres) si tipo tiene el valor None, bien sea de hombres si tipo es 'Hombres', o de mujeres si tipo es 'Mujeres'.
    datos = extranjeria.lee_datos_extranjeria(str(RUTA_CSV))

    resultado_1 = extranjeria.barrio_con_mas_extranjeros(datos)
    resultado_2 = extranjeria.barrio_con_mas_extranjeros(datos, "HOMBRES")
    resultado_3 = extranjeria.barrio_con_mas_extranjeros(datos, "MUJERES")

    print(f"El barrio con más residentes extranjeros es {resultado_1}")
    print(f"El barrio con más hombres residentes extranjeros es {resultado_2}")
    print(f"El barrio con más mujeres residentes extranjeras es {resultado_3}")


def test_pais_mas_representado_por_distrito() -> None:
    # recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve un diccionario de tipo {str:str} en el que las claves son los distritos y los valores los países de los que hay más extranjeros residentes en cada distrito.
    datos = extranjeria.lee_datos_extranjeria(str(RUTA_CSV))
    resultado = extranjeria.pais_mas_representado_por_distrito(datos)
    for i, j in resultado.items():
        print(f"Distrito {i} => {j}")


def main() -> None:
    tests = (
        test_lee_datos_extranjeria,
        test_numero_nacionalidades_distintas,
        test_secciones_distritos_con_extranjeros_nacionalidades,
        test_total_extranjeros_por_pais,
        test_top_n_extranjeria,
        test_barrio_mas_multicultural,
        test_barrio_con_mas_extranjeros,
        test_pais_mas_representado_por_distrito,
    )

    for test in tests:
        print("=" * 10, test.__name__, "=" * 10)
        test()
        print()


if __name__ == "__main__":
    main()
