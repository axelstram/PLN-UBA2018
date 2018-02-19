# https://docs.python.org/3/library/collections.html
from collections import defaultdict
from functools import reduce
from math import log, inf
import math


class LanguageModel(object):

    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.

        sent -- the sentence as a list of tokens.
        """
        return 0.0

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        return -math.inf

    def log_prob(self, sents):
        result = 0.0
        for i, sent in enumerate(sents):
            lp = self.sent_log_prob(sent)
            if lp == -math.inf:
                return lp
            result += lp
        return result

    def cross_entropy(self, sents):
        log_prob = self.log_prob(sents)
        n = sum(len(sent) + 1 for sent in sents)  # count '</s>' events
        e = - log_prob / n
        return e

    def perplexity(self, sents):
        return math.pow(2.0, self.cross_entropy(sents))


class NGram(LanguageModel):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        assert n > 0
        self._n = n

        count = defaultdict(int)
        self._count = dict(count)
        self._sents = []
        
        for sent in sents:
            for i in range(n-1):
                sent = ['<s>'] + sent

            sent.append('</s>')

            self._sents.append(sent)

            for idx, token in enumerate(sent):

                tokens_tuple = (token,)
                
                for j in range(n):
                    if tokens_tuple not in self._count:
                        self._count[tokens_tuple] = 1
                    else:
                        self._count[tokens_tuple] += 1

                    next_token = sent[(idx + j + 1) % len(sent)]
                    tokens_tuple = tokens_tuple + (next_token,)

        empty_tuple = ()    
        
        if n == 1:
            self._count[empty_tuple] = sum(list(self._count.values()))
        

    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.

        tokens -- the n-gram or (n-1)-gram tuple.
        """
        return self._count.get(tokens, 0)

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """

        numerator = token

        if type(token) is not tuple:
            numerator = (token,)

        if prev_tokens is not None:
            numerator = prev_tokens + numerator

        if self._n == 1:
            denominator = ()
        else:
            denominator = prev_tokens

        if self._count.get(denominator, 0) == 0 and self._n > 1:
            return 0.0
        else:
            return self._count.get(numerator, 0) / self._count.get(denominator)



    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.

        sent -- the sentence as a list of tokens.
        """

        for i in range(self._n - 1):
            sent = ['<s>'] + sent

        sent.append('</s>')

        probs = []

        for idx, token in enumerate(sent):
            next_token = None

            for i in range(self._n - 1):
                next_token = sent[(idx + i + 1) % len(sent)]
                probs.append(self.cond_prob(next_token, prev_tokens=(token,)))

            if next_token is None:
                probs.append(self.cond_prob(token))

        return reduce(lambda x, y: x * y, probs, 1)

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        prob = self.sent_prob(sent)

        if prob == 0.0:
            return -inf
        else:    
            return log(prob, 2)

    def next_tokens(self, token):
        tokens = []

        for sent in self._sents:
            for idx, w in enumerate(sent):
                if w == token and w != '</s>':
                    next_token = sent[(idx + 1) % len(sent)]
                    tokens.append(next_token)

        return tokens

class AddOneNGram(NGram):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        # call superclass to compute counts
        super().__init__(n, sents)

        # compute vocabulary
        voc = set()

        for tup, _ in self._count.items():
            if tup is not ():
                for elem in tup:
                    if elem != '<s>':
                        voc.add(elem)
        
        self._voc = voc

        self._V = len(voc)  # vocabulary size

    def V(self):
        """Size of the vocabulary.
        """
        return self._V

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        if not prev_tokens:
            # if prev_tokens not given, assume 0-uple:
            prev_tokens = ()
        assert len(prev_tokens) == n - 1

        prev_tokens = tuple(prev_tokens)
        tokens = prev_tokens + (token,)
        tokens_count = float(self.count(tokens) + 1)
        prev_count = self.count(prev_tokens) + self._V
        return tokens_count / prev_count


class InterpolatedNGram(NGram):

    def __init__(self, n, sents, gamma=None, addone=True):

        self._gamma = gamma
        if gamma is None:
            len_held_out = int(0.1 * len(sents))
            development_data = sents[-len_held_out]
            sents = sents[0:len_held_out+1]
            self.gamma = self.gammaFromHeldOut(development_data)


        models = []
        for i in range(1, n + 1):
            if addone:
                models.append(AddOneNGram(i, sents))
            else:
                models.append(NGram(i, sents))

        self._ngram_models = models
        super().__init__(n, sents)



    def gammaFromHeldOut(self, data):
        #TODO
        return 1

    def count(self, tokens):
        return self._ngram_models[self._n-1].count(tokens)

    def cond_prob(self, token, prev_tokens=None):
        cond_ml = []        # maximum likelihood estimators
        lambdas = []        # calculo de lambdas
        for i in range(0,self._n - 1):
            if prev_tokens is None:
                prev_tokens_per_ngram = tuple()
            else:
                prev_tokens_per_ngram = prev_tokens

            cond_prob = self._ngram_models[self._n -i-1].cond_prob(token, prev_tokens_per_ngram)  #para cada modelo de ngramas calculo la condicional
            if cond_prob == -math.inf:
                cond_prob = 0
            cond_ml.append(cond_prob)

            current_lambda = (1 - sum(lambdas)) * self._ngram_models[self._n -(i+1)].count(prev_tokens[i:]) / (self._ngram_models[self._n -(i+1)].count(prev_tokens[i:]) + self._gamma)
            lambdas.append(current_lambda)

        cond_ml.append(self._ngram_models[0].cond_prob(token))
        lambdas.append(1 - sum(lambdas))

        prob = 0
        for i in range(len(cond_ml)):
            prob += lambdas[i] * cond_ml[i]

        return prob