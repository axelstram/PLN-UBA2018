from collections import defaultdict
import random


class NGramGenerator(object):

    def __init__(self, model):
        """
        model -- n-gram model.
        """
        self._n = model._n

        # compute the probabilities
        probs = defaultdict(dict)

        empty_tuple = ()
        tokens_dict = {}

        if self._n == 1:
            for k, _ in model._count.items():
                if k is not empty_tuple:
                    k = k[0]
                    tokens_dict[k] = model.cond_prob(k)        

            probs[empty_tuple] = tokens_dict
        else:
            for k, _ in model._count.items():
                if k is not empty_tuple:
                    current_token = k[0]

                    if current_token == '</s>':
                        continue

                    next_tokens_dict = {}
                    next_tokens = model.next_tokens(current_token)

                    for t in next_tokens:
                        next_tokens_dict[t] = model.cond_prob(t, prev_tokens=(current_token,))

                    probs[(current_token,)] = next_tokens_dict

        self._probs = dict(probs)        

        # sort in descending order for efficient sampling
        self._sorted_probs = sorted_probs = {}
        # WORK HERE!!

    def generate_sent(self):
        """Randomly generate a sentence."""
        n = self._n

        sent = []
        prev_tokens = ['<s>'] * (n - 1)
        token = self.generate_token(tuple(prev_tokens))
        while token != '</s>':
            # WORK HERE!!
            pass

        return sent

    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.

        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        if not prev_tokens:
            prev_tokens = ()
        assert len(prev_tokens) == n - 1

        r = random.random()
        probs = self._sorted_probs[prev_tokens]
        # WORK HERE!!

        return token
