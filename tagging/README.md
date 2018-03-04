Trabajo Práctico 2
==================


Ejercicio 1:
============

- Basic Statistics:

* Sents: 17378
* Tokens: 517194
* Words: 46501
* Tags: 85


- Most Frequent POS Tags:

|   Tag    | Frecuencia | Porcentaje |         5 Palabras mas frecuentes         |     significado    |
|:--------:|:----------:|:----------:|:-----------------------------------------:|:------------------:|
|  sp000   |   79884    |   15.45 %  |           (de, en, a, del, con)           |	   Preposition	  |
| nc0s000  |   63452    |   12.27 %  |  (presidente, equipo, partido, país, año) |	   Common noun	  |
|  da0000  |   54549    |   10.55 %  |           (la, el, los, las, El)          | 	   Article		  |
|  aq0000  |   33906    |   6.56 %   |    (pasado, gran, mayor, nuevo, próximo)  |	   Adjective	  |
|    fc    |   30147    |   5.83 %   |                    (,)                    |	   Comma		  |
| np00000  |   29111    |   5.63 %   | (Gobierno, España, PP, Barcelona, Madrid) |	   Proper noun    |
| nc0p000  |   27736    |   5.36 %   |  (años, millones, personas, países, días) |     Common noun    |
|    fp    |   17512    |   3.39 %   |                    (.)                    |     Period         |
|    rg    |   15336    |   2.97 %   |        (más, hoy, también, ayer, ya)      |     Adverb         |
|    cc    |   15023    |   2.90 %   |           (y, pero, o, Pero, e)           |	   Conjunction    |


- Word Ambiguity Levels:

| ambiguity  | words     |     %      |              top 5                 |
|:----------:|:---------:|:----------:|:----------------------------------:|
|     1      |   43972   |   94.56 %  |        (,, con, por, su, El)       |
|     2      |   2318    |   4.98 %   |         (el, en, y, ", los)        |
|     3      |    180    |   0.39 %   |         (de, la, ., un, no)        |
|     4      |    23     |   0.05 %   |      (que, a, dos, este, fue)      |
|     5      |     5     |   0.01 %   | (mismo, cinco, medio, ocho, vista) |
|     6      |     3     |   0.01 %   |          (una, como, uno)          |					
|     7      |     0     |    0.0 %   |              ()                    |					
|     8      |     0     |    0.0 %   |              ()                    |					
|     9      |     0     |    0.0 %   |              ()                    |




Ejercicio 2:
============


- BadBaselineTagger:

* Global Score: 12.65 %
* Score sobre palabras desconocidas: 0.00%
* Score sobre palabras conocidas: 12.65%

Matriz de confusión


|  g\m    |  sp000  | nc0s000 | da0000  | aq0000  |   fc    | nc0p000 |   rg    | np00000 |   fp    |   cc    |
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|  sp000  |    -    |  14.39  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| nc0s000 |    -    |  12.65  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| da0000  |    -    |   9.70  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| aq0000  |    -    |   7.28  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
|   fc    |    -    |   5.85  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| nc0p000 |    -    |   5.53  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
|   rg    |    -    |   3.73  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| np00000 |    -    |   3.58  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
|   fp    |    -    |   3.55  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
|   cc    |    -    |   3.41  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |



- BaselineTagger:

* Global Score: 87.57%
* Score sobre palabras desconocidas: 95.25%
* Score sobre palabras conocidas: 18.01%

Matriz de confusión


|  g\m    |  sp000  | nc0s000 | da0000  | aq0000  |   fc    | nc0p000 |   rg    | np00000 |   fp    |   cc    |
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|  sp000  |  14.28  |  0.05   |    -    |    -    |    -    |    -    |  0.01   |    -    |    -    |    -    |
| nc0s000 |    -    |  12.22  |    -    |  0.25   |    -    |    -    |  0.03   |    -    |    -    |    -    |
| da0000  |    -    |  0.15   |  9.54   |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| aq0000  |  0.01   |  2.05   |    -    |  4.84   |    -    |  0.13   |    -    |    -    |    -    |    -    |
|   fc    |    -    |    -    |    -    |    -    |  5.85   |    -    |    -    |    -    |    -    |    -    |
| nc0p000 |    -    |  1.24   |    -    |  0.20   |    -    |  4.09   |    -    |    -    |    -    |    -    |
|   rg    |  0.02   |  0.31   |    -    |  0.04   |    -    |    -    |  3.27   |    -    |    -    |  0.02   |
| np00000 |    -    |  2.05   |    -    |    -    |    -    |    -    |    -    |  1.52   |    -    |    -    |
|   fp    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |  3.55   |    -    |
|   cc    |    -    |  0.01   |    -    |    -    |    -    |    -    |  0.05   |    -    |    -    |  3.34   |



Ejercicio 3:
============

Se implementaron las clases "NPrevTags" y "PrevWord", y las funciones "word_lower", "word_istitle", "word_isupper", "word_isdigit", en el archivo features.py


Ejercicio 4:
============

Los experimentos se corrieron en una CPU Intel i5-4690

**Clasificador "LinearSVC"**:

- n = 1:
* Accuracy: 94.11% / 0.00% / 94.11%
* Tiempo de entrenamiento: 4:32 mins
* Tiempo de evaluación: 24 segs

- n = 2:
* Accuracy: 92.43% / 0.00% / 92.43%
* Tiempo de entrenamiento: 5:40 mins
* Tiempo de evaluación: 25 segs

- n = 3:
* Accuracy: 92.27% / 0.00% / 92.27%
* Tiempo de entrenamiento: 6:52 mins
* Tiempo de evaluación: 25 segs

- n = 4:
* Accuracy: 92.13% / 0.00% / 92.13%
* Tiempo de entrenamiento: 9:40 mins
* Tiempo de evaluación: 26 segs
