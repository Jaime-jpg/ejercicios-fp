from centros import *

def main() -> None:
    centros = leer_centros("L04_Centros_sanitarios/data/centrosSanitarios.csv")
    
    generar_mapa(obtener_centros_con_uci_cercanos_a(centros, Coordenadas(36.17645223264249, -5.554934952989551), 0.5))


if __name__ == "__main__":
    main()
