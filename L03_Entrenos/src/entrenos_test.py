from entrenos import (
    Entreno,
    lee_entrenos,
    filtra_por_ubicacion,
    tipos_entrenamiento,
    distancia_total_de_momento_dia,
)

from datetime import date


RUTA_CSV = "L03_Entrenos/data/entrenos.csv"


def main() -> None:
    entrenos = lee_entrenos(RUTA_CSV)

    print("\n".join(str(entrenos)))
    print()
    
    print("\n".join(str(filtra_por_ubicacion(entrenos, "Sevilla"))))
    print()
    
    print(
        f"Números de tipos de entrenamiento: {tipos_entrenamiento(entrenos, None, date(2020, 9, 27))}"
    )
    print()
    
    print(
        f"Distancia recorrida por la tarde: {distancia_total_de_momento_dia(entrenos, 'TARDE'):.2f} km"
    )
    print()


if __name__ == "__main__":
    main()
