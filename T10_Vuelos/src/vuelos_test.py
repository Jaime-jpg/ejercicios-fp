import unittest
from datetime import date
import pathlib
from vuelos import (
    lee_vuelos,
    filtra_vuelos_a,
    vuelos_mas_velocidad_que,
    todos_vuelos_mas_velocidad_que,
    vuelos_más_velocidad,
    vuelos_por_horario,
    distintas_escalas,
    vuelos_con_escalas_en,
    número_de_vuelo_por_destino,
    suma_de_pasajeros_por_fechas,
    lista_destinos_por_compañía,
    vuelos_entre_fechas,
    destinos_distintos_por_compañía,
    códigos_vuelos_más_plazas_que_por_número_de_escalas,
    vuelo_menor_duración_por_destino,

    compañía_con_más_pasajeros_por_destino,

    calcular_el_incremento_o_decremento_de_pasajeros
)

RUTA_CSV = str(pathlib.Path(__file__).parents[1] / "data" / "vuelos.csv")

# OJO: USO 'UNITTEST', UNA LIBRERÍA DE PYTHON QUE SE USA PROFESIONALMENTE PARA TESTEAR
# CÓDIGO, PERO PROBABLEMENTE NO SEA LO QUE EL PROFESOR QUIERA, COGE INSPIRACIÓN DE
# ESTE CÓDIGO BAJO TU PROPIA RESPONSABILIDAD
class TestVuelosFunctions(unittest.TestCase):
    def test_lee_vuelo(self):
        vuelos = lee_vuelos(RUTA_CSV)
        # Visualizamos los tres primeros registros
        print(vuelos[:3])
        
        self.assertEqual(len(vuelos), 91)
        self.assertEqual(vuelos[0].destino, "Madrid")
        self.assertEqual(vuelos[4].destino, "Barcelona")
        self.assertEqual(vuelos[9].destino, "Santiago")

    def test_filtra_vuelos_a(self):
        vuelos = lee_vuelos(RUTA_CSV)
        vuelos_madrid = filtra_vuelos_a(vuelos, "Madrid")
        self.assertEqual(len(vuelos_madrid), 20)
        for i in vuelos_madrid:
            self.assertEqual(i.destino, "Madrid")

    def test_vuelos_mas_velocidad_que(self):
        vuelos = lee_vuelos(RUTA_CSV)
        vuelos_rápidos = vuelos_mas_velocidad_que(vuelos, 750.0)
        # Comprobamos que hay noventa y un vuelos con velocidad > 750.0
        self.assertEqual(len(vuelos_rápidos), 91)

    def test_todos_vuelos_mas_velocidad_que(self):
        vuelos = lee_vuelos(RUTA_CSV)
        self.assertTrue(todos_vuelos_mas_velocidad_que(vuelos, 600.0))
        self.assertFalse(todos_vuelos_mas_velocidad_que(vuelos, 1000.0))

    def test_vuelos_más_velocidad(self):
        vuelos = lee_vuelos(RUTA_CSV)
        vuelo_rápido = vuelos_más_velocidad(vuelos)
        # Comprobamos que IBE-124 tiene la velocidad más alta
        self.assertEqual(vuelo_rápido.código, "IBE-124")

    def test_vuelos_por_horario(self):
        vuelos = lee_vuelos(RUTA_CSV)
        vuelos_enero = vuelos_por_horario(vuelos, 1)
        vuelos_septiembre = vuelos_por_horario(vuelos, 9)
        # Comprobamos que hay cero vuelos en enero y 41 septiembre
        self.assertEqual(len(vuelos_enero), 0)
        self.assertEqual(len(vuelos_septiembre), 41)

    def test_distintas_escalas(self):
        vuelos = lee_vuelos(RUTA_CSV)
        escalas = distintas_escalas(vuelos)
        # Asumimos que hay once paradas diferentes
        # self.assertEqual(len(escalas), 11)

    def test_vuelos_con_escalas_en(self):
        vuelos = lee_vuelos(RUTA_CSV)
        vuelos_con_escala = vuelos_con_escalas_en(vuelos, "Barcelona")
        # Asumimos que hay dos vuelos que tienen Barcelona como escala
        # self.assertEqual(len(vuelos_con_escala), 21)

    def test_número_de_vuelo_por_destino(self):
        vuelos = lee_vuelos(RUTA_CSV)
        destinos_count = número_de_vuelo_por_destino(vuelos)
        print(destinos_count)  # a) Visualizar el diccionario directamente
        for destino, cantidad in destinos_count.items():
            # b) Visualizar cada pareja clave-valor
            print(f"{destino}: {cantidad}")
        destino_input = input("Ingrese un destino: ")
        if destino_input in destinos_count:
            print("Hay vuelo")
        else:
            print("No hay vuelo")

    def test_suma_de_pasajeros_por_fechas(self):
        vuelos = lee_vuelos(RUTA_CSV)
        pasajeros_por_fecha = suma_de_pasajeros_por_fechas(vuelos)
        print(pasajeros_por_fecha)  # a) Visualizar el diccionario directamente
        for fecha, pasajeros in tuple(pasajeros_por_fecha.items())[:3]:
            # b) Visualizar cada pareja clave-valor (3 primeros)
            print(f"{fecha}: {pasajeros}")

        fecha_input = input("Selecciona una fecha (YYYY-MM-DD): ")
        fecha = date.fromisoformat(fecha_input)
        if fecha in pasajeros_por_fecha:
            print(pasajeros_por_fecha[fecha])
        else:
            print(0)

    def test_lista_destinos_por_compañía(self):
        vuelos = lee_vuelos(RUTA_CSV)
        destinos_por_comp = lista_destinos_por_compañía(vuelos)
        for compañía, destinos in destinos_por_comp.items():
            print(f"{compañía}: {destinos}")

    def test_vuelos_entre_fechas(self):
        vuelos = lee_vuelos(RUTA_CSV)
        fecha_inicio = date(2021, 6, 1)  # Reemplazar con la fecha de inicio que se desee
        fecha_fin = date(2021, 7, 1)  # Reemplazar con la fecha de fin que se desee
        vuelos_entre_fechas_ = vuelos_entre_fechas(vuelos, fecha_inicio, fecha_fin)
        for destino, precio, escalas in vuelos_entre_fechas_:
            print(f"Destino: {destino}, Precio: {precio}, Escalas: {escalas}")
    
    def test_compañía_con_más_pasajeros_por_destino(self):
        vuelos = lee_vuelos(RUTA_CSV)
        res = compañía_con_más_pasajeros_por_destino(vuelos)
        for i, j in res.items():
            print(i, j)
    
    # TODO: test para los ultimos ejercicios

    def test_calcular_el_incremento_o_decremento_de_pasajeros(self) -> None:
        vuelos = lee_vuelos(RUTA_CSV)

        

if __name__ == "__main__":
    
    vuelos = lee_vuelos(RUTA_CSV)
    res = compañía_con_más_pasajeros_por_destino(vuelos)
    print(res)
    for i, j in res.items():
        print(i, j)
    # unittest.main()
