# https://docs.python.org/3/library/collections.html
from collections import defaultdict
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
        
        for sent in sents:
            for i in range(n-1):
                sent = ['<s>'] + sent

            sent.append('</s>')

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
        # WORK HERE!!

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        # WORK HERE!!
