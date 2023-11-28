from datos_personales import (
    lee_datos_personales,
    lee_datos_personales2,
    lee_datos_personales3,
    lee_datos_personales4,
)

RUTA_CSV = "C:/Users/jaime/Documents/ProyectosPython/T09_Datos_Personales/data/"
RUTA_ARCHIVO_1 = RUTA_CSV + "datos_personales.csv"
RUTA_ARCHIVO_2 = RUTA_CSV + "datos_personales2.csv"
RUTA_ARCHIVO_3 = RUTA_CSV + "datos_personales3.csv"
RUTA_ARCHIVO_4 = RUTA_CSV + "datos_personales4.csv"


def main() -> None:
    formato_personas = lambda x: "\n" + "\n\n".join(str(i) for i in x)
    
    personas = lee_datos_personales(RUTA_ARCHIVO_1)
    
    print(f"Leídos {len(personas)} registros\n")
    print(f"Tercer registro (sin contar la cabecera): {personas[3]}\n")
    
    # cuento la cabecera en este caso porque el enunciado no dice nada
    print(f"Tres primeros registros: {personas[:3]}\n")
    print(f"Tres últimos registros: {personas[-3:]}\n")
    

    # ============================================
    # lo mismo para la segunda parte del ejercicio
    print("=" * 50, end="\n\n")
    personas = lee_datos_personales2(RUTA_ARCHIVO_2)
    
    print(f"Leídos {len(personas)} registros\n")
    print(f"Tercer registro (sin contar la cabecera): {personas[3]}\n")
    
    # cuento la cabecera en este caso porque el enunciado no dice nada
    print(f"Tres primeros registros: {personas[:3]}\n")
    print(f"Tres últimos registros: {personas[-3:]}\n")


    # ============================================
    # lo mismo para la tercera parte del ejercicio
    print("=" * 50, end="\n\n")
    personas = lee_datos_personales3(RUTA_ARCHIVO_3)
    
    print(f"Leídos {len(personas)} registros\n")
    print(f"Tercer registro (sin contar la cabecera): {personas[3]}\n")
    
    # cuento la cabecera en este caso porque el enunciado no dice nada
    print(f"Tres primeros registros: {personas[:3]}\n")
    print(f"Tres últimos registros: {personas[-3:]}\n")


    # ============================================
    # lo mismo para la cuarta parte del ejercicio
    print("=" * 50, end="\n\n")
    personas = lee_datos_personales4(RUTA_ARCHIVO_4)
    
    print(f"Leídos {len(personas)} registros\n")
    print(f"Tercer registro (sin contar la cabecera): {personas[3]}\n")
    
    # cuento la cabecera en este caso porque el enunciado no dice nada
    print(f"Tres primeros registros: {formato_personas(personas[:3])}\n")
    print(f"Tres últimos registros: {formato_personas(personas[-3:])}\n")


if __name__ == "__main__":
    main()
