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
