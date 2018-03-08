Trabajo Práctico 3
==================


Ejercicio 1:
============

### InterTASS statistics:

* Total amount of tweets: 1008
* Tweets with [P] polarity: 318
* Tweets with [N] polarity: 418
* Tweets with [NEU] polarity: 133
* Tweets with [NONE] polarity: 139

### GeneralTASS statistics:

* Total amount of tweets: 7219
* Tweets with [P] polarity: 1232
* Tweets with [N] polarity: 1335
* Tweets with [NEU] polarity: 670
* Tweets with [NONE] polarity: 1483




Ejercicio 2:
============

Para este ejercicio se modificaron los archivos classifier.py, curve.py y train.py para que tomen un parámetro adicional '-p', el cuál representa el tipo de pipelina a utilizar: 'default', 'binary', 'stopwords', 'tweet' o 'normalization'.

Se implementaron las siguientes mejoras: Mejor Tokenizer (tweet), Binarización de conteos (binary), Normalización de tweets (normalization) y Filtrado de Stopwords (stopwords).



# *Stopwords:*

## Curvas de aprendizaje:

### Accuracy

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/acc_stopwords.png)

### F1

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/f1_stopwords.png)


## Evaluación sobre Development:

### SVM:

Sentiment P:  
 - Precision: 50.50% (101/200)  
 - Recall: 64.74% (101/156)  
 - F1: 56.74%  

Sentiment N:  
 - Precision: 61.83% (115/186)  
 - Recall: 52.51% (115/219)  
 - F1: 56.79%

Sentiment NEU:  
 - Precision: 17.65% (6/34)  
 - Recall: 8.70% (6/69)  
 - F1: 11.65%  

Sentiment NONE:  
 - Precision: 22.09% (19/86)  
 - Recall: 30.65% (19/62)  
 - F1: 25.68%  

Accuracy: 47.63% (241/506)  
Macro-Precision: 38.02%  
Macro-Recall: 39.15%  
Macro-F1: 38.57%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    101    |     28     |      6       |      21      |
|     N      |    56     |     115    |      16      |      32      |
|    NEU     |    26     |     23     |      6       |      14      |
|    NONE    |    17     |     20     |      6       |      19      |



### MNB:

Sentiment P:  
 - Precision: 43.88% (129/294)
 - Recall: 82.69% (129/156)
 - F1: 57.33%

Sentiment N:  
 - Precision: 60.71% (119/196)
 - Recall: 54.34% (119/219)
 - F1: 57.35%

Sentiment NEU:  
 - Precision: 20.00% (1/5)
 - Recall: 1.45% (1/69)
 - F1: 2.70% 

Sentiment NONE:  
 - Precision: 54.55% (6/11)
 - Recall: 9.68% (6/62)
 - F1: 16.44%  

Accuracy: 50.40% (255/506)  
Macro-Precision: 44.78%  
Macro-Recall: 37.04%  
Macro-F1: 40.55%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    129    |     24     |      1       |      2       |
|     N      |    97     |     119    |      2       |      1       |
|    NEU     |    41     |     25     |      1       |      2       |
|    NONE    |    27     |     28     |      1       |      6       |



### MaxEnt:

Sentiment P:  
 - Precision: 48.71% (113/232)
 - Recall: 72.44% (113/156)
 - F1: 58.25%

Sentiment N:  
 - Precision: 61.84% (128/207)
 - Recall: 58.45% (128/219)
 - F1: 60.09%

Sentiment NEU:  
 - Precision: 21.43% (3/14)
 - Recall: 4.35% (3/69)
 - F1: 7.23%

Sentiment NONE:  
 - Precision: 30.19% (16/53)
 - Recall: 25.81% (16/62)
 - F1: 27.83%

Accuracy: 51.38% (260/506)  
Macro-Precision: 40.54%  
Macro-Recall: 40.26%  
Macro-F1: 40.40%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    113    |     29     |      2       |      12      |
|     N      |    66     |     128    |      6       |      19      |
|    NEU     |    31     |     29     |      3       |      6       |
|    NONE    |    22     |     21     |      3       |      16      |


## Maxent most relevant features:

N:
* portada enhorabuena gracias buena feliz ([-1.72087574 -1.61411835 -1.51477759 -1.41222876 -1.41042154])
* peor corrupción recortes muertos triste ([ 1.78473314  1.81873048  1.91682375  1.9907607   2.4762817 ])

NEU:
* parados enhorabuena puedes tres felicidades ([-1.150014   -1.03717982 -0.91364664 -0.89044434 -0.86144292])
* gana decidirán vicepresidenta broma expectación ([ 1.24276137  1.26878577  1.27755031  1.32713174  1.34644755])

NONE:
* gracias feliz interesante gran mal ([-1.90620358 -1.85716243 -1.82737902 -1.74255757 -1.67852596])
* jugar sesión reunión 300 portada ([ 1.20167375  1.22048875  1.26525041  1.26773236  2.42187334])

P:
* triste portada urdangarin griñan culpa ([-1.64422166 -1.59682195 -1.36776681 -1.35668773 -1.35352684])
* genial homenaje gracias felicidades enhorabuena ([ 1.9467743   1.99712246  2.24202844  2.32473932  2.58299904])

##Tweet and feature weights:

`@lorzagirl oye, que mi madre se le cortó la leche  y mirame, 1,85 XD, aunque algo enfermizo de pequeño. Ahora, lo de la leche X...`

|   Token   |                         Weights
|:---------:|:---------------------------------------------------------------------:|
|   85      |          [-0.09302526 -0.10401111  0.3916153  -0.19723845]            |
|  ahora    |          [-0.19539356 -0.03174294  0.1679441   0.0749638 ]            |
|  aunque   |          [ 0.06743831  0.60623606 -0.66085854 -0.14723992]            |
|  leche    |          [ 0.30859743 -0.18323434 -0.37897767  0.16392086]            |
|  madre    |          [-0.02086725 -0.04935246  0.13901071 -0.12215556]            |
|  oye      |          [-0.15031295  0.11646489  0.16988609 -0.01069041]            |
|  pequeño  |          [ 0.6629558  -0.45229228 -0.53835658 -0.04209061]            |
|  xd       |          [-0.28428317  0.7002109   0.18759896 -0.40002533]            |
