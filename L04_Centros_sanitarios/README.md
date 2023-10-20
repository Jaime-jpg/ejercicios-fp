## Fundamentos de Programación
# Ejercicio de laboratorio: Centros Sanitarios
### Autora: Toñi Reina
### Revisor: Mariano González
---


En este proyecto trabajaremos con datos proporcionados por la diputación de Cádiz de centros sanitarios de los municipios con población inferior a 50.000 habitantes de dicha provincia. 

## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **centros.py**: Contiene funciones para explotar los datos de los centros sanitarios.
    * **centros_test.py**: Contiene funciones de test para probar las funciones del módulo `centros.py`. En este módulo está el main.
    * **coordenadas.py**: Contiene funciones para trabajar con el tipo Coordenadas.
    * **coordenadas_test.py**: Contiene funciones de test para probar las funciones del módulo `coordenadas.py`.
    * **mapas.py**: Contiene funciones para crear un mapa y representar puntos en él. Requiere tener instalada la librería folium.
* **/data**: Contiene el dataset o datasets del proyecto
    * **centrosSanitarios.csv**: Archivo con los datos de población de diversos paises o agrupaciones de paises en distintos años.

## Dependencias
En este ejercicio vamos a trabajar con mapas, para lo que usaremos la librería folium . Para instalar la librería folium abre una ventana de comandos de Anaconda (Anaconda Prompt) y ejecuta el siguiente comando:
```
pip install folium
```
o este otro si tienes como instalador conda:

```
conda install –c conda-forge folium
```
## Funciones a implementar:
Lee las [instrucciones](##Instrucciones) del proyecto que se indican a continuación para tener más detalles de los requisitos que deben cumplir las funciones a implementar.

### Módulo coordenadas

* **calcular_distancia**: recibe dos coordenadas de tipo ```Coordenadas(float, float)``` y devuelve un float que representa la distancia euclídea entre esas dos coordenadas.
* **calcular_media_coordenadas**: recibe una lista de ```Coordenadas(float, float)``` y devuelve una tupla de tipo ```Coordenadas(float, float)``` cuya latitud es la media de las latitudes de la lista y cuya longitud es la media de las longitudes de la lista.

### Módulo centros

* **leer_centros**: recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve una lista de tuplas de tipo ```CentroSanitario(str, str, Coordenadas(float, float), str, int, bool, bool)``` conteniendo todos los datos almacenados en el fichero. 
* **calcular_total_camas_centros_accesibles**: recibe una lista de tuplas de tipo ```CentroSanitario``` y produce como salida un entero correspondiente al número total de camas de los centros sanitarios accesibles para discapacitados.
* **obtener_centros_con_uci_cercanos_a**: recibe una lista de tuplas de tipo ```CentroSanitario```; una tupla de tipo ```Coordenadas```, que representa un punto; y un float, que representa un umbral de distancia. Produce como salida una lista de tuplas ```(str, str, Coordenadas(float, float))``` con el nombre, del centro, la localidad y las coordenadas de los centros situados a una distancia de las coordenadas dadas como parámetro menor o igual que el umbral dado. Observe la Figura 3 para entender mejor el resultado de la función.
![image](https://user-images.githubusercontent.com/72299672/195154929-a0c9fa7b-6f05-4289-b4ee-ea33d011d491.png)
 
* **generar_mapa**: recibe una lista de tuplas ```(str, str, Coordenadas(float, float))``` con el nombre, del centro, la localidad y las coordenadas del centro; y una cadena, que representa la ruta de un fichero html, que se generará con los centros geolocalizados. 

## Instrucciones

Los datos de los que partimos en el proyecto están en el fichero [centrosSanitarios.csv](./centrosSanitarios.csv). Si abres el fichero, comprobarás que es un fichero en formato CSV (los datos están separados por punto y coma). Un extracto del mismo lo puede ver en la Figura 1.

![image](https://user-images.githubusercontent.com/72299672/195154225-c2f72261-997a-43a6-9862-8021ecd1e18a.png)

Como puedes observar, cada línea del fichero contiene el nombre de un centro sanitario, la localidad, la latitud, la longitud, el estado del centro, el número de camas que tiene, si tiene acceso para discapacitados y si tiene UCI (en ambos casos, el valor false representa que no tiene acceso o no tiene UCI, respectivamente).

En el proyecto tendrás que implementar algunas funciones que nos ayuden a explotar los datos de los que disponemos. El objetivo del ejercicio es que trabajes creando un proyecto desde cero, e implementes tanto las funciones como los tests para comprobar que las funciones trabajan como se espera. El proyecto creado debe tener la estructura indicada en la sección [Estructura de las carpetas del proyecto](https://github.com/Fundamentos-de-Programacion-Profesores/LAB-Centros-sanitarios/edit/main/README.md#estructura-de-las-carpetas-del-proyecto).

Para gestionar las coordenadas en el módulo `coordenadas.py` se usará la siguiente definición de `namedtuple`:
```python
Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')
```

En dicho módulo, implementa las funciones que se indican a continuación, teniendo en cuenta la especificación de las mismas dada en la descripcion del módulo [coordenadas](https://github.com/Fundamentos-de-Programacion-Profesores/LAB-Centros-sanitarios/edit/main/README.md#m%C3%B3dulo-coordenadas); además, una vez implementada una función, implementa su test correspondiente en el módulo `coordenadas_test.py` y comprueba que funciona como se espera.

1.	`calcular_distancia`
2.	`calcular_media_coordenadas` 

Para gestionar la información de los centros sanitarios se usará la siguiente definición de namedtuple en el módulo `centros.py`:
```python
CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci')
```
Implementa las funciones que se especifican a continuación en dicho [módulo](https://github.com/Fundamentos-de-Programacion-Profesores/LAB-Centros-sanitarios/edit/main/README.md#m%C3%B3dulo-centros). Una vez implementada una función, implementa su test correspondiente en el módulo `centros_test.py` y comprueba que funciona como se espera.

1.	`leer_centros`
2.	`calcular_total_camas_centros_accesibles`
3.	`obtener_centros_con_uci_cercanos_a`
4.	`generar_mapa`


Para implementar la función `generar_mapa` ayúdate de las funciones auxiliares que se implementan en el módulo [mapas.py](./src/mapas.py). Además, ten en cuenta que:
1.	Primero debes crear un mapa. Usa la media de las coordenadas de los centros para centrar el mapa.
2.	Después ve agregando los marcadores al mapa que has creado mediante la función ```mapas.agrega_marcador```.
3.	Una vez añadidos todos los marcadores, guarda el mapa en el archivo html con `mapas.guarda_mapa`.

El resultado deber ser un fichero con un mapa similar al de la Figura 4, que se abrirá automáticamente en un navegador web.

![image](https://user-images.githubusercontent.com/72299672/195155059-9ba41234-51ed-4c45-a812-5792a30a5831.png)
 
| RETO |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| La fórmula de la distancia euclídea empleada en este proyecto no es la más adecuada cuando se quieren calcular distancias entre dos puntos del globo terrestre, ya que no tiene en cuenta la curvatura de la tierra. Para calcular la distancia entre dos puntos del globo terrestre se usa una aproximación que viene dada por la fórmula de Haversine . Implemente una función `distancia_harvesine` para que en el proyecto se hagan unos cálculos más realistas. |
