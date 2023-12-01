## FUNDAMENTOS DE PROGRAMACIÓN. 
### EXTENSIÓN PRIMER EXAMEN PARCIAL. Enero 2023

Se tienen datos sobre un conjunto de partidos de tenis disputados al mejor de tres sets, de forma que gana el partido el primer jugador que gana dos sets. Si cada jugador gana uno de los dos primeros, se disputa un tercer set. En ese caso, el que gana este éltimo set gana el partido. Los datos tienen esta forma:

```
13/12/2014;Ugo Humbert;Pedro Martínez;Tierra;6-7;6-2;3-6;8;10
9/7/2020;Adrian Mannarino;Botic Van de Zandschulp;Dura;1-6;1-6;0-0;3;5
```

La información de cada línea se corresponde con lo siguiente:

- **fecha del partido**:  fecha en la que se celebra el partido, de tipo date.
- **primer jugador**: nombre del primer jugador, de tipo str.
- **segundo jugador**: nombre del segundo jugador, de tipo str.
- **superficie**: superficie en la que se juega el partido, de tipo str.
- **resultado del primer set**: resultado del primer set en formato int-int. El primer némero representa los juegos ganados por el primer jugador y el segundo los que ha ganado el segundo jugador. El jugador que más puntos tiene es el que gana el set.
- **resultado del segundo set**: resultado del segundo set en formato int-int.
- **resultado del tercer set**: resultado del tercer set en formato int-int. Si el tercer set no se ha jugado aparecerá como 0-0.
- **errores no forzados del primer jugador**: errores no forzados del jugador 1, de tipo int.
- **errores no forzados del segundo jugador**: errores no forzados del jugador 2, de tipo int.

Así, la primera línea de los datos mostrada arriba indica que en el partido disputado el 13/12/2014 entre Ugo Humbert y Pedro Martínez, el primer set lo ganó Martínez por 7 juegos a 6; el segundo set lo ganó Humbert por 6 a 2, y entonces se disputó el tercer set que ganó Martínez por 6 a 3, ganando el partido.  Humbert cometió 8 errores no forzados y 10 Martínez, y el partido se disputó en una superficie de tierra.  En la segunda línea, se muestra que en el partido disputado el 9/7/2020 entre Adrian Mannarino y Botic Van de Zandschulp, Botic ganó los dos primeros sets por 6 a 1, y por tanto, no se disputó el tercer set lo que se indica por “0-0”.  

Para almacenar los datos de un partido se usarán **obligatoriamente** las siguientes namedtuple, que representan los datos un set o parcial y de un partido, respectivamente:

```python
Parcial = NamedTuple('Parcial', 
                [('juegos_j1',int),
                 ('juegos_j2',int)])
PartidoTenis = NamedTuple('PartidoTenis', 
                [('fecha',datetime.date), 
                 ('jugador1',str), 
                 ('jugador2',str), 
                 ('superficie',str), 
                 ('resultado', List[Parcial]), 
                 ('errores_nf1',int), 
                 ('errores_nf2',int)])

```
Cree un módulo **tenis.py** e implemente en él las funciones que se piden. Puede definir funciones auxiliares cuando lo considere necesario:

1. **lee\_partidos\_tenis**: lee un fichero de entrada en formato CSV codificado en UTF-8 y devuelve una lista de tuplas de tipo PartidoTenis conteniendo todos los datos almacenados en el fichero. Le puede ser de ayuda la función ```datetime.strptime(cadena, '%d/%m/%Y')```  para el parseo de fechas. Para implementar esta función defina la siguiente función auxiliar:
   
    a. **parsea\_set**: Toma una cadena con el resultado de un set o parcial y devuelve una tupla de tipo Parcial que representa ese set. La cadena de entrada se espera que tenga los juegos del set del primer jugador, seguido de un guión y los juegos del set del segundo jugador, es decir, int-int. 

1. **partidos\_menos\_errores**: recibe una lista de tipo PartidoTenis y devuelve el partido con mayor némero de errores no forzados entre los dos jugadores.

1. **jugador\_mas\_partidos**: recibe una lista de tipo PartidoTenis y devuelve una tupla con el nombre del jugador que más partidos ha jugado y el némero de partidos. 

1. **tenista\_mas\_victorias**: recibe una lista de tuplas de tipo PartidoTenis, y dos fechas, **ambas de tipo date**, y con valor por defecto None. Devuelve el nombre del tenista que ha tenido más victorias en los partidos jugados entre las fechas (ambas inclusive). Si la primera fecha es None, la función  devuelve el tenista con más victorias hasta esa fecha (inclusive). Si la segunda fecha es None, la función devuelve el tenista con más victorias desde esa fecha (inclusive). Finalmente, si las dos fechas son None, la función devuelve el tenista con más victorias de toda la lista, independientemente de la fecha. Para implementar esta función defina la siguiente función auxiliar:
   a. **ganador**:** recibe una tupla de tipo PartidoTenis y devuelve el nombre del jugador que ganó ese partido. 

1. **media\_errores\_por\_jugador**: recibe una lista de tuplas de tipo PartidoTenis y devuelve una lista de tuplas ordenadas con el nombre de cada jugador y su media de errores no forzados. La lista estará ordenada por la media de errores de menor a mayor.

1. **jugadores\_mayor\_porcentaje\_victorias**: recibe una lista de tuplas de tipo PartidoTenis y devuelve una lista de tuplas con el nombre de cada jugador y el porcentaje de victorias. La lista estará ordenada por el porcentaje de victorias de mayor a menor.

1. **n\_tenistas\_con\_mas\_errores**: recibe una lista de tuplas de tipo PartidoTenis y un némero n, con valor por defecto None, y devuelve una lista con los nombres de los n tenistas que han acumulado más errores no forzados en el total de partidos que han jugado. Si n es None, entonces devuelve todos los tenistas de la lista de tuplas ordenados de mayor a menor némero de errores no forzados. (2 puntos)

1. **fechas\_ordenadas\_por\_jugador**: recibe una lista de tuplas de tipo PartidoTenis y devuelve un diccionario en el que a cada jugador le hace corresponder una lista ordenada con las fechas de sus partidos.

1. **num\_partidos\_nombre**: recibe el nombre de un tenista y devuelve un diccionario en el que las claves son las superficies y los valores una tupla con el némero de partidos jugados y ganados por el tenista en la superficie dada como clave.

1. **num\_tenistas\_distintos\_por\_superficie**: recibe una lista de tuplas de tipo PartidoTenis, y devuelve un diccionario tal que a cada superficie (clave) le hace corresponder el némero de jugadores distintos que han jugado partidos en ese tipo de superficie. (1,5 puntos) 

1. **superficie\_con\_mas\_tenistas\_distintos**: recibe una lista de tuplas de tipo PartidoTenies y devuelve una tupla con la superficie en la que juegan un mayor némero de jugadores distintos, y el némero de jugadores que han jugado en esa superficie.

1. **mas\_errores\_por\_jugador**: recibe una lista de tuplas de tipo PartidoTenis y devuelve un diccionario en el que a cada jugador y le hace corresponder el partido en el que ha cometido mayor némero de errores no forzados.

1. **partido\_mas\_errores\_por\_mes**: recibe una lista de tuplas de tipo PartidoTenis, y una lista de cadenas con tipos de superficie, que toma como valor por defecto None, y devuelve un diccionario que asocia a cada mes, una tupla (fecha del partido, jugador1, jugador2) que representa al partido de ese mes jugado en una de las superficies de la lista dada como parámetro en el que se han cometido más errores no forzados, teniendo en cuenta los errores de ambos jugadores. Si la lista de superficies dada como parámetro tiene como valor None, entonces se tendrán en cuenta todas las superficies para generar el diccionario resultante. (2 puntos).

1. **n\_partidos\_mas\_errores\_por\_jugador**: recibe una lista de tuplas de tipo  PartidoTenis y un valor entero n y devuelve un diccionario en el que a cada jugador le hace corresponder una lista con los n partidos en los que ha cometido más errores no forzados.

1. **mayor_numero_dias_sin_jugar**: recibe una lista de partidos y un jugador y devuelve el máximo némero de días sin jugar del jugador dado. Si el jugador solo ha disputado un partido devolverá None.

1. Cree un módulo de **tenis\_test.py** y defina una función de test para cada función solicitada. Se recomienda el uso de parámetros en las funciones de test para reutilizar código. (1 punto)

 
#### Pruebas de las funciones.

