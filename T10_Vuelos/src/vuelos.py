import csv
from datetime import date, time, datetime
import typing


class Vuelo(typing.NamedTuple):
    destino: str
    precio: float
    num_plazas: int
    num_pasajeros: int
    código: str
    fecha: date
    duración: int
    hora: time
    velocidad: float
    escalas: list[str]
    económico: bool


# peor forma de hacerlo:
#
# from collections import namedtuple
# Vuelo = namedtuple(
#     "Vuelo",
#     "destino, precio, num_plazas, num_pasajeros, código, fecha, duración, hora, velocidad, escalas, económico",
# )


def lee_vuelos(ruta: str) -> list[Vuelo]:
    vuelos = []
    with open(ruta, encoding="utf-8") as file:
        lector = csv.reader(file, delimiter=";")
        next(lector)  # saltar línea de la cabecera
        for línea in lector:
            (
                destino,
                precio,
                num_plazas,
                num_pasajeros,
                código,
                fecha,
                duración,
                hora,
                velocidad,
                escalas,
                económico,
            ) = línea
            destino = destino.strip()
            fecha = datetime.strptime(fecha.strip(), "%d/%m/%Y").date()
            hora = time.fromisoformat(hora.strip())
            duración = int(duración.strip())
            velocidad = float(velocidad.strip())
            precio = float(precio.replace(",", ".").strip())
            num_plazas = int(num_plazas.strip())
            num_pasajeros = int(num_pasajeros.strip())
            escalas = [i.strip() for i in escalas.split("-")]
            económico = económico.strip() == "S"
            vuelo = Vuelo(
                destino,
                precio,
                num_plazas,
                num_pasajeros,
                código,
                fecha,
                duración,
                hora,
                velocidad,
                escalas,
                económico,
            )
            vuelos.append(vuelo)
    return vuelos


def filtra_vuelos_a(vuelos: list[Vuelo], destino: str) -> list[Vuelo]:
    return [v for v in vuelos if v.destino == destino]


def vuelos_mas_velocidad_que(
    vuelos: list[Vuelo], velocidad_media: float
) -> list[tuple[str, date, float]]:
    return [
        (v.destino, v.fecha, v.velocidad)
        for v in vuelos
        if v.velocidad > velocidad_media
    ]


def todos_vuelos_mas_velocidad_que(vuelos: list[Vuelo], velocidad_media: float) -> bool:
    return all(v.velocidad > velocidad_media for v in vuelos)


def vuelos_más_velocidad(vuelos: list[Vuelo]) -> Vuelo:
    return max(vuelos, key=lambda v: v.velocidad)


def vuelos_por_horario(
    vuelos: list[Vuelo], mes: int
) -> list[tuple[str, float, date, time]]:
    return sorted(
        (
            (v.destino, v.precio, v.fecha, v.hora)
            for v in vuelos
            if v.fecha.month == mes
        ),
        key=lambda x: x[3],
    )


def distintas_escalas(vuelos: list[Vuelo]) -> list[str]:
    escalas_set = set()
    for v in vuelos:
        escalas_set.update(v.escalas)
    return sorted(escalas_set)


def vuelos_con_escalas_en(
    vuelos: list[Vuelo], ciudad_escala: str
) -> list[tuple[str, float, int]]:
    vuelos_filtrados = [
        (v.destino, v.precio, v.num_plazas)
        for v in vuelos
        if ciudad_escala in v.escalas or ciudad_escala == v.destino
    ]
    return sorted(vuelos_filtrados, key=lambda x: x[1])


def número_de_vuelo_por_destino(vuelos: list[Vuelo]) -> dict[str, int]:
    destinos_count = typing.DefaultDict(int)
    for v in vuelos:
        destinos_count[v.destino] += 1
    return destinos_count


def suma_de_pasajeros_por_fechas(vuelos: list[Vuelo]) -> dict[str, int]:
    pasajeros_por_fecha = typing.DefaultDict(int)
    for v in vuelos:
        pasajeros_por_fecha[v.fecha] += v.num_pasajeros
    return pasajeros_por_fecha


def lista_destinos_por_compañía(vuelos: list[Vuelo]) -> dict[str, list[str]]:
    destinos_por_compañía = typing.DefaultDict(list[str])
    for v in vuelos:
        compañía = v.código[:3]
        destinos_por_compañía[compañía].append(v.destino)
    return destinos_por_compañía


def vuelos_entre_fechas(
    vuelos: list[Vuelo], fecha_inicio: date, fecha_fin: date
) -> list[tuple[str, float, list[str]]]:
    return sorted(
        (
            (v.destino, v.precio, v.escalas)
            for v in vuelos
            if (fecha_inicio is None or v.fecha >= fecha_inicio)
            and (fecha_fin is None or v.fecha <= fecha_fin)
        ),
        key=lambda x: x[1],
    )


def destinos_distintos_por_compañía(vuelos: list[Vuelo]) -> dict[str, set[str]]:
    destinos_por_compañía = typing.DefaultDict(set[str])
    for v in vuelos:
        compañía = v.código[:3]
        destinos_por_compañía[compañía].add(v.destino)
    return destinos_por_compañía


def códigos_vuelos_más_plazas_que_por_número_de_escalas(
    vuelos: list[Vuelo], plazas: int
) -> dict[str, list[str]]:
    vuelos_por_numero_de_escalas = typing.DefaultDict(list[str])
    for v in vuelos:
        if v.num_plazas == plazas:
            numero_de_escalas = len(v.escalas)
            vuelos_por_numero_de_escalas[str(numero_de_escalas)].append(v.código)

    return vuelos_por_numero_de_escalas


