from calificaciones import nota_teoria, nota_cuatrimestre, nota_continua
from calificaciones_ui import solicita_notas


test_nota_teoria = (9.1, 7.2), (4.0, 6.0), (4.0, 3.0), (None, 3.0), (9.0, None)

test_cuatrimestre = (
    ((9.1, 7.2), 8.1),
    ((4.0, 6.0), 5.0),
    ((4.0, 3.0), None),
    ((None, 3.0), None),
    ((9.0, None), 4.5),
)

test_continua = (
    ((9.6, 9.9, 10.0, 9.8), (9.7, 9.5)),
    ((4.4, 4.9, 5.1, 4.7), (4.6, 4.8)),
    ((4.0, 6.0, 4.0, 3.0), (5.0, None)),
    ((9.0, None, 4.0, 3.0), (4.5, None)),
)


def main() -> None:
    for i in test_nota_teoria:
        print(f"{i[0]}, {i[1]} ==> {nota_teoria(*i)}")
    print()

    for i in test_cuatrimestre:
        print(f"{i[0]}, {i[1]} ==> {nota_cuatrimestre(*i)}")
    print()

    for i in test_continua:
        print(
            f"notas teoría: {i[0]} "
            f"notas práctico: {i[1]} "
            f"==> {nota_continua(*i)}"
        )
    print()

    nombre, notas_teoria, notas_practica = solicita_notas()

    teoria_1 = notas_teoria[:2]
    media_teoria_1 = nota_teoria(*teoria_1)

    teoria_2 = notas_teoria[2:]
    media_teoria_2 = nota_teoria(*teoria_2)

    print(f"Hola, {nombre}")

    print(f"Tus notas del primer cuatrimestre son:")
    print(
        f" teoria {media_teoria_1}, práctica {notas_practica[0]},"
        f" cuatrimestre {nota_cuatrimestre(teoria_1, notas_practica[0])}"
    )

    print(f"Tus notas del segundo cuatrimestre son:")
    print(
        f" teoria {media_teoria_2}, práctica {notas_practica[1]},"
        f" cuatrimestre {nota_cuatrimestre(teoria_2, notas_practica[1])}"
    )

    print(
        f"Tu nota final de la asignatura es {nota_continua(notas_teoria, notas_practica)}"
    )


if __name__ == "__main__":
    main()
