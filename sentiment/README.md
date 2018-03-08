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

## Tweet and feature weights:

Tweet: `@lorzagirl oye, que mi madre se le cortó la leche  y mirame, 1,85 XD, aunque algo enfermizo de pequeño. Ahora, lo de la leche X...`

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






# *Binary:*

## Curvas de aprendizaje:

### Accuracy

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/acc_binary.png)

### F1

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/f1_binary.png)


## Evaluación sobre Development:

### SVM:

Sentiment P:  
 - Precision: 54.55% (108/198)
 - Recall: 69.23% (108/156)
 - F1: 61.02% 

Sentiment N:  
 - Precision: 63.21% (122/193)
 - Recall: 55.71% (122/219)
 - F1: 59.22%

Sentiment NEU:  
 - Precision: 15.79% (6/38)
 - Recall: 8.70% (6/69)
 - F1: 11.21%  

Sentiment NONE:  
 - Precision: 24.68% (19/77)
 - Recall: 30.65% (19/62)
 - F1: 27.34%  

Accuracy: 50.40% (255/506)  
Macro-Precision: 39.56%  
Macro-Recall: 41.07%  
Macro-F1: 40.30%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    108    |     23     |      10      |      15      |
|     N      |    52     |     122    |      15      |      30      |
|    NEU     |    29     |     21     |      6       |      13      |
|    NONE    |    9      |     27     |      7       |      19      |



### MNB:

Sentiment P:  
 - Precision: 48.11% (127/264)
 - Recall: 81.41% (127/156)
 - F1: 60.48%

Sentiment N:  
 - Precision: 59.17% (142/240)
 - Recall: 64.84% (142/219)
 - F1: 61.87%

Sentiment NEU:  
 - Precision: 100.00% (0/0)
 - Recall: 0.00% (0/69)
 - F1: 0.00%

Sentiment NONE:  
 - Precision: 50.00% (1/2)
 - Recall: 1.61% (1/62)
 - F1: 3.12%

Accuracy: 53.36% (270/506)  
Macro-Precision: 64.32%  
Macro-Recall: 36.97%  
Macro-F1: 46.95%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    127    |     29     |      0       |      0       |
|     N      |    76     |     142    |      0       |      1       |
|    NEU     |    37     |     32     |      0       |      0       |
|    NONE    |    24     |     37     |      0       |      1       |



### MaxEnt:

Sentiment P:  
 - Precision: 51.98% (118/227)
 - Recall: 75.64% (118/156)
 - F1: 61.62%

Sentiment N:  
 - Precision: 58.88% (126/214)
 - Recall: 57.53% (126/219)
 - F1: 58.20%

Sentiment NEU:  
 - Precision: 12.50% (2/16)
 - Recall: 2.90% (2/69)
 - F1: 4.71%

Sentiment NONE:  
 - Precision: 26.53% (13/49)
 - Recall: 20.97% (13/62)
 - F1: 23.42%

Accuracy: 51.19% (259/506)  
Macro-Precision: 37.47%  
Macro-Recall: 39.26%  
Macro-F1: 38.35%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    118    |     28     |      4       |      6       |
|     N      |    65     |     126    |      6       |      22      |
|    NEU     |    29     |     30     |      2       |      8       |
|    NONE    |    15     |     30     |      4       |      13      |






# *Normalization:*

## Curvas de aprendizaje:

### Accuracy

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/acc_normalization.png)

### F1

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/f1_normalization.png)


## Evaluación sobre Development:

### SVM:

Sentiment P:  
 - Precision: 34.99% (134/383)
 - Recall: 85.90% (134/156)
 - F1: 49.72%

Sentiment N:  
 - Precision: 52.78% (38/72)
 - Recall: 17.35% (38/219)
 - F1: 26.12%

Sentiment NEU:  
 - Precision: 100.00% (0/0)
 - Recall: 0.00% (0/69)
 - F1: 0.00%

Sentiment NONE:  
 - Precision: 19.61% (10/51)
 - Recall: 16.13% (10/62)
 - F1: 17.70%

Accuracy: 35.97% (182/506)  
Macro-Precision: 51.84%  
Macro-Recall: 29.84%  
Macro-F1: 37.88%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    134    |     16     |      0       |      6       |
|     N      |    152    |     38     |      0       |      29      |
|    NEU     |    54     |     9      |      0       |      6       |
|    NONE    |    43     |     9      |      0       |      10      |



### MNB:

Sentiment P:  
 - Precision: 44.20% (61/138)
 - Recall: 39.10% (61/156)
 - F1: 41.50%

Sentiment N:  
 - Precision: 46.53% (154/331)
 - Recall: 70.32% (154/219)
 - F1: 56.00%