def vuelo_menor_duración_por_destino(vuelos: list[Vuelo]) -> dict[str, tuple[str, int]]:
    # OJO: esta solucion puede que sea algo rebuscada, jeje
    return {
        v.destino: (v.código, v.duración)
        for v in sorted(vuelos, key=lambda x: x.duración, reverse=True)
    }


def promedio_de_precios_por_compañia(
    vuelos: list[Vuelo], económico: bool
) -> list[tuple[str, int]]:
    if económico:
        vuelos = [v for v in vuelos if v.económico]

    precio_total_vuelos_por_compañia = typing.DefaultDict(float)
    for v in vuelos:
        compañia = v.código[:3]
        precio_total_vuelos_por_compañia[compañia] += v.precio

    return [
        (c, p / len(tuple(v for v in vuelos if v.código[:3] == c)))
        for c, p in precio_total_vuelos_por_compañia
    ]


def n_vuelos_mayor_velocidad_por_meses(
    vuelos: list[Vuelo], n: int
) -> dict[int, list[tuple[str, date, float]]]:
    vuelos_mas_rapidos_por_mes = typing.DefaultDict(list[tuple[str, date, float]])
    for v in sorted(vuelos, key=lambda v: v.velocidad, reverse=True):
        if len(vuelos_mas_rapidos_por_mes[v.fecha.month]) >= n:
            continue

        datos = (v.código, v.fecha, v.velocidad)
        vuelos_mas_rapidos_por_mes[v.fecha.month].append(datos)

    return vuelos_mas_rapidos_por_mes


def escala_por_la_que_pasan_más_vuelos_entre_fechas(
    vuelos: list[Vuelo], inicio: date, fin: date
) -> typing.Optional[str]:
    #  Que, recibiendo una lista de tipo Vuelo y dos
    # fechas (si alguna de ellas, o ambas, toman el valor None no se tendrá en cuenta en el filtro la/s fecha/s que
    # tomen dicho valor), devuelve la escala por las que pasan más vuelos entre las fechas dadas. Si no hay vuelos
    # entra las fechas dadas devuelve None.
    # En el test se pide que se visualice la escala y las fechas consideradas.
    vuelos_por_escala = typing.DefaultDict(int)

    for v in vuelos:
        if ((inicio is None) or (inicio <= v.fecha)) and (
            (fin is None) or (v.fecha <= fin)
        ):
            for i in v.escalas:
                vuelos_por_escala[i] += 1

    if vuelos_por_escala:
        return max(vuelos_por_escala.items(), key=lambda x: x[1])[0]

    return None


def vuelo_con_mayor_porcentaje_de_ocupación_por_destino(
    vuelos: list[Vuelo],
) -> dict[str, tuple[str, int, int, float]]:
    #  Que, recibiendo una lista de tipo Vuelo,
    # devuelva un diccionario que a cada destino le haga corresponder una tupla con el código de vuelo, el número
    # de plazas, el número de pasajeros y el porcentaje del vuelo con mayor porcentaje de ocupación al destino
    # de que se trate.
    # En el test se pide que se visualice cada pareja clave-valor una debajo de otra
    datos_por_destinos_con_mayor_ocupacion = {}

    for v in vuelos:
        porcentaje_de_ocupacion = v.num_pasajeros / v.num_plazas * 100
        datos_actuales = datos_por_destinos_con_mayor_ocupacion.get(v.destino)

        if not datos_actuales or (datos_actuales[3] < porcentaje_de_ocupacion):
            datos_por_destinos_con_mayor_ocupacion[v.destino] = (
                v.código,
                v.num_plazas,
                v.num_pasajeros,
                porcentaje_de_ocupacion,
            )

    return datos_por_destinos_con_mayor_ocupacion


def destino_menor_promedio_de_precios_mayor_porcentaje_ocupación(
    vuelos: list[Vuelo], porcentaje_umbral: float
) -> str:
    #  Que, recibiendo una lista de tipo
    # Vuelo y un número real, devuelva el destino al que, de promedio, cuesta menos el billete de los vuelos cuyo
    # porcentaje de ocupación sea mayor o igual que el número real dado.
    # En el test se pide que se visualice el número real y el destino obtenido.
    vuelos_filtrados = (
        v for v in vuelos if v.num_pasajeros / v.num_plazas * 100 >= porcentaje_umbral
    )
    return min(vuelos_filtrados, key=lambda v: v.precio).destino

def compañía_con_más_pasajeros_por_destino(vuelos: list[Vuelo]) -> dict[str, str]:
    # otra solucion es (puede que sea más eficiente, no he hecho pruebas):
    #
    # compañia_por_destino = {}
    # pasajeros_por_destino = typing.DefaultDict(int)
    #
    # for v in vuelos:
    #     if v.num_pasajeros > pasajeros_por_destino[v.destino]:
    #         pasajeros_por_destino[v.destino] = v.num_pasajeros
    #
    #         compañia = v.código[:3]
    #         compañia_por_destino[compañia] = v.destino
    #
    # return compañia_por_destino

    vuelos = sorted(vuelos, key=lambda v: v.num_pasajeros)

    return {
        v.destino: v.código[:3]
        for v in vuelos
    }


