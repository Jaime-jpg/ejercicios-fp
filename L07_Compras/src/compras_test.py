import pathlib
import compras


def test_lee_compras(datos) -> None:
    print(f"Registros leídos: {len(datos)}\n")
    print(f"Tres primeros: {datos[:3]}\n")
    print(f"Tres últimos: {datos[-3:]}")


def test_compra_maxima_minima_provincia(datos) -> None:
    print(f"{compras.compra_maxima_minima_provincia(datos, 'Huelva') = }")
    print(f"{compras.compra_maxima_minima_provincia(datos, None) = }")


def test_hora_menos_afluencia(datos) -> None:
    print(f"{compras.hora_menos_afluencia(datos) = }")


def test_supermercados_mas_facturacion(datos) -> None:
    print(f"{compras.supermercados_mas_facturacion(datos, n=2) = }")


def test_clientes_itinerantes(datos) -> None:
    print(f"{compras.clientes_itinerantes(datos, n=6) = }")
    print(f"{compras.clientes_itinerantes(datos, n=7) = }")


def test_dias_estrella(datos) -> None:
    print(f"{compras.dias_estrella(datos, 'Aldi', 'Huelva') = }")


def main() -> None:
    RUTA_CSV = pathlib.Path(__file__).parents[1] / "data" / "compras.csv"
    TESTS = (
        test_lee_compras,
        test_compra_maxima_minima_provincia,
        test_hora_menos_afluencia,
        test_supermercados_mas_facturacion,
        test_clientes_itinerantes,
        test_dias_estrella,
    )
    datos = compras.lee_compras(str(RUTA_CSV))

    for test in TESTS:
        print("=" * 10, test.__name__, "=" * 10)
        test(datos)
        print()


if __name__ == "__main__":
    main()
