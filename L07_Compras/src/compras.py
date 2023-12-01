import csv
import typing
from datetime import datetime, time

Compra = typing.NamedTuple(
    "Compra",
    [
        ("dni", str),
        ("supermercado", str),
        ("provincia", str),
        ("fecha_llegada", datetime),
        ("fecha_salida", datetime),
        ("total_compra", float),
    ],
)


def lee_compras(ruta_csv: str) -> list[Compra]:
    # recibe el nombre de un fichero y devuelve una lista de tuplas de tipo Compra conteniendo todos los datos almacenados en el fichero. (1 punto)
    compras = []

    with open(ruta_csv, encoding="utf-8") as f:
        archivo = csv.reader(f)
        next(archivo)  # se omite la cabecera

        for i in archivo:
            (
                dni,
                supermercado,
                provincia,
                fecha_llegada,
                fecha_salida,
                total_compra,
            ) = i

            compras.append(
                Compra(
                    dni,
                    supermercado,
                    provincia,
                    datetime.strptime(fecha_llegada, r"%d/%m/%Y %H:%M"),
                    datetime.strptime(fecha_salida, r"%d/%m/%Y %H:%M"),
                    float(total_compra),
                )
            )

    return compras


def compra_maxima_minima_provincia(
    compras: list[Compra], provincia: str | None
) -> tuple[float, float]:
    # recibe una lista de tuplas de tipo Compra y una provincia. Devuelve una tupla que contiene el importe máximo y el mínimo de las compras que se han realizado en la provincia dada como parámetro. Si la provincia toma el valor None, se devuelve una tupla con el importe máximo y el mínimo calculados a partir de todas las compras. (1 punto)

    compras_filtradas = tuple(
        (i.total_compra for i in compras)
        if provincia is None
        else (i.total_compra for i in compras if i.provincia == provincia)
    )

    return max(compras_filtradas), min(compras_filtradas)


def hora_menos_afluencia(compras: list[Compra]) -> tuple[int, int]:
    # recibe una lista de tuplas de tipo Compra y devuelve una tupla con la hora en la que llegan menos clientes y el número de clientes que llegan a dicha hora. (1,5 puntos)
    clientes_por_hora = typing.DefaultDict(int)
    for i in compras:
        clientes_por_hora[i.fecha_llegada.hour] += 1

    return min(clientes_por_hora.items(), key=lambda x: x[1])


def supermercados_mas_facturacion(
    compras: list[Compra], n: int = 3
) -> list[tuple[str, float]]:
    # recibe una lista de tuplas de tipo Compra y un número entero n, con valor por defecto 3. Devuelve un ranking, es decir, una lista de tuplas (posición_ranking, (supermercado, facturación)) con las n marcas de supermercados que más facturan, en orden decreciente de facturación. El ranking debe empezar por la posición 1. (1,5 puntos)
    facturacion_por_supermercado = typing.DefaultDict(float)
    for i in compras:
        facturacion_por_supermercado[i.supermercado] += i.total_compra

    return sorted(
        facturacion_por_supermercado.items(), key=lambda x: x[1], reverse=True
    )[:n]


def clientes_itinerantes(compras: list[Compra], n: int) -> list[tuple[str, list[str]]]:
    # recibe una lista de tuplas de tipo Compra y un entero n, y devuelve una lista de tuplas con el dni del cliente y la lista de provincias donde el cliente ha realizado sus compras, ordenadas alfabéticamente. Solo se devolverán aquellos clientes que hayan comprado en un número de provincias mayor que el parámetro n. (2 puntos)
    provincias_por_cliente = typing.DefaultDict(set[str])
    for i in compras:
        provincias_por_cliente[i.dni].add(i.provincia)

    return [
        (i[0], sorted(i[1])) for i in provincias_por_cliente.items() if len(i[1]) > n
    ]


def dias_estrella(
    compras: list[Compra], supermercado: str, provincia: str
) -> list[str]:
    # recibe una lista de tuplas de tipo Compra, un supermercado y una provincia, y devuelve una lista ordenada cronológicamente con las "fechas estrella" de ese supermercado en esa provincia. La fechas de las lista deben estar en formato "dd/mm/aaaa". Se consideran "fechas estrella" aquellos días de salida en los que el supermercado factura más que el día anterior y más que el día siguiente. (2 puntos)
    compras_filtradas = [
        i
        for i in compras
        if i.supermercado == supermercado and i.provincia == provincia
    ]
    beneficios_por_dia = typing.DefaultDict(float)

    for i in compras_filtradas:
        beneficios_por_dia[i.fecha_llegada.date()] += i.total_compra

    res = []
    beneficios_por_dia_ordenados = sorted(beneficios_por_dia.items())
    
    for i, j, k in zip(
        beneficios_por_dia_ordenados,
        beneficios_por_dia_ordenados[1:],
        beneficios_por_dia_ordenados[2:],
    ):
        print(j[0].strftime(r"%d/%m/%Y"))

        if (j[1] > i[1]) and (j[1] > k[1]):
            res.append(j[0].strftime(r"%d/%m/%Y"))

    return sorted(res)