A continuación, se muestran el resultado de ejecutar funciones de prueba para cada una de estas funciones. 
```
EJERCICIO  1==================================================
Test de 'lee_partidos_tenis'
Numero total de partidos leidos: 201
Mostrando los tres primeros registros leídos:

1-PartidoTenis(fecha=datetime.date(2011, 11, 7), jugador1='Sebastian Korda', jugador2='Ben Shelton', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=3, juegos_j2=6)], errores_nf1=8, errores_nf2=6)
2-PartidoTenis(fecha=datetime.date(2019, 3, 27), jugador1='Benjamin Bonzi', jugador2='Sebastian Baez', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=8, errores_nf2=10)
3-PartidoTenis(fecha=datetime.date(2016, 1, 17), jugador1='John Isner', jugador2="Christopher O'Connell", superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=13)
EJERCICIO  2==================================================
Test de 'partido_menos_errores'
El partido con menos errores es PartidoTenis(fecha=datetime.date(2015, 5, 3), jugador1='Novak Djokovic', jugador2='Casper Ruud', superficie='Dura', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=0, errores_nf2=1)
EJERCICIO  3==================================================
Test de 'jugador_mas_partidos'
El jugador que ha jugado más partidos es Novak Djokovic, con un total de 26 partidos
EJERCICIO  4==================================================
Test de 'tenista_mas_victorias' fecha1=None, fecha2=None
El tenista con más victorias entre las fechas None y None es ('Casper Ruud', 13)
Test de 'tenista_mas_victorias' fecha1=None, fecha2=2020-01-01
El tenista con más victorias entre las fechas None y 2020-01-01 es ('Casper Ruud', 12)
Test de 'tenista_mas_victorias' fecha1=2020-01-01, fecha2=None
El tenista con más victorias entre las fechas 2020-01-01 y None es ('Jaume Munar', 3)
Test de 'tenista_mas_victorias' fecha1=2013-01-01, fecha2=2020-01-01
El tenista con más victorias entre las fechas 2013-01-01 y 2020-01-01 es ('Dominic Thiem', 10)
EJERCICIO  5==================================================
Test de 'media_errores_por_jugador'
La media de errores por jugador, de menos a más errores es
1-('Arthur Rinderknech', 4.5)
2-('Gregoire Barrere', 5.0)
3-('Kamil Majchrzak', 5.0)
4-('Holger Rune', 5.5)
5-('Roberto Carballés Baena', 5.8)
6-('Hubert Hurkacz', 6.0)
7-('Lorenzo Sonego', 6.0)
8-('Mikael Ymer', 6.0)
9-('Emil Ruusuvuori', 6.333333333333333)
10-('Nick Kyrgios', 6.666666666666667)
11-('Federico Coria', 7.0)
12-('Alejandro Davidovich Fokina', 7.0)
13-('Nikoloz Basilashvili', 7.333333333333333)
14-('Tommy Paul', 7.5)
15-('Taylor Fritz', 7.5)
16-('Daniel Altmaier', 7.666666666666667)
17-('Vasek Pospisil', 7.666666666666667)
18-('Daniil Medvedev', 7.857142857142857)
19-('Taro Daniel', 8.0)
20-('Jannik Sinner', 8.0)
21-('Quentin Halys', 8.25)
22-('Dominic Thiem', 8.5625)
23-('Ugo Humbert', 8.666666666666666)
24-('Alex de Mi±aur', 8.666666666666666)
25-('Stefanos Tsitsipas', 8.88888888888889)
26-('Sebastian Korda', 9.0)
27-('Adrian Mannarino', 9.0)
28-('Jaume Munar', 9.0)
29-('Soon Woo Kwon', 9.0)
30-('David Goffin', 9.0)
31-('Alex Molcan', 9.0)
32-('Daniel Elahi Galán', 9.0)
33-('Borna Coric', 9.333333333333334)
34-('Constant Lestienne', 9.5)
35-('Nuno Borges', 10.0)
36-('Alexander Bublik', 10.0)
37-('Gael Monfils', 10.0)
38-('Maxime Cressy', 10.0)
39-('Jiri Lehecka', 10.0)
40-('Tomas Machac', 10.0)
41-('Cristian Garín', 10.2)
42-('Alexander Zverev', 10.23076923076923)
43-('Jack Draper', 10.333333333333334)
44-('Albert Ramos Vi±olas', 10.5)
45-('Yoshihito Nishioka', 10.5)
46-('Andrey Rublev', 10.61111111111111)
47-('Felix Auger-Aliassime', 10.666666666666666)
48-('Casper Ruud', 10.736842105263158)
49-('Tomas Martin Etcheverry', 10.75)
50-('Miomir Kecmanovic', 11.0)
51-('Richard Gasquet', 11.0)
52-('Aslan Karatsev', 11.0)
53-('J.J. Wolf', 11.0)
54-('Marin Cilic', 11.0)
55-('Matteo Berrettini', 11.0)
56-('Daniel Evans', 11.0)
57-('Pedro Cachin', 11.0)
58-('Frances Tiafoe', 11.0)
59-('Marc-Andrea Huesler', 11.0)
60-('Carlos Alcaraz', 11.117647058823529)
61-('Roberto Bautista Agut', 11.176470588235293)
62-('Novak Djokovic', 11.192307692307692)
63-('Ben Shelton', 11.2)
64-('John Isner', 11.2)
65-('Roman Safiullin', 11.285714285714286)
66-("Christopher O'Connell", 11.333333333333334)
67-('Lorenzo Musetti', 11.333333333333334)
68-('Pavel Kotov', 11.333333333333334)
69-('Bernabé Zapata Miralles', 11.5)
70-('Benjamin Bonzi', 12.0)
71-('Marton Fucsovics', 12.0)
72-('Denis Shapovalov', 12.0)
73-('Karen Khachanov', 12.0)
74-('Oscar Otte', 12.0)
75-('Diego Schwartzman', 12.166666666666666)
76-('Rafael Nadal', 12.3125)
77-('Pedro Martínez', 12.5)
78-('Jenson Brooksby', 12.5)
79-('Botic Van de Zandschulp', 12.666666666666666)
80-('Fabio Fognini', 13.0)
81-('Roger Federer', 13.142857142857142)
82-('Sebastian Baez', 13.5)
83-('Jordan Thompson', 14.0)
84-('Grigor Dimitrov', 14.0)
85-('Laslo Djere', 14.0)
86-('Thanasi Kokkinakis', 14.0)
87-('Cameron Norrie', 15.0)
88-('Pablo Carre±o Busta', 15.0)
89-('Filip Krajinovic', 16.0)
90-('Brandon Nakashima', 16.0)
EJERCICIO  6==================================================
Test de 'jugadores_mayor_porcentaje_victorias'
El porcentaje de victorias de cada jugador (ordendo de mayor a menor) es
1-('Fabio Fognini', 1.0)
2-('Aslan Karatsev', 1.0)
3-('Alexander Bublik', 1.0)
4-('Yoshihito Nishioka', 1.0)
5-('Gael Monfils', 1.0)
6-('Maxime Cressy', 1.0)
7-('Marin Cilic', 1.0)
8-('Vasek Pospisil', 1.0)
9-('Daniel Elahi Galán', 1.0)
10-('Jiri Lehecka', 1.0)
11-('Daniel Evans', 1.0)
12-('Brandon Nakashima', 1.0)
13-('Pablo Carre±o Busta', 1.0)
14-('Frances Tiafoe', 1.0)
15-('Marc-Andrea Huesler', 1.0)
16-('Jaume Munar', 0.75)
17-('Roman Safiullin', 0.7142857142857143)
18-('Roger Federer', 0.7142857142857143)
19-('Dominic Thiem', 0.6875)
20-('Casper Ruud', 0.6842105263157895)
21-('Daniel Altmaier', 0.6666666666666666)
22-('Jack Draper', 0.6666666666666666)
23-('Botic Van de Zandschulp', 0.6666666666666666)
24-('Richard Gasquet', 0.6666666666666666)
25-('Alex de Mi±aur', 0.6666666666666666)
26-('Pavel Kotov', 0.6666666666666666)
27-('Borna Coric', 0.6666666666666666)
28-('Roberto Bautista Agut', 0.6470588235294118)
29-('Andrey Rublev', 0.6111111111111112)
30-('Ben Shelton', 0.6)
31-('Roberto Carballés Baena', 0.6)
32-('Sebastian Korda', 0.5)
33-('Benjamin Bonzi', 0.5)
34-('Sebastian Baez', 0.5)
35-('Marton Fucsovics', 0.5)
36-('Pedro Martínez', 0.5)
37-('Quentin Halys', 0.5)
38-('Tommy Paul', 0.5)
39-('Lorenzo Sonego', 0.5)
40-('Tomas Martin Etcheverry', 0.5)
41-('Arthur Rinderknech', 0.5)
42-('Jenson Brooksby', 0.5)
43-('Filip Krajinovic', 0.5)
44-('Constant Lestienne', 0.5)
45-('Federico Coria', 0.5)
46-('Bernabé Zapata Miralles', 0.5)
47-('Laslo Djere', 0.5)
48-('Taro Daniel', 0.5)
49-('Holger Rune', 0.5)
50-('Thanasi Kokkinakis', 0.5)
51-('Taylor Fritz', 0.5)
52-('Matteo Berrettini', 0.5)
53-('Pedro Cachin', 0.5)
54-('Alexander Zverev', 0.46153846153846156)
55-('Rafael Nadal', 0.4375)
56-('Daniil Medvedev', 0.42857142857142855)
57-('Carlos Alcaraz', 0.4117647058823529)
58-('John Isner', 0.4)
59-('Cristian Garín', 0.4)
60-('Felix Auger-Aliassime', 0.4)
61-('Diego Schwartzman', 0.3888888888888889)
62-('Stefanos Tsitsipas', 0.3888888888888889)
63-('Novak Djokovic', 0.38461538461538464)
64-("Christopher O'Connell", 0.3333333333333333)
65-('Nikoloz Basilashvili', 0.3333333333333333)
66-('Jordan Thompson', 0.3333333333333333)
67-('Lorenzo Musetti', 0.3333333333333333)
68-('Mikael Ymer', 0.3333333333333333)
69-('David Goffin', 0.3333333333333333)
70-('Alex Molcan', 0.3333333333333333)
71-('Albert Ramos Vi±olas', 0.25)
72-('Hubert Hurkacz', 0.0)
73-('Miomir Kecmanovic', 0.0)
74-('Gregoire Barrere', 0.0)
75-('Ugo Humbert', 0.0)
76-('Adrian Mannarino', 0.0)
77-('Emil Ruusuvuori', 0.0)
78-('Grigor Dimitrov', 0.0)
79-('Nuno Borges', 0.0)
80-('Soon Woo Kwon', 0.0)
81-('J.J. Wolf', 0.0)
82-('Alejandro Davidovich Fokina', 0.0)
83-('Denis Shapovalov', 0.0)
84-('Karen Khachanov', 0.0)
85-('Nick Kyrgios', 0.0)
86-('Tomas Machac', 0.0)
87-('Cameron Norrie', 0.0)
88-('Kamil Majchrzak', 0.0)
89-('Oscar Otte', 0.0)
90-('Jannik Sinner', 0.0)
EJERCICIO  7==================================================
Test de 'n_tenistas_con_mas_errores' n=5
Los 5 tenistas con mas errores son:
1-('Novak Djokovic', 291)
2-('Diego Schwartzman', 219)
3-('Casper Ruud', 204)
4-('Rafael Nadal', 197)
5-('Andrey Rublev', 191)
Test de 'n_tenistas_con_mas_errores' n=None
Los None tenistas con mas errores son:
1-('Novak Djokovic', 291)
2-('Diego Schwartzman', 219)
3-('Casper Ruud', 204)
4-('Rafael Nadal', 197)
5-('Andrey Rublev', 191)
6-('Roberto Bautista Agut', 190)
7-('Carlos Alcaraz', 189)
8-('Roger Federer', 184)
9-('Felix Auger-Aliassime', 160)
10-('Stefanos Tsitsipas', 160)
11-('Dominic Thiem', 137)
12-('Alexander Zverev', 133)
13-('Daniil Medvedev', 110)
14-('Roman Safiullin', 79)
15-('Ben Shelton', 56)
16-('John Isner', 56)
17-('Cristian Garín', 51)
18-('Jenson Brooksby', 50)
19-('Tomas Martin Etcheverry', 43)
20-('Jordan Thompson', 42)
21-('Albert Ramos Vi±olas', 42)
22-('Gael Monfils', 40)
23-('Botic Van de Zandschulp', 38)
24-('Jaume Munar', 36)
25-("Christopher O'Connell", 34)
26-('Lorenzo Musetti', 34)
27-('Pavel Kotov', 34)
28-('Quentin Halys', 33)
29-('Richard Gasquet', 33)
30-('Filip Krajinovic', 32)
31-('Jack Draper', 31)
32-('Roberto Carballés Baena', 29)
33-('Federico Coria', 28)
34-('Laslo Djere', 28)
35-('Thanasi Kokkinakis', 28)
36-('Borna Coric', 28)
37-('Sebastian Baez', 27)
38-('Adrian Mannarino', 27)
39-('David Goffin', 27)
40-('Alex Molcan', 27)
41-('Ugo Humbert', 26)
42-('Alex de Mi±aur', 26)
43-('Pedro Martínez', 25)
44-('Benjamin Bonzi', 24)
45-('Marton Fucsovics', 24)
46-('Daniel Altmaier', 23)
47-('Bernabé Zapata Miralles', 23)
48-('Vasek Pospisil', 23)
49-('Nikoloz Basilashvili', 22)
50-('Matteo Berrettini', 22)
51-('Pedro Cachin', 22)
52-('Yoshihito Nishioka', 21)
53-('Nuno Borges', 20)
54-('Alexander Bublik', 20)
55-('Nick Kyrgios', 20)
56-('Jiri Lehecka', 20)
57-('Emil Ruusuvuori', 19)
58-('Constant Lestienne', 19)
59-('Sebastian Korda', 18)
60-('Mikael Ymer', 18)
61-('Soon Woo Kwon', 18)
62-('Taro Daniel', 16)
63-('Brandon Nakashima', 16)
64-('Tommy Paul', 15)
65-('Taylor Fritz', 15)
66-('Cameron Norrie', 15)
67-('Pablo Carre±o Busta', 15)
68-('Grigor Dimitrov', 14)
69-('Fabio Fognini', 13)
70-('Lorenzo Sonego', 12)
71-('Denis Shapovalov', 12)
72-('Karen Khachanov', 12)
73-('Oscar Otte', 12)
74-('Miomir Kecmanovic', 11)
75-('Aslan Karatsev', 11)
76-('J.J. Wolf', 11)
77-('Holger Rune', 11)
78-('Marin Cilic', 11)
79-('Daniel Evans', 11)
80-('Frances Tiafoe', 11)
81-('Marc-Andrea Huesler', 11)
82-('Maxime Cressy', 10)
83-('Tomas Machac', 10)
84-('Arthur Rinderknech', 9)
85-('Daniel Elahi Galán', 9)
86-('Jannik Sinner', 8)
87-('Alejandro Davidovich Fokina', 7)
88-('Hubert Hurkacz', 6)
89-('Gregoire Barrere', 5)
90-('Kamil Majchrzak', 5)
EJERCICIO  8==================================================
Test de 'fechas_por_jugador'
Las fechas de cada partido por jugador son
Sebastian Korda --> [datetime.date(2011, 11, 7), datetime.date(2011, 11, 10)]
Ben Shelton --> [datetime.date(2011, 11, 7), datetime.date(2013, 8, 12), datetime.date(2018, 7, 20), datetime.date(2014, 9, 20), datetime.date(2018, 3, 23)]
Benjamin Bonzi --> [datetime.date(2019, 3, 27), datetime.date(2016, 1, 15)]
Sebastian Baez --> [datetime.date(2019, 3, 27), datetime.date(2010, 7, 1)]
John Isner --> [datetime.date(2016, 1, 17), datetime.date(2011, 11, 10), datetime.date(2012, 2, 24), datetime.date(2014, 9, 20), datetime.date(2015, 10, 25)]
Christopher O'Connell --> [datetime.date(2016, 1, 17), datetime.date(2015, 4, 28), datetime.date(2019, 8, 16)]
Daniel Altmaier --> [datetime.date(2019, 3, 26), datetime.date(2015, 10, 27), datetime.date(2013, 1, 12)]
Hubert Hurkacz --> [datetime.date(2019, 3, 26)]
Jack Draper --> [datetime.date(2017, 11, 28), datetime.date(2014, 8, 13), datetime.date(2011, 2, 13)]
Nikoloz Basilashvili --> [datetime.date(2017, 11, 28), datetime.date(2019, 7, 25), datetime.date(2017, 7, 10)]
Miomir Kecmanovic --> [datetime.date(2017, 8, 10)]
Roman Safiullin --> [datetime.date(2017, 8, 10), datetime.date(2019, 6, 22), datetime.date(2013, 4, 23), datetime.date(2018, 7, 18), datetime.date(2010, 12, 12), datetime.date(2010, 10, 14), datetime.date(2010, 4, 24)]
Marton Fucsovics --> [datetime.date(2019, 8, 13), datetime.date(2011, 2, 13)]
Gregoire Barrere --> [datetime.date(2019, 8, 13)]
Ugo Humbert --> [datetime.date(2014, 12, 13), datetime.date(2018, 1, 4), datetime.date(2012, 7, 19)]
Pedro Martínez --> [datetime.date(2014, 12, 13), datetime.date(2012, 2, 24)]
Adrian Mannarino --> [datetime.date(2020, 7, 9), datetime.date(2019, 7, 25), datetime.date(2011, 6, 3)]
Botic Van de Zandschulp --> [datetime.date(2020, 7, 9), datetime.date(2014, 7, 6), datetime.date(2020, 4, 17)]
Jordan Thompson --> [datetime.date(2013, 10, 21), datetime.date(2013, 6, 23), datetime.date(2020, 9, 4)]
Quentin Halys --> [datetime.date(2013, 10, 21), datetime.date(2014, 8, 13), datetime.date(2017, 3, 16), datetime.date(2019, 3, 2)]
Tommy Paul --> [datetime.date(2017, 8, 26), datetime.date(2013, 12, 19)]
Novak Djokovic --> [datetime.date(2017, 8, 26), datetime.date(2012, 2, 13), datetime.date(2010, 5, 27), datetime.date(2011, 4, 3), datetime.date(2010, 6, 27), datetime.date(2015, 3, 7), datetime.date(2016, 1, 3), datetime.date(2016, 10, 13), datetime.date(2015, 11, 30), datetime.date(2017, 6, 16), datetime.date(2016, 1, 26), datetime.date(2015, 4, 11), datetime.date(2013, 12, 22), datetime.date(2011, 1, 9), datetime.date(2019, 10, 24), datetime.date(2018, 6, 3), datetime.date(2020, 12, 16), datetime.date(2012, 11, 20), datetime.date(2019, 1, 15), datetime.date(2020, 10, 24), datetime.date(2015, 5, 3), datetime.date(2012, 5, 30), datetime.date(2013, 2, 1), datetime.date(2010, 10, 26), datetime.date(2016, 3, 5), datetime.date(2010, 9, 28)]
Lorenzo Sonego --> [datetime.date(2019, 6, 22), datetime.date(2020, 2, 21)]
Carlos Alcaraz --> [datetime.date(2013, 4, 23), datetime.date(2020, 12, 2), datetime.date(2012, 5, 7), datetime.date(2017, 12, 21), datetime.date(2011, 4, 3), datetime.date(2016, 12, 4), datetime.date(2018, 5, 4), datetime.date(2016, 8, 30), datetime.date(2020, 7, 11), datetime.date(2010, 9, 20), datetime.date(2015, 6, 13), datetime.date(2013, 12, 22), datetime.date(2013, 7, 15), datetime.date(2010, 11, 7), datetime.date(2013, 6, 26), datetime.date(2017, 12, 5), datetime.date(2015, 6, 4)]
Tomas Martin Etcheverry --> [datetime.date(2010, 6, 19), datetime.date(2020, 1, 24), datetime.date(2020, 3, 19), datetime.date(2017, 7, 10)]
Cristian Garín --> [datetime.date(2010, 6, 19), datetime.date(2016, 9, 9), datetime.date(2020, 3, 19), datetime.date(2016, 2, 3), datetime.date(2015, 3, 13)]
Arthur Rinderknech --> [datetime.date(2012, 10, 25), datetime.date(2012, 9, 2)]
Richard Gasquet --> [datetime.date(2012, 10, 25), datetime.date(2016, 11, 21), datetime.date(2012, 10, 24)]
Alex de Mi±aur --> [datetime.date(2016, 9, 9), datetime.date(2012, 10, 14), datetime.date(2013, 1, 8)]
Lorenzo Musetti --> [datetime.date(2018, 7, 18), datetime.date(2013, 8, 12), datetime.date(2012, 4, 20)]
Jenson Brooksby --> [datetime.date(2012, 10, 14), datetime.date(2010, 12, 12), datetime.date(2020, 9, 4), datetime.date(2020, 4, 25)]
Filip Krajinovic --> [datetime.date(2011, 6, 18), datetime.date(2010, 11, 16)]
Diego Schwartzman --> [datetime.date(2011, 6, 18), datetime.date(2016, 11, 21), datetime.date(2016, 1, 15), datetime.date(2018, 2, 3), datetime.date(2017, 11, 7), datetime.date(2019, 1, 26), datetime.date(2018, 3, 28), datetime.date(2020, 10, 4), datetime.date(2013, 2, 9), datetime.date(2013, 7, 15), datetime.date(2013, 11, 29), datetime.date(2018, 5, 23), datetime.date(2013, 6, 26), datetime.date(2014, 11, 20), datetime.date(2017, 12, 27), datetime.date(2018, 5, 1), datetime.date(2012, 3, 10), datetime.date(2017, 1, 29)]
Alexander Zverev --> [datetime.date(2012, 4, 16), datetime.date(2017, 3, 20), datetime.date(2020, 7, 11), datetime.date(2016, 10, 13), datetime.date(2018, 5, 19), datetime.date(2015, 4, 11), datetime.date(2018, 3, 24), datetime.date(2020, 12, 16), datetime.date(2012, 5, 30), datetime.date(2013, 2, 1), datetime.date(2011, 12, 23), datetime.date(2018, 5, 1), datetime.date(2013, 7, 3)]
Emil Ruusuvuori --> [datetime.date(2012, 4, 16), datetime.date(2010, 11, 16), datetime.date(2013, 1, 8)]
Constant Lestienne --> [datetime.date(2012, 2, 26), datetime.date(2014, 4, 15)]
Federico Coria --> [datetime.date(2012, 2, 26), datetime.date(2014, 3, 26), datetime.date(2010, 7, 1), datetime.date(2013, 1, 12)]
Jaume Munar --> [datetime.date(2020, 8, 1), datetime.date(2020, 1, 2), datetime.date(2020, 2, 8), datetime.date(2020, 11, 9)]
Grigor Dimitrov --> [datetime.date(2020, 8, 1)]
Mikael Ymer --> [datetime.date(2014, 4, 1), datetime.date(2014, 4, 1), datetime.date(2020, 4, 25)]
Nuno Borges --> [datetime.date(2012, 3, 28), datetime.date(2020, 9, 9)]
Fabio Fognini --> [datetime.date(2012, 3, 28)]
Daniil Medvedev --> [datetime.date(2011, 9, 23), datetime.date(2018, 5, 4), datetime.date(2016, 9, 22), datetime.date(2014, 10, 28), datetime.date(2016, 1, 3), datetime.date(2018, 8, 23), datetime.date(2017, 9, 6), datetime.date(2017, 2, 16), datetime.date(2017, 6, 14), datetime.date(2017, 12, 27), datetime.date(2010, 8, 28), datetime.date(2013, 7, 29), datetime.date(2010, 11, 26), datetime.date(2019, 6, 11)]
Soon Woo Kwon --> [datetime.date(2011, 9, 23), datetime.date(2020, 6, 16)]
Aslan Karatsev --> [datetime.date(2020, 12, 6)]
Albert Ramos Vi±olas --> [datetime.date(2020, 12, 6), datetime.date(2014, 10, 25), datetime.date(2010, 5, 27), datetime.date(2020, 4, 17)]
J.J. Wolf --> [datetime.date(2012, 12, 9)]
Alexander Bublik --> [datetime.date(2012, 12, 9), datetime.date(2014, 1, 26)]
Bernabé Zapata Miralles --> [datetime.date(2018, 11, 17), datetime.date(2014, 1, 26)]
Alejandro Davidovich Fokina --> [datetime.date(2018, 11, 17)]
Denis Shapovalov --> [datetime.date(2016, 5, 3)]
Yoshihito Nishioka --> [datetime.date(2016, 5, 3), datetime.date(2011, 6, 3)]
Gael Monfils --> [datetime.date(2010, 5, 7), datetime.date(2016, 2, 17), datetime.date(2012, 5, 7), datetime.date(2011, 12, 19)]
Laslo Djere --> [datetime.date(2010, 5, 7), datetime.date(2020, 9, 9)]
David Goffin --> [datetime.date(2012, 12, 11), datetime.date(2010, 5, 27), datetime.date(2015, 3, 13)]
Maxime Cressy --> [datetime.date(2012, 12, 11)]
Taro Daniel --> [datetime.date(2015, 4, 28), datetime.date(2020, 2, 21)]
Casper Ruud --> [datetime.date(2012, 9, 2), datetime.date(2013, 3, 24), datetime.date(2020, 10, 23), datetime.date(2019, 1, 26), datetime.date(2019, 5, 22), datetime.date(2018, 1, 29), datetime.date(2016, 8, 14), datetime.date(2010, 10, 15), datetime.date(2017, 3, 20), datetime.date(2015, 11, 30), datetime.date(2018, 8, 23), datetime.date(2010, 11, 7), datetime.date(2012, 11, 20), datetime.date(2015, 5, 3), datetime.date(2011, 10, 8), datetime.date(2017, 12, 5), datetime.date(2013, 7, 29), datetime.date(2017, 7, 29), datetime.date(2015, 1, 28)]
Karen Khachanov --> [datetime.date(2020, 1, 2)]
Holger Rune --> [datetime.date(2019, 8, 16), datetime.date(2013, 12, 19)]
Pavel Kotov --> [datetime.date(2013, 12, 25), datetime.date(2012, 7, 21), datetime.date(2013, 3, 24)]
Roberto Carballés Baena --> [datetime.date(2013, 12, 25), datetime.date(2014, 7, 6), datetime.date(2017, 10, 12), datetime.date(2016, 2, 3), datetime.date(2014, 4, 15)]
Thanasi Kokkinakis --> [datetime.date(2013, 6, 23), datetime.date(2010, 10, 14)]
Marin Cilic --> [datetime.date(2018, 1, 4)]
Taylor Fritz --> [datetime.date(2020, 12, 2), datetime.date(2017, 4, 20)]
Andrey Rublev --> [datetime.date(2020, 2, 8), datetime.date(2017, 3, 16), datetime.date(2019, 3, 2), datetime.date(2011, 1, 12), datetime.date(2014, 1, 6), datetime.date(2018, 5, 19), datetime.date(2015, 6, 13), datetime.date(2016, 1, 26), datetime.date(2020, 7, 17), datetime.date(2013, 11, 29), datetime.date(2017, 6, 14), datetime.date(2011, 10, 8), datetime.date(2010, 8, 28), datetime.date(2011, 12, 23), datetime.date(2010, 11, 22), datetime.date(2017, 2, 28), datetime.date(2010, 9, 24), datetime.date(2015, 6, 4)]
Felix Auger-Aliassime --> [datetime.date(2014, 10, 25), datetime.date(2017, 11, 1), datetime.date(2015, 2, 15), datetime.date(2016, 2, 9), datetime.date(2020, 5, 29), datetime.date(2012, 1, 8), datetime.date(2016, 6, 7), datetime.date(2016, 11, 20), datetime.date(2013, 2, 9), datetime.date(2017, 2, 16), datetime.date(2020, 7, 17), datetime.date(2011, 11, 4), datetime.date(2016, 9, 29), datetime.date(2014, 7, 30), datetime.date(2015, 9, 17)]
Vasek Pospisil --> [datetime.date(2018, 7, 20), datetime.date(2020, 1, 24), datetime.date(2017, 4, 20)]
Alex Molcan --> [datetime.date(2012, 7, 21), datetime.date(2014, 7, 10), datetime.date(2010, 9, 1)]
Nick Kyrgios --> [datetime.date(2012, 10, 24), datetime.date(2014, 3, 26), datetime.date(2018, 3, 23)]
Daniel Elahi Galán --> [datetime.date(2017, 10, 12)]
Borna Coric --> [datetime.date(2016, 2, 17), datetime.date(2010, 5, 27), datetime.date(2019, 4, 10)]
Jiri Lehecka --> [datetime.date(2012, 2, 13), datetime.date(2020, 6, 16)]
Stefanos Tsitsipas --> [datetime.date(2020, 11, 9), datetime.date(2020, 10, 23), datetime.date(2017, 11, 7), datetime.date(2014, 10, 28), datetime.date(2020, 10, 4), datetime.date(2011, 12, 4), datetime.date(2010, 9, 20), datetime.date(2018, 9, 23), datetime.date(2016, 11, 20), datetime.date(2018, 3, 24), datetime.date(2019, 10, 24), datetime.date(2013, 2, 9), datetime.date(2012, 12, 18), datetime.date(2016, 6, 22), datetime.date(2017, 7, 29), datetime.date(2014, 10, 10), datetime.date(2015, 1, 28), datetime.date(2013, 7, 3)]
Matteo Berrettini --> [datetime.date(2014, 7, 10), datetime.date(2010, 9, 1)]
Daniel Evans --> [datetime.date(2014, 9, 20)]
Brandon Nakashima --> [datetime.date(2016, 8, 9)]
Tomas Machac --> [datetime.date(2016, 8, 9)]
Cameron Norrie --> [datetime.date(2017, 12, 21)]
Kamil Majchrzak --> [datetime.date(2019, 4, 10)]
Pedro Cachin --> [datetime.date(2012, 4, 20), datetime.date(2011, 12, 19)]
Pablo Carre±o Busta --> [datetime.date(2015, 10, 27)]
Frances Tiafoe --> [datetime.date(2014, 9, 20)]
Oscar Otte --> [datetime.date(2010, 4, 24)]
Marc-Andrea Huesler --> [datetime.date(2012, 7, 19)]
Jannik Sinner --> [datetime.date(2015, 10, 25)]
Dominic Thiem --> [datetime.date(2014, 8, 19), datetime.date(2014, 8, 19), datetime.date(2015, 2, 15), datetime.date(2016, 8, 30), datetime.date(2018, 3, 28), datetime.date(2012, 4, 20), datetime.date(2018, 9, 23), datetime.date(2011, 1, 9), datetime.date(2013, 2, 9), datetime.date(2018, 5, 23), datetime.date(2010, 11, 22), datetime.date(2017, 2, 28), datetime.date(2016, 6, 22), datetime.date(2010, 11, 26), datetime.date(2019, 6, 11), datetime.date(2015, 8, 8)]
Rafael Nadal --> [datetime.date(2014, 8, 19), datetime.date(2014, 8, 19), datetime.date(2011, 3, 13), datetime.date(2010, 6, 27), datetime.date(2016, 8, 14), datetime.date(2020, 5, 29), datetime.date(2012, 12, 18), datetime.date(2019, 1, 15), datetime.date(2011, 11, 4), datetime.date(2016, 9, 29), datetime.date(2010, 10, 26), datetime.date(2015, 9, 17), datetime.date(2016, 3, 5), datetime.date(2018, 2, 11), datetime.date(2016, 1, 17), datetime.date(2015, 8, 8)]
Roger Federer --> [datetime.date(2011, 3, 13), datetime.date(2016, 12, 4), datetime.date(2018, 2, 3), datetime.date(2015, 3, 7), datetime.date(2016, 9, 22), datetime.date(2019, 5, 22), datetime.date(2014, 1, 6), datetime.date(2012, 4, 20), datetime.date(2012, 1, 8), datetime.date(2017, 9, 6), datetime.date(2012, 3, 10), datetime.date(2010, 9, 24), datetime.date(2010, 9, 28), datetime.date(2014, 10, 10)]
Roberto Bautista Agut --> [datetime.date(2017, 11, 1), datetime.date(2016, 2, 9), datetime.date(2018, 1, 29), datetime.date(2014, 10, 28), datetime.date(2014, 10, 28), datetime.date(2010, 10, 15), datetime.date(2011, 1, 12), datetime.date(2011, 12, 4), datetime.date(2016, 6, 7), datetime.date(2017, 6, 16), datetime.date(2018, 6, 3), datetime.date(2014, 11, 20), datetime.date(2020, 10, 24), datetime.date(2014, 7, 30), datetime.date(2018, 2, 11), datetime.date(2016, 1, 17), datetime.date(2017, 1, 29)]
EJERCICIO  9==================================================
Test de 'num_partidos_nombre' nombre:Rafael Nadal
Los partidos jugados y ganados por superficie de Rafael Nadal son
Tierra --> (7, 3)
Dura --> (5, 0)
Sintética --> (2, 2)
Hierba --> (2, 2)
Test de 'num_partidos_nombre' nombre:Carlos Alcaraz
Los partidos jugados y ganados por superficie de Carlos Alcaraz son
Hierba --> (2, 2)
Tierra --> (8, 3)
Dura --> (5, 2)
Sintética --> (2, 0)
EJERCICIO 10==================================================
Test de 'num_tenistas_distintos_por_superficie'
El número de tenistas distintos segun cada superficie es
Hierba --> 56
Tierra --> 63
Dura --> 51
Sintética --> 12
EJERCICIO 11==================================================
Test de 'mas_errores_por_jugador'
El partido con más errores por cada jugador es
Sebastian Korda --> PartidoTenis(fecha=datetime.date(2011, 11, 10), jugador1='John Isner', jugador2='Sebastian Korda', superficie='Hierba', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=10)
Ben Shelton --> PartidoTenis(fecha=datetime.date(2013, 8, 12), jugador1='Lorenzo Musetti', jugador2='Ben Shelton', superficie='Tierra', resultado=[Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=19)
Benjamin Bonzi --> PartidoTenis(fecha=datetime.date(2016, 1, 15), jugador1='Benjamin Bonzi', jugador2='Diego Schwartzman', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=15)
Sebastian Baez --> PartidoTenis(fecha=datetime.date(2010, 7, 1), jugador1='Federico Coria', jugador2='Sebastian Baez', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=5, errores_nf2=17)
John Isner --> PartidoTenis(fecha=datetime.date(2016, 1, 17), jugador1='John Isner', jugador2="Christopher O'Connell", superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=13)
Christopher O'Connell --> PartidoTenis(fecha=datetime.date(2016, 1, 17), jugador1='John Isner', jugador2="Christopher O'Connell", superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=13)
Daniel Altmaier --> PartidoTenis(fecha=datetime.date(2015, 10, 27), jugador1='Daniel Altmaier', jugador2='Pablo Carre±o Busta', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=15)
Hubert Hurkacz --> PartidoTenis(fecha=datetime.date(2019, 3, 26), jugador1='Daniel Altmaier', jugador2='Hubert Hurkacz', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=6, errores_nf2=6)
Jack Draper --> PartidoTenis(fecha=datetime.date(2011, 2, 13), jugador1='Marton Fucsovics', jugador2='Jack Draper', superficie='Dura', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=12)
Nikoloz Basilashvili --> PartidoTenis(fecha=datetime.date(2017, 11, 28), jugador1='Jack Draper', jugador2='Nikoloz Basilashvili', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=8, errores_nf2=10)
Miomir Kecmanovic --> PartidoTenis(fecha=datetime.date(2017, 8, 10), jugador1='Miomir Kecmanovic', jugador2='Roman Safiullin', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=12)
Roman Safiullin --> PartidoTenis(fecha=datetime.date(2010, 12, 12), jugador1='Jenson Brooksby', jugador2='Roman Safiullin', superficie='Tierra', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=20)
Marton Fucsovics --> PartidoTenis(fecha=datetime.date(2019, 8, 13), jugador1='Marton Fucsovics', jugador2='Gregoire Barrere', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=13, errores_nf2=5)
Gregoire Barrere --> PartidoTenis(fecha=datetime.date(2019, 8, 13), jugador1='Marton Fucsovics', jugador2='Gregoire Barrere', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=13, errores_nf2=5)
Ugo Humbert --> PartidoTenis(fecha=datetime.date(2018, 1, 4), jugador1='Ugo Humbert', jugador2='Marin Cilic', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=11)
Pedro Martínez --> PartidoTenis(fecha=datetime.date(2012, 2, 24), jugador1='Pedro Martínez', jugador2='John Isner', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=10)
Adrian Mannarino --> PartidoTenis(fecha=datetime.date(2019, 7, 25), jugador1='Nikoloz Basilashvili', jugador2='Adrian Mannarino', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=17)
Botic Van de Zandschulp --> PartidoTenis(fecha=datetime.date(2014, 7, 6), jugador1='Botic Van de Zandschulp', jugador2='Roberto Carballés Baena', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=18, errores_nf2=8)
Jordan Thompson --> PartidoTenis(fecha=datetime.date(2013, 10, 21), jugador1='Jordan Thompson', jugador2='Quentin Halys', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=3, juegos_j2=6)], errores_nf1=19, errores_nf2=1)
Quentin Halys --> PartidoTenis(fecha=datetime.date(2019, 3, 2), jugador1='Andrey Rublev', jugador2='Quentin Halys', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=15, errores_nf2=15)
Tommy Paul --> PartidoTenis(fecha=datetime.date(2017, 8, 26), jugador1='Tommy Paul', jugador2='Novak Djokovic', superficie='Dura', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=22)
Novak Djokovic --> PartidoTenis(fecha=datetime.date(2010, 9, 28), jugador1='Novak Djokovic', jugador2='Roger Federer', superficie='Dura', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=19, errores_nf2=4)
Lorenzo Sonego --> PartidoTenis(fecha=datetime.date(2019, 6, 22), jugador1='Lorenzo Sonego', jugador2='Roman Safiullin', superficie='Tierra', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=6, errores_nf2=7)
Carlos Alcaraz --> PartidoTenis(fecha=datetime.date(2017, 12, 5), jugador1='Carlos Alcaraz', jugador2='Casper Ruud', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=20, errores_nf2=5)
Tomas Martin Etcheverry --> PartidoTenis(fecha=datetime.date(2020, 1, 24), jugador1='Tomas Martin Etcheverry', jugador2='Vasek Pospisil', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=11)
Cristian Garín --> PartidoTenis(fecha=datetime.date(2015, 3, 13), jugador1='David Goffin', jugador2='Cristian Garín', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=11, errores_nf2=9)
Arthur Rinderknech --> PartidoTenis(fecha=datetime.date(2012, 10, 25), jugador1='Arthur Rinderknech', jugador2='Richard Gasquet', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=0)], errores_nf1=8, errores_nf2=7)
Richard Gasquet --> PartidoTenis(fecha=datetime.date(2012, 10, 24), jugador1='Nick Kyrgios', jugador2='Richard Gasquet', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=16)
Alex de Mi±aur --> PartidoTenis(fecha=datetime.date(2013, 1, 8), jugador1='Emil Ruusuvuori', jugador2='Alex de Mi±aur', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=11)
Lorenzo Musetti --> PartidoTenis(fecha=datetime.date(2012, 4, 20), jugador1='Pedro Cachin', jugador2='Lorenzo Musetti', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=8, errores_nf2=10)
Jenson Brooksby --> PartidoTenis(fecha=datetime.date(2010, 12, 12), jugador1='Jenson Brooksby', jugador2='Roman Safiullin', superficie='Tierra', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=20)
Filip Krajinovic --> PartidoTenis(fecha=datetime.date(2011, 6, 18), jugador1='Filip Krajinovic', jugador2='Diego Schwartzman', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=20, errores_nf2=12)
Diego Schwartzman --> PartidoTenis(fecha=datetime.date(2017, 12, 27), jugador1='Diego Schwartzman', jugador2='Daniil Medvedev', superficie='Sintética', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=15)
Alexander Zverev --> PartidoTenis(fecha=datetime.date(2013, 7, 3), jugador1='Stefanos Tsitsipas', jugador2='Alexander Zverev', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=20)
Emil Ruusuvuori --> PartidoTenis(fecha=datetime.date(2010, 11, 16), jugador1='Filip Krajinovic', jugador2='Emil Ruusuvuori', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=8)
Constant Lestienne --> PartidoTenis(fecha=datetime.date(2014, 4, 15), jugador1='Roberto Carballés Baena', jugador2='Constant Lestienne', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=9)
Federico Coria --> PartidoTenis(fecha=datetime.date(2012, 2, 26), jugador1='Constant Lestienne', jugador2='Federico Coria', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=10, errores_nf2=7)
Jaume Munar --> PartidoTenis(fecha=datetime.date(2020, 11, 9), jugador1='Stefanos Tsitsipas', jugador2='Jaume Munar', superficie='Dura', resultado=[Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=3, errores_nf2=10)
Grigor Dimitrov --> PartidoTenis(fecha=datetime.date(2020, 8, 1), jugador1='Jaume Munar', jugador2='Grigor Dimitrov', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=14)
Mikael Ymer --> PartidoTenis(fecha=datetime.date(2020, 4, 25), jugador1='Mikael Ymer', jugador2='Jenson Brooksby', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=10, errores_nf2=15)
Nuno Borges --> PartidoTenis(fecha=datetime.date(2012, 3, 28), jugador1='Nuno Borges', jugador2='Fabio Fognini', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=13)
Fabio Fognini --> PartidoTenis(fecha=datetime.date(2012, 3, 28), jugador1='Nuno Borges', jugador2='Fabio Fognini', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=13)
Daniil Medvedev --> PartidoTenis(fecha=datetime.date(2019, 6, 11), jugador1='Daniil Medvedev', jugador2='Dominic Thiem', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=13, errores_nf2=7)
Soon Woo Kwon --> PartidoTenis(fecha=datetime.date(2020, 6, 16), jugador1='Soon Woo Kwon', jugador2='Jiri Lehecka', superficie='Hierba', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=15)
Aslan Karatsev --> PartidoTenis(fecha=datetime.date(2020, 12, 6), jugador1='Aslan Karatsev', jugador2='Albert Ramos Vi±olas', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=6)
Albert Ramos Vi±olas --> PartidoTenis(fecha=datetime.date(2010, 5, 27), jugador1='Albert Ramos Vi±olas', jugador2='Borna Coric', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=14, errores_nf2=13)
J.J. Wolf --> PartidoTenis(fecha=datetime.date(2012, 12, 9), jugador1='J.J. Wolf', jugador2='Alexander Bublik', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=9)
Alexander Bublik --> PartidoTenis(fecha=datetime.date(2012, 12, 9), jugador1='J.J. Wolf', jugador2='Alexander Bublik', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=9)
Bernabé Zapata Miralles --> PartidoTenis(fecha=datetime.date(2014, 1, 26), jugador1='Alexander Bublik', jugador2='Bernabé Zapata Miralles', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2)], errores_nf1=11, errores_nf2=13)
Alejandro Davidovich Fokina --> PartidoTenis(fecha=datetime.date(2018, 11, 17), jugador1='Bernabé Zapata Miralles', jugador2='Alejandro Davidovich Fokina', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=1)], errores_nf1=10, errores_nf2=7)
Denis Shapovalov --> PartidoTenis(fecha=datetime.date(2016, 5, 3), jugador1='Denis Shapovalov', jugador2='Yoshihito Nishioka', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=12, errores_nf2=12)
Yoshihito Nishioka --> PartidoTenis(fecha=datetime.date(2016, 5, 3), jugador1='Denis Shapovalov', jugador2='Yoshihito Nishioka', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=12, errores_nf2=12)
Gael Monfils --> PartidoTenis(fecha=datetime.date(2011, 12, 19), jugador1='Gael Monfils', jugador2='Pedro Cachin', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=16, errores_nf2=14)
Laslo Djere --> PartidoTenis(fecha=datetime.date(2020, 9, 9), jugador1='Nuno Borges', jugador2='Laslo Djere', superficie='Tierra', resultado=[Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=5, errores_nf2=15)
David Goffin --> PartidoTenis(fecha=datetime.date(2015, 3, 13), jugador1='David Goffin', jugador2='Cristian Garín', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=11, errores_nf2=9)
Maxime Cressy --> PartidoTenis(fecha=datetime.date(2012, 12, 11), jugador1='David Goffin', jugador2='Maxime Cressy', superficie='Hierba', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=9, errores_nf2=10)
Taro Daniel --> PartidoTenis(fecha=datetime.date(2015, 4, 28), jugador1='Taro Daniel', jugador2="Christopher O'Connell", superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=9)
Casper Ruud --> PartidoTenis(fecha=datetime.date(2010, 11, 7), jugador1='Carlos Alcaraz', jugador2='Casper Ruud', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=17, errores_nf2=19)
Karen Khachanov --> PartidoTenis(fecha=datetime.date(2020, 1, 2), jugador1='Karen Khachanov', jugador2='Jaume Munar', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=12, errores_nf2=2)
Holger Rune --> PartidoTenis(fecha=datetime.date(2019, 8, 16), jugador1="Christopher O'Connell", jugador2='Holger Rune', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=6)
Pavel Kotov --> PartidoTenis(fecha=datetime.date(2012, 7, 21), jugador1='Pavel Kotov', jugador2='Alex Molcan', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=17, errores_nf2=12)
Roberto Carballés Baena --> PartidoTenis(fecha=datetime.date(2014, 7, 6), jugador1='Botic Van de Zandschulp', jugador2='Roberto Carballés Baena', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=18, errores_nf2=8)
Thanasi Kokkinakis --> PartidoTenis(fecha=datetime.date(2010, 10, 14), jugador1='Thanasi Kokkinakis', jugador2='Roman Safiullin', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=3, juegos_j2=6)], errores_nf1=15, errores_nf2=14)
Marin Cilic --> PartidoTenis(fecha=datetime.date(2018, 1, 4), jugador1='Ugo Humbert', jugador2='Marin Cilic', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=11)
Taylor Fritz --> PartidoTenis(fecha=datetime.date(2020, 12, 2), jugador1='Carlos Alcaraz', jugador2='Taylor Fritz', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=13, errores_nf2=8)
Andrey Rublev --> PartidoTenis(fecha=datetime.date(2010, 11, 22), jugador1='Dominic Thiem', jugador2='Andrey Rublev', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=16, errores_nf2=16)
Felix Auger-Aliassime --> PartidoTenis(fecha=datetime.date(2015, 9, 17), jugador1='Felix Auger-Aliassime', jugador2='Rafael Nadal', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=1, errores_nf2=11)
Vasek Pospisil --> PartidoTenis(fecha=datetime.date(2017, 4, 20), jugador1='Vasek Pospisil', jugador2='Taylor Fritz', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=10, errores_nf2=7)
Alex Molcan --> PartidoTenis(fecha=datetime.date(2012, 7, 21), jugador1='Pavel Kotov', jugador2='Alex Molcan', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=17, errores_nf2=12)
Nick Kyrgios --> PartidoTenis(fecha=datetime.date(2014, 3, 26), jugador1='Nick Kyrgios', jugador2='Federico Coria', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=7)
Daniel Elahi Galán --> PartidoTenis(fecha=datetime.date(2017, 10, 12), jugador1='Daniel Elahi Galán', jugador2='Roberto Carballés Baena', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=9, errores_nf2=2)
Borna Coric --> PartidoTenis(fecha=datetime.date(2010, 5, 27), jugador1='Albert Ramos Vi±olas', jugador2='Borna Coric', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=14, errores_nf2=13)
Jiri Lehecka --> PartidoTenis(fecha=datetime.date(2020, 6, 16), jugador1='Soon Woo Kwon', jugador2='Jiri Lehecka', superficie='Hierba', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=15)
Stefanos Tsitsipas --> PartidoTenis(fecha=datetime.date(2017, 7, 29), jugador1='Stefanos Tsitsipas', jugador2='Casper Ruud', superficie='Dura', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=17, errores_nf2=12)
Matteo Berrettini --> PartidoTenis(fecha=datetime.date(2010, 9, 1), jugador1='Matteo Berrettini', jugador2='Alex Molcan', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=13, errores_nf2=9)
Daniel Evans --> PartidoTenis(fecha=datetime.date(2014, 9, 20), jugador1='Daniel Evans', jugador2='Ben Shelton', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=11, errores_nf2=7)
Brandon Nakashima --> PartidoTenis(fecha=datetime.date(2016, 8, 9), jugador1='Brandon Nakashima', jugador2='Tomas Machac', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=10)
Tomas Machac --> PartidoTenis(fecha=datetime.date(2016, 8, 9), jugador1='Brandon Nakashima', jugador2='Tomas Machac', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=10)
Cameron Norrie --> PartidoTenis(fecha=datetime.date(2017, 12, 21), jugador1='Carlos Alcaraz', jugador2='Cameron Norrie', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=10, errores_nf2=15)
Kamil Majchrzak --> PartidoTenis(fecha=datetime.date(2019, 4, 10), jugador1='Borna Coric', jugador2='Kamil Majchrzak', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=8, errores_nf2=5)
Pedro Cachin --> PartidoTenis(fecha=datetime.date(2011, 12, 19), jugador1='Gael Monfils', jugador2='Pedro Cachin', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=16, errores_nf2=14)
Pablo Carre±o Busta --> PartidoTenis(fecha=datetime.date(2015, 10, 27), jugador1='Daniel Altmaier', jugador2='Pablo Carre±o Busta', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=15)
Frances Tiafoe --> PartidoTenis(fecha=datetime.date(2014, 9, 20), jugador1='Frances Tiafoe', jugador2='John Isner', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=11)
Oscar Otte --> PartidoTenis(fecha=datetime.date(2010, 4, 24), jugador1='Oscar Otte', jugador2='Roman Safiullin', superficie='Dura', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=4)
Marc-Andrea Huesler --> PartidoTenis(fecha=datetime.date(2012, 7, 19), jugador1='Marc-Andrea Huesler', jugador2='Ugo Humbert', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=11, errores_nf2=7)
Jannik Sinner --> PartidoTenis(fecha=datetime.date(2015, 10, 25), jugador1='Jannik Sinner', jugador2='John Isner', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=8, errores_nf2=11)
Dominic Thiem --> PartidoTenis(fecha=datetime.date(2010, 11, 22), jugador1='Dominic Thiem', jugador2='Andrey Rublev', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=16, errores_nf2=16)
Rafael Nadal --> PartidoTenis(fecha=datetime.date(2015, 8, 8), jugador1='Dominic Thiem', jugador2='Rafael Nadal', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=16)
Roger Federer --> PartidoTenis(fecha=datetime.date(2014, 10, 10), jugador1='Stefanos Tsitsipas', jugador2='Roger Federer', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=17, errores_nf2=20)
Roberto Bautista Agut --> PartidoTenis(fecha=datetime.date(2016, 1, 17), jugador1='Rafael Nadal', jugador2='Roberto Bautista Agut', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=3, juegos_j2=6)], errores_nf1=12, errores_nf2=19)
EJERCICIO 12==================================================
Test de 'partido_mas_errores_por_mes' superficies=['Sintética']
Los partidos con mas errores para las superificies ['Sintética'] son
12 --> (datetime.date(2017, 12, 27), 'Diego Schwartzman', 'Daniil Medvedev')
3 --> (datetime.date(2017, 3, 20), 'Alexander Zverev', 'Casper Ruud')
10 --> (datetime.date(2020, 10, 4), 'Diego Schwartzman', 'Stefanos Tsitsipas')
5 --> (datetime.date(2020, 5, 29), 'Rafael Nadal', 'Felix Auger-Aliassime')
9 --> (datetime.date(2010, 9, 20), 'Carlos Alcaraz', 'Stefanos Tsitsipas')
2 --> (datetime.date(2013, 2, 9), 'Felix Auger-Aliassime', 'Diego Schwartzman')
6 --> (datetime.date(2017, 6, 14), 'Andrey Rublev', 'Daniil Medvedev')
11 --> (datetime.date(2013, 11, 29), 'Diego Schwartzman', 'Andrey Rublev')
1 --> (datetime.date(2015, 1, 28), 'Stefanos Tsitsipas', 'Casper Ruud')
Test de 'partido_mas_errores_por_mes' superficies=['Sintética', 'Tierra']
Los partidos con mas errores para las superificies ['Sintética', 'Tierra'] son
1 --> (datetime.date(2020, 1, 24), 'Tomas Martin Etcheverry', 'Vasek Pospisil')
12 --> (datetime.date(2010, 12, 12), 'Jenson Brooksby', 'Roman Safiullin')
6 --> (datetime.date(2017, 6, 14), 'Andrey Rublev', 'Daniil Medvedev')
9 --> (datetime.date(2010, 9, 1), 'Matteo Berrettini', 'Alex Molcan')
2 --> (datetime.date(2013, 2, 9), 'Felix Auger-Aliassime', 'Diego Schwartzman')
4 --> (datetime.date(2011, 4, 3), 'Novak Djokovic', 'Carlos Alcaraz')
3 --> (datetime.date(2019, 3, 2), 'Andrey Rublev', 'Quentin Halys')
11 --> (datetime.date(2010, 11, 7), 'Carlos Alcaraz', 'Casper Ruud')
5 --> (datetime.date(2012, 5, 30), 'Alexander Zverev', 'Novak Djokovic')
8 --> (datetime.date(2013, 8, 12), 'Lorenzo Musetti', 'Ben Shelton')
7 --> (datetime.date(2013, 7, 3), 'Stefanos Tsitsipas', 'Alexander Zverev')
10 --> (datetime.date(2014, 10, 10), 'Stefanos Tsitsipas', 'Roger Federer')
Test de 'partido_mas_errores_por_mes' superficies=None
Los partidos con mas errores para las superificies None son
11 --> (datetime.date(2010, 11, 7), 'Carlos Alcaraz', 'Casper Ruud')
3 --> (datetime.date(2011, 3, 13), 'Roger Federer', 'Rafael Nadal')
1 --> (datetime.date(2016, 1, 15), 'Benjamin Bonzi', 'Diego Schwartzman')
8 --> (datetime.date(2016, 8, 14), 'Rafael Nadal', 'Casper Ruud')
12 --> (datetime.date(2010, 12, 12), 'Jenson Brooksby', 'Roman Safiullin')
7 --> (datetime.date(2013, 7, 3), 'Stefanos Tsitsipas', 'Alexander Zverev')
10 --> (datetime.date(2014, 10, 10), 'Stefanos Tsitsipas', 'Roger Federer')
6 --> (datetime.date(2011, 6, 18), 'Filip Krajinovic', 'Diego Schwartzman')
4 --> (datetime.date(2013, 4, 23), 'Roman Safiullin', 'Carlos Alcaraz')
9 --> (datetime.date(2020, 9, 4), 'Jordan Thompson', 'Jenson Brooksby')
2 --> (datetime.date(2016, 2, 9), 'Roberto Bautista Agut', 'Felix Auger-Aliassime')
5 --> (datetime.date(2012, 5, 30), 'Alexander Zverev', 'Novak Djokovic')
EJERCICIO 13==================================================
Test de 'n_partidos_mas_errores_por_jugador' n=3
Los 3 partidos con mas errores para los jugadores son
Sebastian Korda --> [PartidoTenis(fecha=datetime.date(2011, 11, 10), jugador1='John Isner', jugador2='Sebastian Korda', superficie='Hierba', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=10), PartidoTenis(fecha=datetime.date(2011, 11, 7), jugador1='Sebastian Korda', jugador2='Ben Shelton', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=3, juegos_j2=6)], errores_nf1=8, errores_nf2=6)]
Ben Shelton --> [PartidoTenis(fecha=datetime.date(2013, 8, 12), jugador1='Lorenzo Musetti', jugador2='Ben Shelton', superficie='Tierra', resultado=[Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=19), PartidoTenis(fecha=datetime.date(2018, 7, 20), jugador1='Vasek Pospisil', jugador2='Ben Shelton', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=2, errores_nf2=17), PartidoTenis(fecha=datetime.date(2014, 9, 20), jugador1='Daniel Evans', jugador2='Ben Shelton', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=11, errores_nf2=7)]
Benjamin Bonzi --> [PartidoTenis(fecha=datetime.date(2016, 1, 15), jugador1='Benjamin Bonzi', jugador2='Diego Schwartzman', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=15), PartidoTenis(fecha=datetime.date(2019, 3, 27), jugador1='Benjamin Bonzi', jugador2='Sebastian Baez', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=8, errores_nf2=10)]
Sebastian Baez --> [PartidoTenis(fecha=datetime.date(2010, 7, 1), jugador1='Federico Coria', jugador2='Sebastian Baez', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=5, errores_nf2=17), PartidoTenis(fecha=datetime.date(2019, 3, 27), jugador1='Benjamin Bonzi', jugador2='Sebastian Baez', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=8, errores_nf2=10)]
John Isner --> [PartidoTenis(fecha=datetime.date(2016, 1, 17), jugador1='John Isner', jugador2="Christopher O'Connell", superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=13), PartidoTenis(fecha=datetime.date(2011, 11, 10), jugador1='John Isner', jugador2='Sebastian Korda', superficie='Hierba', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=10), PartidoTenis(fecha=datetime.date(2014, 9, 20), jugador1='Frances Tiafoe', jugador2='John Isner', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=11)]
Christopher O'Connell --> [PartidoTenis(fecha=datetime.date(2016, 1, 17), jugador1='John Isner', jugador2="Christopher O'Connell", superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=13), PartidoTenis(fecha=datetime.date(2019, 8, 16), jugador1="Christopher O'Connell", jugador2='Holger Rune', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=6), PartidoTenis(fecha=datetime.date(2015, 4, 28), jugador1='Taro Daniel', jugador2="Christopher O'Connell", superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=9)]
Daniel Altmaier --> [PartidoTenis(fecha=datetime.date(2015, 10, 27), jugador1='Daniel Altmaier', jugador2='Pablo Carre±o Busta', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=15), PartidoTenis(fecha=datetime.date(2019, 3, 26), jugador1='Daniel Altmaier', jugador2='Hubert Hurkacz', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=6, errores_nf2=6), PartidoTenis(fecha=datetime.date(2013, 1, 12), jugador1='Federico Coria', jugador2='Daniel Altmaier', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=9, errores_nf2=5)]
Hubert Hurkacz --> [PartidoTenis(fecha=datetime.date(2019, 3, 26), jugador1='Daniel Altmaier', jugador2='Hubert Hurkacz', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=6, errores_nf2=6)]
Jack Draper --> [PartidoTenis(fecha=datetime.date(2011, 2, 13), jugador1='Marton Fucsovics', jugador2='Jack Draper', superficie='Dura', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=12), PartidoTenis(fecha=datetime.date(2014, 8, 13), jugador1='Jack Draper', jugador2='Quentin Halys', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=10), PartidoTenis(fecha=datetime.date(2017, 11, 28), jugador1='Jack Draper', jugador2='Nikoloz Basilashvili', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=8, errores_nf2=10)]
Nikoloz Basilashvili --> [PartidoTenis(fecha=datetime.date(2017, 11, 28), jugador1='Jack Draper', jugador2='Nikoloz Basilashvili', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=8, errores_nf2=10), PartidoTenis(fecha=datetime.date(2019, 7, 25), jugador1='Nikoloz Basilashvili', jugador2='Adrian Mannarino', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=17), PartidoTenis(fecha=datetime.date(2017, 7, 10), jugador1='Nikoloz Basilashvili', jugador2='Tomas Martin Etcheverry', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=4, errores_nf2=10)]
Miomir Kecmanovic --> [PartidoTenis(fecha=datetime.date(2017, 8, 10), jugador1='Miomir Kecmanovic', jugador2='Roman Safiullin', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=12)]
Roman Safiullin --> [PartidoTenis(fecha=datetime.date(2010, 12, 12), jugador1='Jenson Brooksby', jugador2='Roman Safiullin', superficie='Tierra', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=20), PartidoTenis(fecha=datetime.date(2013, 4, 23), jugador1='Roman Safiullin', jugador2='Carlos Alcaraz', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=14), PartidoTenis(fecha=datetime.date(2010, 10, 14), jugador1='Thanasi Kokkinakis', jugador2='Roman Safiullin', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=3, juegos_j2=6)], errores_nf1=15, errores_nf2=14)]
Marton Fucsovics --> [PartidoTenis(fecha=datetime.date(2019, 8, 13), jugador1='Marton Fucsovics', jugador2='Gregoire Barrere', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=13, errores_nf2=5), PartidoTenis(fecha=datetime.date(2011, 2, 13), jugador1='Marton Fucsovics', jugador2='Jack Draper', superficie='Dura', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=12)]
Gregoire Barrere --> [PartidoTenis(fecha=datetime.date(2019, 8, 13), jugador1='Marton Fucsovics', jugador2='Gregoire Barrere', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=13, errores_nf2=5)]
Ugo Humbert --> [PartidoTenis(fecha=datetime.date(2018, 1, 4), jugador1='Ugo Humbert', jugador2='Marin Cilic', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=11), PartidoTenis(fecha=datetime.date(2014, 12, 13), jugador1='Ugo Humbert', jugador2='Pedro Martínez', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=8, errores_nf2=10), PartidoTenis(fecha=datetime.date(2012, 7, 19), jugador1='Marc-Andrea Huesler', jugador2='Ugo Humbert', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=11, errores_nf2=7)]
Pedro Martínez --> [PartidoTenis(fecha=datetime.date(2012, 2, 24), jugador1='Pedro Martínez', jugador2='John Isner', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=10), PartidoTenis(fecha=datetime.date(2014, 12, 13), jugador1='Ugo Humbert', jugador2='Pedro Martínez', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=8, errores_nf2=10)]
Adrian Mannarino --> [PartidoTenis(fecha=datetime.date(2019, 7, 25), jugador1='Nikoloz Basilashvili', jugador2='Adrian Mannarino', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=17), PartidoTenis(fecha=datetime.date(2011, 6, 3), jugador1='Yoshihito Nishioka', jugador2='Adrian Mannarino', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=7), PartidoTenis(fecha=datetime.date(2020, 7, 9), jugador1='Adrian Mannarino', jugador2='Botic Van de Zandschulp', superficie='Dura', resultado=[Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=3, errores_nf2=5)]
Botic Van de Zandschulp --> [PartidoTenis(fecha=datetime.date(2014, 7, 6), jugador1='Botic Van de Zandschulp', jugador2='Roberto Carballés Baena', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=18, errores_nf2=8), PartidoTenis(fecha=datetime.date(2020, 4, 17), jugador1='Botic Van de Zandschulp', jugador2='Albert Ramos Vi±olas', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=10), PartidoTenis(fecha=datetime.date(2020, 7, 9), jugador1='Adrian Mannarino', jugador2='Botic Van de Zandschulp', superficie='Dura', resultado=[Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=3, errores_nf2=5)]
Jordan Thompson --> [PartidoTenis(fecha=datetime.date(2013, 10, 21), jugador1='Jordan Thompson', jugador2='Quentin Halys', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=3, juegos_j2=6)], errores_nf1=19, errores_nf2=1), PartidoTenis(fecha=datetime.date(2020, 9, 4), jugador1='Jordan Thompson', jugador2='Jenson Brooksby', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=14), PartidoTenis(fecha=datetime.date(2013, 6, 23), jugador1='Jordan Thompson', jugador2='Thanasi Kokkinakis', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=13)]
Quentin Halys --> [PartidoTenis(fecha=datetime.date(2019, 3, 2), jugador1='Andrey Rublev', jugador2='Quentin Halys', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=15, errores_nf2=15), PartidoTenis(fecha=datetime.date(2014, 8, 13), jugador1='Jack Draper', jugador2='Quentin Halys', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=10), PartidoTenis(fecha=datetime.date(2017, 3, 16), jugador1='Andrey Rublev', jugador2='Quentin Halys', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=19, errores_nf2=7)]
Tommy Paul --> [PartidoTenis(fecha=datetime.date(2013, 12, 19), jugador1='Holger Rune', jugador2='Tommy Paul', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=5, errores_nf2=8), PartidoTenis(fecha=datetime.date(2017, 8, 26), jugador1='Tommy Paul', jugador2='Novak Djokovic', superficie='Dura', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=22)]
Novak Djokovic --> [PartidoTenis(fecha=datetime.date(2017, 8, 26), jugador1='Tommy Paul', jugador2='Novak Djokovic', superficie='Dura', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=22), PartidoTenis(fecha=datetime.date(2011, 4, 3), jugador1='Novak Djokovic', jugador2='Carlos Alcaraz', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=19, errores_nf2=8), PartidoTenis(fecha=datetime.date(2011, 1, 9), jugador1='Novak Djokovic', jugador2='Dominic Thiem', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=19, errores_nf2=2)]
Lorenzo Sonego --> [PartidoTenis(fecha=datetime.date(2019, 6, 22), jugador1='Lorenzo Sonego', jugador2='Roman Safiullin', superficie='Tierra', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=6, errores_nf2=7), PartidoTenis(fecha=datetime.date(2020, 2, 21), jugador1='Taro Daniel', jugador2='Lorenzo Sonego', superficie='Tierra', resultado=[Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=6)]
Carlos Alcaraz --> [PartidoTenis(fecha=datetime.date(2017, 12, 5), jugador1='Carlos Alcaraz', jugador2='Casper Ruud', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=20, errores_nf2=5), PartidoTenis(fecha=datetime.date(2010, 9, 20), jugador1='Carlos Alcaraz', jugador2='Stefanos Tsitsipas', superficie='Sintética', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=1, juegos_j2=6)], errores_nf1=17, errores_nf2=1), PartidoTenis(fecha=datetime.date(2010, 11, 7), jugador1='Carlos Alcaraz', jugador2='Casper Ruud', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=17, errores_nf2=19)]
Tomas Martin Etcheverry --> [PartidoTenis(fecha=datetime.date(2020, 1, 24), jugador1='Tomas Martin Etcheverry', jugador2='Vasek Pospisil', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=11), PartidoTenis(fecha=datetime.date(2010, 6, 19), jugador1='Tomas Martin Etcheverry', jugador2='Cristian Garín', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=13), PartidoTenis(fecha=datetime.date(2017, 7, 10), jugador1='Nikoloz Basilashvili', jugador2='Tomas Martin Etcheverry', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=4, errores_nf2=10)]
Cristian Garín --> [PartidoTenis(fecha=datetime.date(2010, 6, 19), jugador1='Tomas Martin Etcheverry', jugador2='Cristian Garín', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=13), PartidoTenis(fecha=datetime.date(2016, 9, 9), jugador1='Cristian Garín', jugador2='Alex de Mi±aur', superficie='Tierra', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=13, errores_nf2=7), PartidoTenis(fecha=datetime.date(2020, 3, 19), jugador1='Cristian Garín', jugador2='Tomas Martin Etcheverry', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=13, errores_nf2=6)]
Arthur Rinderknech --> [PartidoTenis(fecha=datetime.date(2012, 10, 25), jugador1='Arthur Rinderknech', jugador2='Richard Gasquet', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=0)], errores_nf1=8, errores_nf2=7), PartidoTenis(fecha=datetime.date(2012, 9, 2), jugador1='Casper Ruud', jugador2='Arthur Rinderknech', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=13, errores_nf2=1)]
Richard Gasquet --> [PartidoTenis(fecha=datetime.date(2012, 10, 24), jugador1='Nick Kyrgios', jugador2='Richard Gasquet', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=16), PartidoTenis(fecha=datetime.date(2016, 11, 21), jugador1='Diego Schwartzman', jugador2='Richard Gasquet', superficie='Dura', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=19, errores_nf2=10), PartidoTenis(fecha=datetime.date(2012, 10, 25), jugador1='Arthur Rinderknech', jugador2='Richard Gasquet', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=0)], errores_nf1=8, errores_nf2=7)]
Alex de Mi±aur --> [PartidoTenis(fecha=datetime.date(2013, 1, 8), jugador1='Emil Ruusuvuori', jugador2='Alex de Mi±aur', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=11), PartidoTenis(fecha=datetime.date(2012, 10, 14), jugador1='Jenson Brooksby', jugador2='Alex de Mi±aur', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=5, errores_nf2=8), PartidoTenis(fecha=datetime.date(2016, 9, 9), jugador1='Cristian Garín', jugador2='Alex de Mi±aur', superficie='Tierra', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=13, errores_nf2=7)]
Lorenzo Musetti --> [PartidoTenis(fecha=datetime.date(2018, 7, 18), jugador1='Lorenzo Musetti', jugador2='Roman Safiullin', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=6), PartidoTenis(fecha=datetime.date(2012, 4, 20), jugador1='Pedro Cachin', jugador2='Lorenzo Musetti', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=8, errores_nf2=10), PartidoTenis(fecha=datetime.date(2013, 8, 12), jugador1='Lorenzo Musetti', jugador2='Ben Shelton', superficie='Tierra', resultado=[Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=19)]
Jenson Brooksby --> [PartidoTenis(fecha=datetime.date(2010, 12, 12), jugador1='Jenson Brooksby', jugador2='Roman Safiullin', superficie='Tierra', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=20), PartidoTenis(fecha=datetime.date(2020, 4, 25), jugador1='Mikael Ymer', jugador2='Jenson Brooksby', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=10, errores_nf2=15), PartidoTenis(fecha=datetime.date(2020, 9, 4), jugador1='Jordan Thompson', jugador2='Jenson Brooksby', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=14)]
Filip Krajinovic --> [PartidoTenis(fecha=datetime.date(2011, 6, 18), jugador1='Filip Krajinovic', jugador2='Diego Schwartzman', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=20, errores_nf2=12), PartidoTenis(fecha=datetime.date(2010, 11, 16), jugador1='Filip Krajinovic', jugador2='Emil Ruusuvuori', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=8)]
Diego Schwartzman --> [PartidoTenis(fecha=datetime.date(2016, 11, 21), jugador1='Diego Schwartzman', jugador2='Richard Gasquet', superficie='Dura', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=19, errores_nf2=10), PartidoTenis(fecha=datetime.date(2013, 2, 9), jugador1='Felix Auger-Aliassime', jugador2='Diego Schwartzman', superficie='Sintética', resultado=[Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=9, errores_nf2=19), PartidoTenis(fecha=datetime.date(2013, 7, 15), jugador1='Diego Schwartzman', jugador2='Carlos Alcaraz', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=19, errores_nf2=9)]
Alexander Zverev --> [PartidoTenis(fecha=datetime.date(2012, 5, 30), jugador1='Alexander Zverev', jugador2='Novak Djokovic', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=20, errores_nf2=18), PartidoTenis(fecha=datetime.date(2013, 7, 3), jugador1='Stefanos Tsitsipas', jugador2='Alexander Zverev', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=20), PartidoTenis(fecha=datetime.date(2018, 5, 1), jugador1='Diego Schwartzman', jugador2='Alexander Zverev', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=16)]
Emil Ruusuvuori --> [PartidoTenis(fecha=datetime.date(2010, 11, 16), jugador1='Filip Krajinovic', jugador2='Emil Ruusuvuori', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=8), PartidoTenis(fecha=datetime.date(2013, 1, 8), jugador1='Emil Ruusuvuori', jugador2='Alex de Mi±aur', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=11), PartidoTenis(fecha=datetime.date(2012, 4, 16), jugador1='Alexander Zverev', jugador2='Emil Ruusuvuori', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=3)]
Constant Lestienne --> [PartidoTenis(fecha=datetime.date(2012, 2, 26), jugador1='Constant Lestienne', jugador2='Federico Coria', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=10, errores_nf2=7), PartidoTenis(fecha=datetime.date(2014, 4, 15), jugador1='Roberto Carballés Baena', jugador2='Constant Lestienne', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=9)]
Federico Coria --> [PartidoTenis(fecha=datetime.date(2013, 1, 12), jugador1='Federico Coria', jugador2='Daniel Altmaier', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=9, errores_nf2=5), PartidoTenis(fecha=datetime.date(2012, 2, 26), jugador1='Constant Lestienne', jugador2='Federico Coria', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=10, errores_nf2=7), PartidoTenis(fecha=datetime.date(2014, 3, 26), jugador1='Nick Kyrgios', jugador2='Federico Coria', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=7)]
Jaume Munar --> [PartidoTenis(fecha=datetime.date(2020, 2, 8), jugador1='Jaume Munar', jugador2='Andrey Rublev', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=15, errores_nf2=8), PartidoTenis(fecha=datetime.date(2020, 11, 9), jugador1='Stefanos Tsitsipas', jugador2='Jaume Munar', superficie='Dura', resultado=[Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=3, errores_nf2=10), PartidoTenis(fecha=datetime.date(2020, 8, 1), jugador1='Jaume Munar', jugador2='Grigor Dimitrov', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=14)]
Grigor Dimitrov --> [PartidoTenis(fecha=datetime.date(2020, 8, 1), jugador1='Jaume Munar', jugador2='Grigor Dimitrov', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=14)]
Mikael Ymer --> [PartidoTenis(fecha=datetime.date(2020, 4, 25), jugador1='Mikael Ymer', jugador2='Jenson Brooksby', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=10, errores_nf2=15), PartidoTenis(fecha=datetime.date(2014, 4, 1), jugador1='Mikael Ymer', jugador2='Mikael Ymer', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=1)], errores_nf1=3, errores_nf2=5), PartidoTenis(fecha=datetime.date(2014, 4, 1), jugador1='Mikael Ymer', jugador2='Mikael Ymer', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=1)], errores_nf1=3, errores_nf2=5)]
Nuno Borges --> [PartidoTenis(fecha=datetime.date(2012, 3, 28), jugador1='Nuno Borges', jugador2='Fabio Fognini', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=13), PartidoTenis(fecha=datetime.date(2020, 9, 9), jugador1='Nuno Borges', jugador2='Laslo Djere', superficie='Tierra', resultado=[Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=5, errores_nf2=15)]
Fabio Fognini --> [PartidoTenis(fecha=datetime.date(2012, 3, 28), jugador1='Nuno Borges', jugador2='Fabio Fognini', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=13)]
Daniil Medvedev --> [PartidoTenis(fecha=datetime.date(2017, 9, 6), jugador1='Roger Federer', jugador2='Daniil Medvedev', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=2)], errores_nf1=4, errores_nf2=19), PartidoTenis(fecha=datetime.date(2017, 2, 16), jugador1='Felix Auger-Aliassime', jugador2='Daniil Medvedev', superficie='Tierra', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=6, errores_nf2=18), PartidoTenis(fecha=datetime.date(2010, 8, 28), jugador1='Andrey Rublev', jugador2='Daniil Medvedev', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=6)], errores_nf1=4, errores_nf2=16)]
Soon Woo Kwon --> [PartidoTenis(fecha=datetime.date(2020, 6, 16), jugador1='Soon Woo Kwon', jugador2='Jiri Lehecka', superficie='Hierba', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=15), PartidoTenis(fecha=datetime.date(2011, 9, 23), jugador1='Daniil Medvedev', jugador2='Soon Woo Kwon', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=4, errores_nf2=3)]
Aslan Karatsev --> [PartidoTenis(fecha=datetime.date(2020, 12, 6), jugador1='Aslan Karatsev', jugador2='Albert Ramos Vi±olas', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=6)]
Albert Ramos Vi±olas --> [PartidoTenis(fecha=datetime.date(2010, 5, 27), jugador1='Albert Ramos Vi±olas', jugador2='Borna Coric', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=14, errores_nf2=13), PartidoTenis(fecha=datetime.date(2014, 10, 25), jugador1='Felix Auger-Aliassime', jugador2='Albert Ramos Vi±olas', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=12), PartidoTenis(fecha=datetime.date(2020, 4, 17), jugador1='Botic Van de Zandschulp', jugador2='Albert Ramos Vi±olas', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=10)]
J.J. Wolf --> [PartidoTenis(fecha=datetime.date(2012, 12, 9), jugador1='J.J. Wolf', jugador2='Alexander Bublik', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=9)]
Alexander Bublik --> [PartidoTenis(fecha=datetime.date(2014, 1, 26), jugador1='Alexander Bublik', jugador2='Bernabé Zapata Miralles', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2)], errores_nf1=11, errores_nf2=13), PartidoTenis(fecha=datetime.date(2012, 12, 9), jugador1='J.J. Wolf', jugador2='Alexander Bublik', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=9)]
Bernabé Zapata Miralles --> [PartidoTenis(fecha=datetime.date(2014, 1, 26), jugador1='Alexander Bublik', jugador2='Bernabé Zapata Miralles', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2)], errores_nf1=11, errores_nf2=13), PartidoTenis(fecha=datetime.date(2018, 11, 17), jugador1='Bernabé Zapata Miralles', jugador2='Alejandro Davidovich Fokina', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=1)], errores_nf1=10, errores_nf2=7)]
Alejandro Davidovich Fokina --> [PartidoTenis(fecha=datetime.date(2018, 11, 17), jugador1='Bernabé Zapata Miralles', jugador2='Alejandro Davidovich Fokina', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=1)], errores_nf1=10, errores_nf2=7)]
Denis Shapovalov --> [PartidoTenis(fecha=datetime.date(2016, 5, 3), jugador1='Denis Shapovalov', jugador2='Yoshihito Nishioka', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=12, errores_nf2=12)]
Yoshihito Nishioka --> [PartidoTenis(fecha=datetime.date(2016, 5, 3), jugador1='Denis Shapovalov', jugador2='Yoshihito Nishioka', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=12, errores_nf2=12), PartidoTenis(fecha=datetime.date(2011, 6, 3), jugador1='Yoshihito Nishioka', jugador2='Adrian Mannarino', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=7)]
Gael Monfils --> [PartidoTenis(fecha=datetime.date(2011, 12, 19), jugador1='Gael Monfils', jugador2='Pedro Cachin', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=16, errores_nf2=14), PartidoTenis(fecha=datetime.date(2010, 5, 7), jugador1='Gael Monfils', jugador2='Laslo Djere', superficie='Dura', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=2)], errores_nf1=13, errores_nf2=13), PartidoTenis(fecha=datetime.date(2016, 2, 17), jugador1='Borna Coric', jugador2='Gael Monfils', superficie='Dura', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=9)]
Laslo Djere --> [PartidoTenis(fecha=datetime.date(2020, 9, 9), jugador1='Nuno Borges', jugador2='Laslo Djere', superficie='Tierra', resultado=[Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=5, errores_nf2=15), PartidoTenis(fecha=datetime.date(2010, 5, 7), jugador1='Gael Monfils', jugador2='Laslo Djere', superficie='Dura', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=2)], errores_nf1=13, errores_nf2=13)]
David Goffin --> [PartidoTenis(fecha=datetime.date(2015, 3, 13), jugador1='David Goffin', jugador2='Cristian Garín', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=11, errores_nf2=9), PartidoTenis(fecha=datetime.date(2012, 12, 11), jugador1='David Goffin', jugador2='Maxime Cressy', superficie='Hierba', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=9, errores_nf2=10), PartidoTenis(fecha=datetime.date(2010, 5, 27), jugador1='Novak Djokovic', jugador2='David Goffin', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=12, errores_nf2=7)]
Maxime Cressy --> [PartidoTenis(fecha=datetime.date(2012, 12, 11), jugador1='David Goffin', jugador2='Maxime Cressy', superficie='Hierba', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=9, errores_nf2=10)]
Taro Daniel --> [PartidoTenis(fecha=datetime.date(2015, 4, 28), jugador1='Taro Daniel', jugador2="Christopher O'Connell", superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=9), PartidoTenis(fecha=datetime.date(2020, 2, 21), jugador1='Taro Daniel', jugador2='Lorenzo Sonego', superficie='Tierra', resultado=[Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=6)]
Casper Ruud --> [PartidoTenis(fecha=datetime.date(2015, 11, 30), jugador1='Casper Ruud', jugador2='Novak Djokovic', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=0)], errores_nf1=19, errores_nf2=10), PartidoTenis(fecha=datetime.date(2010, 11, 7), jugador1='Carlos Alcaraz', jugador2='Casper Ruud', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=17, errores_nf2=19), PartidoTenis(fecha=datetime.date(2019, 1, 26), jugador1='Diego Schwartzman', jugador2='Casper Ruud', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=18)]
Karen Khachanov --> [PartidoTenis(fecha=datetime.date(2020, 1, 2), jugador1='Karen Khachanov', jugador2='Jaume Munar', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=12, errores_nf2=2)]
Holger Rune --> [PartidoTenis(fecha=datetime.date(2019, 8, 16), jugador1="Christopher O'Connell", jugador2='Holger Rune', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=6), PartidoTenis(fecha=datetime.date(2013, 12, 19), jugador1='Holger Rune', jugador2='Tommy Paul', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=5, errores_nf2=8)]
Pavel Kotov --> [PartidoTenis(fecha=datetime.date(2012, 7, 21), jugador1='Pavel Kotov', jugador2='Alex Molcan', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=17, errores_nf2=12), PartidoTenis(fecha=datetime.date(2013, 12, 25), jugador1='Pavel Kotov', jugador2='Roberto Carballés Baena', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=9, errores_nf2=5), PartidoTenis(fecha=datetime.date(2013, 3, 24), jugador1='Pavel Kotov', jugador2='Casper Ruud', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=5)]
Roberto Carballés Baena --> [PartidoTenis(fecha=datetime.date(2014, 4, 15), jugador1='Roberto Carballés Baena', jugador2='Constant Lestienne', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=9, errores_nf2=9), PartidoTenis(fecha=datetime.date(2014, 7, 6), jugador1='Botic Van de Zandschulp', jugador2='Roberto Carballés Baena', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=18, errores_nf2=8), PartidoTenis(fecha=datetime.date(2013, 12, 25), jugador1='Pavel Kotov', jugador2='Roberto Carballés Baena', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=9, errores_nf2=5)]
Thanasi Kokkinakis --> [PartidoTenis(fecha=datetime.date(2010, 10, 14), jugador1='Thanasi Kokkinakis', jugador2='Roman Safiullin', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=3, juegos_j2=6)], errores_nf1=15, errores_nf2=14), PartidoTenis(fecha=datetime.date(2013, 6, 23), jugador1='Jordan Thompson', jugador2='Thanasi Kokkinakis', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=13)]
Marin Cilic --> [PartidoTenis(fecha=datetime.date(2018, 1, 4), jugador1='Ugo Humbert', jugador2='Marin Cilic', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=7)], errores_nf1=11, errores_nf2=11)]
Taylor Fritz --> [PartidoTenis(fecha=datetime.date(2020, 12, 2), jugador1='Carlos Alcaraz', jugador2='Taylor Fritz', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=13, errores_nf2=8), PartidoTenis(fecha=datetime.date(2017, 4, 20), jugador1='Vasek Pospisil', jugador2='Taylor Fritz', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=10, errores_nf2=7)]
Andrey Rublev --> [PartidoTenis(fecha=datetime.date(2017, 3, 16), jugador1='Andrey Rublev', jugador2='Quentin Halys', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=19, errores_nf2=7), PartidoTenis(fecha=datetime.date(2011, 1, 12), jugador1='Andrey Rublev', jugador2='Roberto Bautista Agut', superficie='Hierba', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=19, errores_nf2=6), PartidoTenis(fecha=datetime.date(2016, 1, 26), jugador1='Novak Djokovic', jugador2='Andrey Rublev', superficie='Dura', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=11, errores_nf2=17)]
Felix Auger-Aliassime --> [PartidoTenis(fecha=datetime.date(2011, 11, 4), jugador1='Rafael Nadal', jugador2='Felix Auger-Aliassime', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=0, errores_nf2=20), PartidoTenis(fecha=datetime.date(2016, 11, 20), jugador1='Felix Auger-Aliassime', jugador2='Stefanos Tsitsipas', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2)], errores_nf1=18, errores_nf2=4), PartidoTenis(fecha=datetime.date(2015, 2, 15), jugador1='Dominic Thiem', jugador2='Felix Auger-Aliassime', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=3, errores_nf2=17)]
Vasek Pospisil --> [PartidoTenis(fecha=datetime.date(2020, 1, 24), jugador1='Tomas Martin Etcheverry', jugador2='Vasek Pospisil', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=11), PartidoTenis(fecha=datetime.date(2017, 4, 20), jugador1='Vasek Pospisil', jugador2='Taylor Fritz', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=10, errores_nf2=7), PartidoTenis(fecha=datetime.date(2018, 7, 20), jugador1='Vasek Pospisil', jugador2='Ben Shelton', superficie='Hierba', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=2, errores_nf2=17)]
Alex Molcan --> [PartidoTenis(fecha=datetime.date(2012, 7, 21), jugador1='Pavel Kotov', jugador2='Alex Molcan', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=17, errores_nf2=12), PartidoTenis(fecha=datetime.date(2010, 9, 1), jugador1='Matteo Berrettini', jugador2='Alex Molcan', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=13, errores_nf2=9), PartidoTenis(fecha=datetime.date(2014, 7, 10), jugador1='Alex Molcan', jugador2='Matteo Berrettini', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=6, errores_nf2=9)]
Nick Kyrgios --> [PartidoTenis(fecha=datetime.date(2014, 3, 26), jugador1='Nick Kyrgios', jugador2='Federico Coria', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=8, errores_nf2=7), PartidoTenis(fecha=datetime.date(2012, 10, 24), jugador1='Nick Kyrgios', jugador2='Richard Gasquet', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=16), PartidoTenis(fecha=datetime.date(2018, 3, 23), jugador1='Nick Kyrgios', jugador2='Ben Shelton', superficie='Tierra', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=5, errores_nf2=7)]
Daniel Elahi Galán --> [PartidoTenis(fecha=datetime.date(2017, 10, 12), jugador1='Daniel Elahi Galán', jugador2='Roberto Carballés Baena', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=9, errores_nf2=2)]
Borna Coric --> [PartidoTenis(fecha=datetime.date(2010, 5, 27), jugador1='Albert Ramos Vi±olas', jugador2='Borna Coric', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6)], errores_nf1=14, errores_nf2=13), PartidoTenis(fecha=datetime.date(2019, 4, 10), jugador1='Borna Coric', jugador2='Kamil Majchrzak', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=8, errores_nf2=5), PartidoTenis(fecha=datetime.date(2016, 2, 17), jugador1='Borna Coric', jugador2='Gael Monfils', superficie='Dura', resultado=[Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=7, errores_nf2=9)]
Jiri Lehecka --> [PartidoTenis(fecha=datetime.date(2020, 6, 16), jugador1='Soon Woo Kwon', jugador2='Jiri Lehecka', superficie='Hierba', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=15, errores_nf2=15), PartidoTenis(fecha=datetime.date(2012, 2, 13), jugador1='Novak Djokovic', jugador2='Jiri Lehecka', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=10, errores_nf2=5)]
Stefanos Tsitsipas --> [PartidoTenis(fecha=datetime.date(2014, 10, 28), jugador1='Stefanos Tsitsipas', jugador2='Roberto Bautista Agut', superficie='Hierba', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=1)], errores_nf1=18, errores_nf2=13), PartidoTenis(fecha=datetime.date(2017, 7, 29), jugador1='Stefanos Tsitsipas', jugador2='Casper Ruud', superficie='Dura', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=17, errores_nf2=12), PartidoTenis(fecha=datetime.date(2014, 10, 10), jugador1='Stefanos Tsitsipas', jugador2='Roger Federer', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=17, errores_nf2=20)]
Matteo Berrettini --> [PartidoTenis(fecha=datetime.date(2010, 9, 1), jugador1='Matteo Berrettini', jugador2='Alex Molcan', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=13, errores_nf2=9), PartidoTenis(fecha=datetime.date(2014, 7, 10), jugador1='Alex Molcan', jugador2='Matteo Berrettini', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=6, errores_nf2=9)]
Daniel Evans --> [PartidoTenis(fecha=datetime.date(2014, 9, 20), jugador1='Daniel Evans', jugador2='Ben Shelton', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=11, errores_nf2=7)]
Brandon Nakashima --> [PartidoTenis(fecha=datetime.date(2016, 8, 9), jugador1='Brandon Nakashima', jugador2='Tomas Machac', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=10)]
Tomas Machac --> [PartidoTenis(fecha=datetime.date(2016, 8, 9), jugador1='Brandon Nakashima', jugador2='Tomas Machac', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=16, errores_nf2=10)]
Cameron Norrie --> [PartidoTenis(fecha=datetime.date(2017, 12, 21), jugador1='Carlos Alcaraz', jugador2='Cameron Norrie', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=10, errores_nf2=15)]
Kamil Majchrzak --> [PartidoTenis(fecha=datetime.date(2019, 4, 10), jugador1='Borna Coric', jugador2='Kamil Majchrzak', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=8, errores_nf2=5)]
Pedro Cachin --> [PartidoTenis(fecha=datetime.date(2011, 12, 19), jugador1='Gael Monfils', jugador2='Pedro Cachin', superficie='Tierra', resultado=[Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=7, juegos_j2=6)], errores_nf1=16, errores_nf2=14), PartidoTenis(fecha=datetime.date(2012, 4, 20), jugador1='Pedro Cachin', jugador2='Lorenzo Musetti', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=8, errores_nf2=10)]
Pablo Carre±o Busta --> [PartidoTenis(fecha=datetime.date(2015, 10, 27), jugador1='Daniel Altmaier', jugador2='Pablo Carre±o Busta', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=12, errores_nf2=15)]
Frances Tiafoe --> [PartidoTenis(fecha=datetime.date(2014, 9, 20), jugador1='Frances Tiafoe', jugador2='John Isner', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=11, errores_nf2=11)]
Oscar Otte --> [PartidoTenis(fecha=datetime.date(2010, 4, 24), jugador1='Oscar Otte', jugador2='Roman Safiullin', superficie='Dura', resultado=[Parcial(juegos_j1=3, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=12, errores_nf2=4)]
Marc-Andrea Huesler --> [PartidoTenis(fecha=datetime.date(2012, 7, 19), jugador1='Marc-Andrea Huesler', jugador2='Ugo Humbert', superficie='Tierra', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=11, errores_nf2=7)]
Jannik Sinner --> [PartidoTenis(fecha=datetime.date(2015, 10, 25), jugador1='Jannik Sinner', jugador2='John Isner', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6)], errores_nf1=8, errores_nf2=11)]
Dominic Thiem --> [PartidoTenis(fecha=datetime.date(2014, 8, 19), jugador1='Dominic Thiem', jugador2='Rafael Nadal', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=0)], errores_nf1=20, errores_nf2=6), PartidoTenis(fecha=datetime.date(2014, 8, 19), jugador1='Dominic Thiem', jugador2='Rafael Nadal', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=2, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=0)], errores_nf1=20, errores_nf2=6), PartidoTenis(fecha=datetime.date(2010, 11, 22), jugador1='Dominic Thiem', jugador2='Andrey Rublev', superficie='Hierba', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=4, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=16, errores_nf2=16)]
Rafael Nadal --> [PartidoTenis(fecha=datetime.date(2011, 3, 13), jugador1='Roger Federer', jugador2='Rafael Nadal', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2)], errores_nf1=18, errores_nf2=20), PartidoTenis(fecha=datetime.date(2020, 5, 29), jugador1='Rafael Nadal', jugador2='Felix Auger-Aliassime', superficie='Sintética', resultado=[Parcial(juegos_j1=6, juegos_j2=4), Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=3)], errores_nf1=20, errores_nf2=13), PartidoTenis(fecha=datetime.date(2016, 3, 5), jugador1='Rafael Nadal', jugador2='Novak Djokovic', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=19, errores_nf2=9)]
Roger Federer --> [PartidoTenis(fecha=datetime.date(2018, 2, 3), jugador1='Roger Federer', jugador2='Diego Schwartzman', superficie='Hierba', resultado=[Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=2), Parcial(juegos_j1=6, juegos_j2=4)], errores_nf1=20, errores_nf2=8), PartidoTenis(fecha=datetime.date(2012, 1, 8), jugador1='Felix Auger-Aliassime', jugador2='Roger Federer', superficie='Tierra', resultado=[Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=1, juegos_j2=6), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=4, errores_nf2=20), PartidoTenis(fecha=datetime.date(2010, 9, 24), jugador1='Roger Federer', jugador2='Andrey Rublev', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=6, juegos_j2=1), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=20, errores_nf2=2)]
Roberto Bautista Agut --> [PartidoTenis(fecha=datetime.date(2016, 1, 17), jugador1='Rafael Nadal', jugador2='Roberto Bautista Agut', superficie='Dura', resultado=[Parcial(juegos_j1=7, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=7), Parcial(juegos_j1=3, juegos_j2=6)], errores_nf1=12, errores_nf2=19), PartidoTenis(fecha=datetime.date(2017, 11, 1), jugador1='Roberto Bautista Agut', jugador2='Felix Auger-Aliassime', superficie='Dura', resultado=[Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=0, juegos_j2=6), Parcial(juegos_j1=6, juegos_j2=1)], errores_nf1=18, errores_nf2=9), PartidoTenis(fecha=datetime.date(2010, 10, 15), jugador1='Casper Ruud', jugador2='Roberto Bautista Agut', superficie='Hierba', resultado=[Parcial(juegos_j1=6, juegos_j2=0), Parcial(juegos_j1=6, juegos_j2=3), Parcial(juegos_j1=0, juegos_j2=0)], errores_nf1=5, errores_nf2=17)]
EJERCICIO 14==================================================
Test de 'test_mayor_numero_dias_sin_jugar' jugador=Carlos Alcaraz
El mayor némero de días que el jugador Carlos Alcaraz ha estado sin jugar es 799
```
