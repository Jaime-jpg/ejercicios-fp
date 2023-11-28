from math import sqrt

def raices(
    a: int | float,
    b: int | float,
    c: int | float,
) -> tuple[float | None, float | None]:
    discriminante = b ** 2 - 4 * a * c
    
    if (a != 0) and (discriminante >= 0):
        return (
            (- b + sqrt(discriminante)) / (2 * a),
            (- b + sqrt(discriminante)) / (2 * a),
        )

    return None, None
