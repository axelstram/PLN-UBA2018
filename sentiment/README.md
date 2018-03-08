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


### *Stopwords:*

* Curvas de aprendizaje:

Accuracy

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/acc_stopwords.png)

F1

![alt text](https://github.com/axelstram/PLN-UBA2018/blob/practico3/sentiment/images/f1_stopwords.png)


* Evaluación sobre Development:

SVM:

Sentiment P:
  Precision: 50.50% (101/200)
  Recall: 64.74% (101/156)
  F1: 56.74%
Sentiment N:
  Precision: 61.83% (115/186)
  Recall: 52.51% (115/219)
  F1: 56.79%
Sentiment NEU:
  Precision: 17.65% (6/34)
  Recall: 8.70% (6/69)
  F1: 11.65%
Sentiment NONE:
  Precision: 22.09% (19/86)
  Recall: 30.65% (19/62)
  F1: 25.68%
Accuracy: 47.63% (241/506)
Macro-Precision: 38.02%
Macro-Recall: 39.15%
Macro-F1: 38.57%

	P	N	NEU	NONE
P	101	28	6	21
N	56	115	16	32
NEU	26	23	6	14
NONE	17	20	6	19


