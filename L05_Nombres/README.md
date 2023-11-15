## Fundamentos de Programación
# Ejercicio de laboratorio: Nombres
### Autor: José A. Troyano
---

En este proyecto trabajaremos con datos correspondientes a los nombres de las personas nacidas en España desde 2002 a 2017. Los datos están tomados del Instituto Nacional de Estadística, donde se pueden encontrar muchos datos interesantes principalmente sobre la demografía, economía y sociedad españolas. Representaremos la información de entrada mediante listas de tuplas, y a partir de esta estructura implementaremos una serie de funciones que nos permitirán realizar varios tipos de consultas y generar visualizaciones.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **nombres.py**: Contiene funciones para explotar los datos.
    * **nombres_test.py**: Contiene funciones de test para probar las funciones del módulo `nombres.py`. En este módulo está el main.
* **/data**: Contiene el dataset o datasets del proyecto
    * **frecuencias_nombres.csv**: Archivo con los datos de nombres de personas.

## Ejercicios a realizar

Trabajaremos con ficheros en formato CSV. Cada registro del fichero de entrada ocupa una línea y contiene cuatro informaciones sobre los nombres (año, nombre, frecuencia, genero). Estas son las  primeras líneas de un fichero de entrada: 

```
Año,Nombre,Frecuencia,Género
2002,ALEJANDRO,8020,Hombre
2002,PABLO,5799,Hombre
2002,DANIEL,5603,Hombre
2002,DAVID,5414,Hombre
```

Además de distintos indicadores, generaremos dos gráficas que mostrarán, respectivamente, la evolución del uso de un nombre determinado (Figura 1), o las frecuencias acumuladas de los nombres  más populares (Figura 2).

Figura 1             |  Figura 2
:-------------------------:|:-------------------------:
<img src="./img/Figura 1.png" alt="Figura 1: evolución de la frecuencia de un nombre" height="300"/>  |  <img src="./img/Figura 2.png" alt="Figura 2: frecuencias de los nombres más populares" height="300"/>




Para almacenar estos datos en memoria, utilizaremos tuplas con nombre con la siguiente definición:

``
FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')
``

El  objetivo  del  ejercicio  es  leer  estos  datos  y  realizar  distintas  operaciones  con  ellos.  Cada  operación  se implementará en una función distinta. Use funciones auxiliares cuando lo crea conveniente para mejorar la legibilidad del código. Defina las cabeceras de las funciones usando `typing`, es decir, especificando el tipo de los parámetros y el tipo del valor de retorno de las funciones mediante la biblioteca `typing`. Las funciones a implementar son:

1. **leer_frecuencias_nombres**: recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve una lista de tuplas de tipo FrecuenciaNombre(int, str, int, str) conteniendo todos los datos almacenados en el fichero.
2. **filtrar_por_genero**: recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, y devuelve una lista de tuplas de tipo FrecuenciaNombre con los registros del género recibido como parámetro.
3. **calcular_nombres**: recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, y devuelve un conjunto {str} con los nombres del género recibido como parámetro. El género puede ser 'Hombre', 'Mujer' o tener un valor None, en cuyo caso se incluyen en el conjunto todos los nombres. El valor por defecto del género es None. 
4. **calcular_top_nombres_de_año**: recibe una lista de tuplas de tipo FrecuenciaNombre, un año de tipo int, un número límite de tipo int y un género de tipo str, y devuelve una lista de tuplas (nombre, frecuencia) de tipo (str, int) con los nombres más frecuentes del año y el género dados, ordenada de mayor a menor frecuencia, y con un máximo de límite nombres. El género puede ser 'Hombre', 'Mujer' o tener un valor None, en cuyo caso se incluyen en la lista todos los nombres. El valor por defecto del límite es 10 y el del género es None.
5. **calcular_nombres_ambos_generos**: recibe una lista de tuplas de tipo FrecuenciaNombre, y devuelve un conjunto {str} con los nombres que han sido utilizados en ambos géneros.
6. **calcular_nombres_compuestos**: recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, y devuelve un conjunto {str} con los nombres que contienen más de una palabra. El género puede ser 'Hombre', 'Mujer' o tener un valor None, en cuyo caso se incluyen en el conjunto todos los nombres. El valor por defecto del género es None.
7. **calcular_nombre_mas_frecuente_por_año**: recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, y devuelve una lista de tuplas (año, nombre, frecuencia) de tipo (int, str, int) ordenada por año con el nombre más frecuente de cada año. El género puede ser ‘Hombre’, ‘Mujer’ o tener un valor None, en cuyo caso se incluyen en la lista todos los nombres. El valor por defecto del género es None. Se calculará en primer lugar la lista de años y, posteriormente, se buscará el nombre más frecuente para cada año.
8. **calcular_frecuencia_por_año**: recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre de tipo str, y devuelve una lista de tuplas (año, frecuencia) de tipo (int, int) ordenada por año  con la frecuencia del nombre en cada año. En el caso de que un nombre se use para hombres y mujeres, se sumarán ambas frecuencias.
9. **mostrar_evolucion_por_año**: recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre de tipo str, y genera un gráfico con la evolución de la frecuencia del nombre a lo largo de los años(Figura 1). Se usarán las siguientes instrucciones para generar la gráfica:
```
plt.plot(años, frecuencias)
plt.title("Evolución del nombre '{}'".format(nombre))
plt.show()
```
Donde años y frecuencias se extraen del resultado de la función calcular_frecuencia_por_año.

