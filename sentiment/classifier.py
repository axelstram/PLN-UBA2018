from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords


classifiers = {
    'maxent': LogisticRegression,
    'mnb': MultinomialNB,
    'svm': LinearSVC,
}

def createDefaultPipeline(clf):
        return Pipeline([
            ('vect', CountVectorizer()),
            ('clf', classifiers[clf]()),
        ])

def createBinaryCountPipeline(clf):
        return Pipeline([
            ('vect', CountVectorizer(binary=True)),
            ('clf', classifiers[clf]()),
        ])

def createStopwordsPipeline(clf):
        return Pipeline([
            ('vect', CountVectorizer(stop_words=stopwords.words('spanish'))),
            ('clf', classifiers[clf]()),
        ])


class SentimentClassifier(object):

    def __init__(self, clf='svm', pipeline='default'):
        """
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        pipeline -- type of pipeline to use: 'default', 'binary', 'stopwords'

        """
        self._clf = clf
        self._pipeline = None

        if pipeline == 'default':
            self._pipeline = createDefaultPipeline(clf)
        elif pipeline == 'binary':
            self._pipeline = createBinaryCountPipeline(clf)
        elif pipeline == 'stopwords':
            self._pipeline = createStopwordsPipeline(clf)    


    def fit(self, X, y):
        self._pipeline.fit(X, y)

    def predict(self, X):
        return self._pipeline.predict(X)

    