Sentiment NEU:  
 - Precision: 20.00% (2/10)
 - Recall: 2.90% (2/69)
 - F1: 5.06%

Sentiment NONE:  
 - Precision: 18.52% (5/27)
 - Recall: 8.06% (5/62)
 - F1: 11.24%

Accuracy: 43.87% (222/506)  
Macro-Precision: 32.31%  
Macro-Recall: 30.10%  
Macro-F1: 31.16%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    61     |     85     |      0       |      10      |
|     N      |    49     |     154    |      6       |      10      |
|    NEU     |    13     |     52     |      2       |      2       |
|    NONE    |    15     |     40     |      2       |      5       |



### MaxEnt:

Sentiment P:  
 - Precision: 38.10% (88/231)
 - Recall: 56.41% (88/156)
 - F1: 45.48%

Sentiment N:  
 - Precision: 49.72% (89/179)
 - Recall: 40.64% (89/219)
 - F1: 44.72%

Sentiment NEU:  
 - Precision: 100.00% (0/0)
 - Recall: 0.00% (0/69)
 - F1: 0.00%

Sentiment NONE:  
 - Precision: 17.71% (17/96)
 - Recall: 27.42% (17/62)
 - F1: 21.52%

Accuracy: 38.34% (194/506)  
Macro-Precision: 51.38%  
Macro-Recall: 31.12%  
Macro-F1: 38.76%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    88     |     48     |      0       |      20      |
|     N      |    84     |     89     |      0       |      46      |
|    NEU     |    31     |     25     |      0       |      13      |
|    NONE    |    28     |     17     |      0       |      17      |








# *Tweet:*

## Curvas de aprendizaje:

### Accuracy

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/acc_tweet.png)

### F1

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/f1_tweet.png)


## Evaluación sobre Development:

### SVM:

Sentiment P:  
 - Precision: 54.21% (103/190)
 - Recall: 66.03% (103/156)
 - F1: 59.54%

Sentiment N:  
 - Precision: 62.11% (118/190)
 - Recall: 53.88% (118/219)
 - F1: 57.70%

Sentiment NEU:  
 - Precision: 12.00% (6/50)
 - Recall: 8.70% (6/69)
 - F1: 10.08%

Sentiment NONE:  
 - Precision: 31.58% (24/76)
 - Recall: 38.71% (24/62)
 - F1: 34.78%

Accuracy: 49.60% (251/506)  
Macro-Precision: 39.97%  
Macro-Recall: 41.83%  
Macro-F1: 40.88%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    103    |     29     |      13      |      11      |
|     N      |    45     |     118    |      27      |      29      |
|    NEU     |    28     |     23     |      6       |      12      |
|    NONE    |    14     |     20     |      4       |      24      |



### MNB:

Sentiment P:  
 - Precision: 49.80% (126/253)
 - Recall: 80.77% (126/156)
 - F1: 61.61%

Sentiment N:  
 - Precision: 60.80% (152/250)
 - Recall: 69.41% (152/219)
 - F1: 64.82%

Sentiment NEU:  
 - Precision: 0.00% (0/1)
 - Recall: 0.00% (0/69)
 - F1: 0.00%

Sentiment NONE:  
 - Precision: 100.00% (2/2)
 - Recall: 3.23% (2/62)
 - F1: 6.25%

Accuracy: 55.34% (280/506)  
Macro-Precision: 52.65%  
Macro-Recall: 38.35%  
Macro-F1: 44.38%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    126    |     30     |      0       |      0       |
|     N      |    67     |     152    |      0       |      0       |
|    NEU     |    35     |     34     |      0       |      0       |
|    NONE    |    25     |     34     |      1       |      2       |



### MaxEnt:

Sentiment P:  
 - Precision: 54.63% (118/216)
 - Recall: 75.64% (118/156)
 - F1: 63.44%

Sentiment N:  
 - Precision: 66.35% (138/208)
 - Recall: 63.01% (138/219)
 - F1: 64.64%

Sentiment NEU:  
 - Precision: 15.79% (3/19)
 - Recall: 4.35% (3/69)
 - F1: 6.82%

Sentiment NONE:  
 - Precision: 26.98% (17/63)
 - Recall: 27.42% (17/62)
 - F1: 27.20%

Accuracy: 54.55% (276/506)  
Macro-Precision: 40.94%  
Macro-Recall: 42.61%  
Macro-F1: 41.75%  


| 			 | 	   P     |     N      |     NEU      |     NONE     |
|:----------:|:---------:|:----------:|:------------:|:------------:|
|     P      |    118    |     21     |      7       |      10      |
|     N      |    47     |     138    |      7       |      27      |
|    NEU     |    33     |     24     |      3       |      9       |
|    NONE    |    18     |     25     |      2       |      17      |