10. **calcular_frecuencia_acumulada**: recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre de tipo str, y devuelve la frecuencia acumulada del nombre en todos los años
11. **calcular_frecuencias_por_nombre**: recibe una lista de tuplas de tipo FrecuenciaNombre, y devuelve un diccionario {str: int} que relaciona cada nombre con la frecuencia acumulada del nombre.

12. **mostrar_frecuencias_nombres**: recibe una lista de tuplas de tipo FrecuenciaNombre y un número límite de tipo int, y genera un diagrama de barras con las frecuencias de los nombres más populares, en orden decreciente de popularidad y con un máximo de límite nombres (Figura 2). El valor por defecto del límite es 10. Se usarán las siguientes instrucciones para generar la gráfica:
```
plt.bar(nombres, frecuencias)
plt.xticks(rotation=80)
plt.title("Frecuencia de los {} nombres más comunes".format(limite))
plt.show()
```
Donde nombres y frecuencias se extraen del resultado de la función calcular_frecuencias_por_nombre. El cálculo de los nombres más populares se puede realizar ordenando las claves del diccionario devuelto por calcular_frecuencias_por_nombre en función de sus valores asociados.


Cree un fichero `nombres_TEST.py`. Importe todas las funciones del módulo `nombres.py`. Cargue los datos del fichero CSV y muestre en consola los datos leídos. Incluya llamadas a todas las funciones implementadas, mostrando los resultados en la consola.

