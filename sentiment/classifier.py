from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.stem.snowball import SpanishStemmer
import re



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

def createTweetTokenizerPipeline(clf):
        tweetTokenizer = TweetTokenizer()    
        spanishStemmer = SpanishStemmer()

        def tweet_tokenizer(sentence):
            return [spanishStemmer.stem(token) for token in tweetTokenizer.tokenize(sentence)]

        return Pipeline([
            ('vect', CountVectorizer(tokenizer=tweet_tokenizer)),
            ('clf', classifiers[clf]()),
        ])


def createNormalizationPipeline(clf):
        tweetTokenizer = TweetTokenizer()    

        def normalizator(sentence):
            urls = r'(?:https?\://t.co/[\w]+)'
            mentions = r'(?:@[^\s]+)'
            sentence = re.sub(urls, '', sentence)
            sentence = re.sub(mentions, '', sentence)
            
            vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

            for vowel in vowels:
                sentence = re.sub(r'(' + vowel + ')\1+', r'\1', sentence)

            return sentence


        return Pipeline([
            ('vect', CountVectorizer(tokenizer=normalizator)),
            ('clf', classifiers[clf]()),
        ])


class SentimentClassifier(object):

    def __init__(self, clf='svm', pipeline='default'):
        """
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        pipeline -- type of pipeline to use: 'default', 'binary', 'stopwords', 'tweet'

        """
        self._clf = clf
        self._pipeline = None

        if pipeline == 'default':
            self._pipeline = createDefaultPipeline(clf)
        elif pipeline == 'binary':
            self._pipeline = createBinaryCountPipeline(clf)
        elif pipeline == 'stopwords':
            self._pipeline = createStopwordsPipeline(clf)
        elif pipeline == 'tweet':
            self._pipeline = createTweetTokenizerPipeline(clf)
        elif pipeline == 'normalize':
            self._pipeline = createNormalizationPipeline(clf)


    def fit(self, X, y):
        self._pipeline.fit(X, y)

    def predict(self, X):
        return self._pipeline.predict(X)

    