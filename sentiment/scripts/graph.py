import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("darkgrid")

df = pd.read_csv('curve_f1_stopwords.csv')

n = df['n'].as_matrix()
acc_svm = df['f1_svm'].as_matrix()
acc_maxent = df['f1_maxent'].as_matrix()
acc_mnb = df['f1_mnb'].as_matrix()

plt.xlabel('n')
plt.ylabel('f1')
plt.title('Stopwords')

f = plt.plot(n, acc_svm)
f = plt.plot(n, acc_maxent)
f = plt.plot(n, acc_mnb)
plt.legend(['svm','maxnet','mnb'])

f = f[0].get_figure()

f.savefig('f1_stopwords.png')

plt.gcf().clear()