```
TEST de 'leer_frecuencias_nombres'

Leídos 3505 registros
Mostrando los 3 primeros:
    [Registro(año=2002, nombre='ALEJANDRO', frecuencia=8020, genero='Hombre'), Registro(año=2002, nombre='PABLO', frecuencia=5799, genero='Hombre'), Registro(año=2002, nombre='DANIEL', frecuencia=5603, genero='Hombre')]

Mostrando los 3 últimos:
    [Registro(año=2017, nombre='NAIARA', frecuencia=330, genero='Mujer'), Registro(año=2017, nombre='NAHIA', frecuencia=322, genero='Mujer'), Registro(año=2017, nombre='ELISA', frecuencia=317, genero='Mujer')]

####################################################################################

TEST de 'filtrar_por_genero'
   - Número de registros para 'Hombre': 1752
   - Número de registros para 'Mujer': 1753

####################################################################################

TEST de 'calcular_nombres'
   - Ambos géneros: ['AARON', 'ABEL', 'ABRAHAM', 'ABRIL', 'ADAM', 'ADAN', 'ADARA', 'ADRIA', 'ADRIAN', 'ADRIANA']
   - Hombres: ['AARON', 'ABEL', 'ABRAHAM', 'ABRIL', 'ADAM', 'ADAN', 'ADRIA', 'ADRIAN', 'AGUSTIN', 'AIMAR']
   - Mujeres: ['ABRIL', 'ADARA', 'ADRIANA', 'AFRICA', 'AIDA', 'AINA', 'AINARA', 'AINHOA', 'AINOA', 'AITANA']

####################################################################################

TEST de 'calcular_top_nombres_de_año' para 2008
   - Ambos géneros: [('LUCIA', 8013), ('MARIA', 6883), ('PAULA', 6806), ('DANIEL', 6580), ('ALEJANDRO', 6478), ('PABLO', 5911), ('DAVID', 5385), ('ADRIAN', 5330), ('HUGO', 5162), ('ALVARO', 5034)]
   - Hombres: [('DANIEL', 6580), ('ALEJANDRO', 6478), ('PABLO', 5911), ('DAVID', 5385), ('ADRIAN', 5330), ('HUGO', 5162), ('ALVARO', 5034), ('JAVIER', 4091), ('DIEGO', 3506), ('SERGIO', 3401)]
   - Mujeres: [('LUCIA', 8013), ('MARIA', 6883), ('PAULA', 6806), ('SARA', 4730), ('CARLA', 4271), ('CLAUDIA', 4095), ('LAURA', 4023), ('MARTA', 3927), ('IRENE', 3759), ('ALBA', 3706)]

####################################################################################

TEST de 'calcular_nombres_ambos_generos'
   - Nombres: {'ABRIL'}

####################################################################################

TEST de 'calcular_nombres_compuestos'
   - Ambos géneros: ['ALBA MARIA', 'ANA BELEN', 'ANA ISABEL', 'ANA MARIA', 'ANTONIO JESUS', 'ANTONIO JOSE', 'CARMEN MARIA', 'EVA MARIA', 'FRANCISCO JAVIER', 'FRANCISCO JOSE', 'ISABEL MARIA', 'JOSE ANGEL', 'JOSE ANTONIO', 'JOSE CARLOS', 'JOSE LUIS', 'JOSE MANUEL', 'JOSE MARIA', 'JOSE MIGUEL', 'JUAN ANTONIO', 'JUAN CARLOS', 'JUAN FRANCISCO', 'JUAN JOSE', 'JUAN MANUEL', 'LUIS MIGUEL', 'MARIA DEL CARMEN', 'MARIA DEL MAR', 'MARIA ISABEL', 'MARIA JOSE', 'MIGUEL ANGEL']
   - Hombres: ['ANTONIO JESUS', 'ANTONIO JOSE', 'FRANCISCO JAVIER', 'FRANCISCO JOSE', 'JOSE ANGEL', 'JOSE ANTONIO', 'JOSE CARLOS', 'JOSE LUIS', 'JOSE MANUEL', 'JOSE MARIA', 'JOSE MIGUEL', 'JUAN ANTONIO', 'JUAN CARLOS', 'JUAN FRANCISCO', 'JUAN JOSE', 'JUAN MANUEL', 'LUIS MIGUEL', 'MIGUEL ANGEL'] 
   - Mujeres: ['ALBA MARIA', 'ANA BELEN', 'ANA ISABEL', 'ANA MARIA', 'CARMEN MARIA', 'EVA MARIA', 'ISABEL MARIA', 'MARIA DEL CARMEN', 'MARIA DEL MAR', 'MARIA ISABEL', 'MARIA JOSE']

####################################################################################

TEST de 'calcular_nombre_mas_frecuente_por_año'
   - Ambos géneros: [(2002, 'MARIA', 8838), (2003, 'MARIA', 8709), (2004, 'LUCIA', 10370), (2005, 'LUCIA', 10146), (2006, 'LUCIA', 9454), (2007, 'LUCIA', 8192), (2008, 'LUCIA', 8013), (2009, 'LUCIA', 6847), (2010, 'LUCIA', 6624), (2011, 'LUCIA', 6143), (2012, 'LUCIA', 6363), (2013, 'HUGO', 5369), (2014, 'LUCIA', 5161), (2015, 'LUCIA', 5229), (2016, 'HUGO', 4870), (2017, 'LUCIA', 4410)]
   - Hombres: [(2002, 'ALEJANDRO', 8020), (2003, 'DANIEL', 6015), (2004, 'ALEJANDRO', 7381), (2005, 'ALEJANDRO', 7173), (2006, 'ALEJANDRO', 7581), (2007, 'DANIEL', 6755), (2008, 'DANIEL', 6580), (2009, 'DANIEL', 6227), (2010, 'DANIEL', 6020), (2011, 'ALEJANDRO', 5879), (2012, 'DANIEL', 6234), (2013, 'HUGO', 5369), (2014, 'HUGO', 5121), (2015, 'HUGO', 5162), (2016, 'HUGO', 4870), (2017, 'LUCAS', 4209)]
   - Mujeres: [(2002, 'MARIA', 8838), (2003, 'MARIA', 8709), (2004, 'LUCIA', 10370), (2005, 'LUCIA', 10146), (2006, 'LUCIA', 9454), (2007, 'LUCIA', 8192), (2008, 'LUCIA', 8013), (2009, 'LUCIA', 6847), (2010, 'LUCIA', 6624), (2011, 'LUCIA', 6143), (2012, 'LUCIA', 6363), (2013, 'LUCIA', 5206), (2014, 'LUCIA', 5161), (2015, 'LUCIA', 5229), (2016, 'LUCIA', 4672), (2017, 'LUCIA', 4410)]

####################################################################################

TEST de 'calcular_frecuencia_por_año'
   - IKER: [(2002, 1178), (2003, 1528), (2004, 1691), (2005, 1972), (2006, 2479), (2007, 2509), (2008, 3086), (2009, 2856), (2010, 2795), (2011, 2535), (2012, 2694), (2013, 2082), (2014, 1917), (2015, 1513), (2016, 1307), (2017, 1095)]

####################################################################################

TEST de 'mostrar_evolucion_por_año'
(Muestra gráfica)

####################################################################################

TEST de 'calcular_frecuencia_acumulada'
   - IKER: 33237

####################################################################################

TEST de 'calcular_frecuencias_por_nombre'
   - Frecuencias: {'AINOA': 600, 'ITZIAR': 654, 'REBECA': 2538, 'NOELIA': 12879, 'RAYAN': 6112, 'ESTEFANIA': 672, 'BRIAN': 201, 'ARITZ': 380, 'ENRIQUE': 10452, 'EMILIO': 797, 'CLAUDIA': 52204, 'UXUE': 656, 'GUILLEM': 5194, 'ABEL': 1074, 'ENZO': 7587, 'MARCO': 14018, 'NEIZAN': 413, 'SARA': 59326, 'SILVIA': 11419, 'MARKEL': 669, 'PEDRO': 18388, 'OMAR': 4387, 'FERNANDO': 14452, 'SARAY': 3922, 'JOSE MARIA': 4401, 'MARTIN': 29381, 'GEMA': 1476, 'NAZARET': 206, 'EVA': 15793, 'IMRAN': 371, 'CARMEN MARIA': 481, 'AIMAR': 3901, 'XABIER': 878, 'AITANA': 24323, 'JUDITH': 5367, 'DIEGO': 48543, 'FRANCISCO JAVIER': 11150, 'CELIA': 17869, 'DIANA': 6792, 'IAN': 5711, 'CECILIA': 386, 'ALEXANDRA': 2404, 'JOAN': 11877, 'GAEL': 4832, 'JULIETA': 395, 'NAROA': 539, 'CLOE': 1078, 'LEIRE': 15103, 'NEREA': 33241, 'TOMAS': 1016, 'JESUS': 22830, 'IVAN': 37906, 'AURORA': 190, 'LOLA': 15133, 'ERIKA': 8290, 'CANDELA': 18306, 'SUSANA': 944, 'ISABEL MARIA': 213, 'MIGUEL': 36454, 'NAHIA': 4604, 'YERAY': 5976, 'NAYARA': 7113, 'NORA': 13015, 'UXIA': 453, 'RUBEN': 30626, 'NIL': 5204, 'VERONICA': 1969, 'SERGI': 4477, 'MARTI': 9667, 'CARLOS': 40792, 'ALEIX': 7156, 'LIA': 1994, 'PAOLA': 8475, 'PAU': 18965, 'THIAGO': 4069, 'IÑIGO': 1043, 'ISABEL': 13668, 'ROSA': 722, 'ALEJANDRO': 86354, 'ABRAHAM': 1614, 'ANTONIO': 32178, 'JUAN ANTONIO': 3583, 'MARIA ISABEL': 648, 'MAIDER': 186, 'MARCOS': 41130, 'CLARA': 17388, 'IRIA': 7267, 'ERIK': 10338, 'IKER': 33237, 'SOFIA': 48138, 'AYA': 6375, 'LYDIA': 870, 'MARIO': 46308, 'CAROLINA': 12448, 'ALONSO': 5853, 'SHEILA': 3895, 'AARON': 18509, 'NOEMI': 2039, 'ESTELA': 1773, 'NAIA': 4816, 'LUCA': 3339, 'JON': 4348, 'ELIAS': 238, 'ADRIA': 6386, 'ADRIANA': 25806, 'JAVIER': 56915, 'NATALIA': 27045, 'GISELA': 2473, 'IAGO': 238, 'MOISES': 725, 'ADARA': 337, 'PALOMA': 1026, 'VERA': 7686, 'JOAQUIN': 3717, 'YOLANDA': 704, 'TEO': 382, 'ALBA MARIA': 889, 'YAGO': 2944, 'ISMAEL': 16679, 'BARBARA': 450, 'AINARA': 17039, 'AIDA': 988, 'LIAM': 909, 'MARIA DEL MAR': 767, 'RAMON': 1111, 'LUCIA': 104542, 'ANTONIO JESUS': 230, 'ANA ISABEL': 456, 'ESTHER': 4723, 'ANDRES': 14005, 'RICARDO': 1250, 'AZAHARA': 420, 'ANE': 4306, 'JENNIFER': 774, 'ELISA': 1663, 'HECTOR': 22730, 'JONATHAN': 1370, 'IGNACIO': 14376, 'DAVID': 72677, 'CRISTIAN': 13220, 'MIQUEL': 925, 'SANTIAGO': 11257, 'VICENTE': 831, 'IRIS': 4122, 'FRANCISCO JOSE': 2356, 'AMANDA': 802, 'CESAR': 4516, 'ADAN': 243, 'SERGIO': 46986, 'MALAK': 4156, 'MANUELA': 7009, 'SAMUEL': 25988, 'VALERIA': 28607, 'JUNE': 220, 'ALAN': 491, 'MIREIA': 8736, 'MARIA JOSE': 1096, 'ALMUDENA': 790, 'ALBERT': 1419, 'BEATRIZ': 6610, 'RAQUEL': 10536, 'POL': 13383, 'MIRIAM': 12044, 'LAURA': 55627, 'LUIS MIGUEL': 513, 'LUCAS': 34465, 'VICTORIA': 13356, 'ALVARO': 68127, 'YAIZA': 4991, 'ALBA': 57791, 'JOEL': 16672, 'UNAI': 13697, 'ROGER': 2443, 'JUAN FRANCISCO': 801, 'VEGA': 8336, 'AITOR': 20790, 'CARMEN': 36692, 'ANNA': 8488, 'OIER': 703, 'AFRICA': 7130, 'SALMA': 7396, 'IRENE': 43306, 'ELIA': 1582, 'VANESSA': 188, 'FERRAN': 813, 'BIEL': 8037, 'INDIA': 364, 'IZARO': 416, 'YASMINA': 633, 'JESSICA': 707, 'YOUSSEF': 1397, 'TANIA': 2033, 'JUAN': 29495, 'TERESA': 4105, 'SALVADOR': 1027, 'ERIC': 17619, 'BERTA': 8235, 'TRIANA': 4077, 'HUGO': 69493, 'LORENA': 7682, 'GABRIELA': 8516, 'RAFAEL': 16346, 'JUAN CARLOS': 2711, 'NAIARA': 9548, 'ALEXIA': 4985, 'ARNAU': 12135, 'CHLOE': 4669, 'GUILLERMO': 20504, 'MARA': 4234, 'BELEN': 1836, 'JULEN': 3404, 'ALEX': 29578, 'CARLES': 222, 'ASIER': 12118, 'NOAH': 1221, 'AMIR': 417, 'JORDI': 8582, 'ALICIA': 18173, 'MAIALEN': 201, 'NAIM': 195, 'ARTURO': 1246, 'PABLO': 84075, 'ZOE': 3997, 'MARTINA': 40519, 'OLIVER': 7693, 'MARIA': 100165, 'LETICIA': 214, 'GORKA': 469, 'ALBERTO': 22107, 'ARIADNA': 20024, 'NOUR': 330, 'LEO': 15552, 'IZAN': 24909, 'CAYETANA': 1262, 'ABRIL': 9640, 'CHRISTIAN': 4330, 'IRATI': 2069, 'JOSE MIGUEL': 1115, 'GALA': 1029, 'AXEL': 392, 'KEVIN': 4262, 'MATEO': 22770, 'RODRIGO': 18857, 'MIREYA': 653, 'MARINA': 27150, 'ANGEL': 26445, 'XAVIER': 2906, 'ROBERTO': 8650, 'GEMMA': 727, 'BRUNO': 13675, 'OLGA': 759, 'BRAIS': 698, 'INES': 23162, 'ANA BELEN': 439, 'ANDREA': 37278, 'LAIA': 20498, 'MANUEL': 42729, 'EVA MARIA': 405, 'DANIEL': 90883, 'JANA': 5799, 'JOSE MANUEL': 10418, 'ELSA': 9897, 'LUIS': 17589, 'JOSE ANTONIO': 11278, 'MAURO': 1462, 'VIRGINIA': 706, 'DENIS': 218, 'RAUL': 29504, 'DARIO': 14946, 'MARTA': 52506, 'NADIA': 5147, 'AINHOA': 27925, 'ANA MARIA': 5021, 'RUTH': 729, 'JAIRO': 243, 'JOSEP': 844, 'PILAR': 935, 'JUAN JOSE': 5963, 'INMACULADA': 774, 'ALFONSO': 1310, 'ENEKO': 1354, 'JAN': 9162, 'AINA': 10261, 'GONZALO': 24269, 'NURIA': 17402, 'SAUL': 7603, 'EDGAR': 715, 'VALENTINA': 11625, 'BORJA': 1556, 'JOSE LUIS': 4960, 'DANIELA': 47098, 'ARLET': 2371, 'JAUME': 773, 'OLIVIA': 8109, 'MAR': 9964, 'AGUSTIN': 211, 'AMIRA': 824, 'JIMENA': 14965, 'ANDER': 3487, 'FRANCISCO': 21021, 'PAULA': 88706, 'MIGUEL ANGEL': 14134, 'GERARD': 8902, 'GERMAN': 430, 'NEUS': 587, 'SONIA': 2864, 'ALMA': 7780, 'DYLAN': 4788, 'INGRID': 200, 'MARIAM': 212, 'ADRIAN': 69044, 'JOSE': 22036, 'LUNA': 6612, 'ANA': 37253, 'JORGE': 38146, 'FATIMA': 5527, 'VANESA': 400, 'LARA': 11146, 'ADAM': 14521, 'SANDRA': 12631, 'HELENA': 8575, 'MATIAS': 427, 'MOHAMED': 13169, 'ELENA': 33420, 'DESIREE': 1061, 'MARC': 30603, 'BLANCA': 16874, 'SORAYA': 1044, 'EDUARDO': 9714, 'GABRIEL': 20319, 'ANTIA': 602, 'ALEJANDRA': 25459, 'YANIRA': 2235, 'JAIME': 19745, 'IBAI': 919, 'ELOY': 785, 'JOSE CARLOS': 727, 'LIDIA': 7480, 'CRISTINA': 21769, 'ORIOL': 6638, 'LEYRE': 10421, 'MARIONA': 729, 'NOA': 28502, 'JUDIT': 1846, 'NICOLAS': 28497, 'ANTONIO JOSE': 212, 'ONA': 3238, 'OSCAR': 18793, 'ALEXANDER': 691, 'ISAAC': 8254, 'GLORIA': 725, 'JUAN MANUEL': 4454, 'MERCEDES': 422, 'VICTOR': 28066, 'JULIA': 43826, 'ZAIRA': 1489, 'MONICA': 4967, 'PATRICIA': 11152, 'MIA': 3857, 'AROA': 12049, 'JULIO': 915, 'MIKEL': 3152, 'ISRAEL': 788, 'CARLOTA': 17849, 'JOSE ANGEL': 449, 'EMMA': 23546, 'CARLA': 53482, 'ROCIO': 23533, 'MARIA DEL CARMEN': 1622, 'JULIAN': 726, 'ANGELA': 22555, 'SEBASTIAN': 715}

####################################################################################

TEST de 'mostrar_frecuencias_nombres'
(Muestra gráfica)

```
