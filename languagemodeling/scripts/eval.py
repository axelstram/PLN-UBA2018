"""Evaulate a language model using a test set.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Language model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import math

from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import gutenberg


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the model
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    # load the data
    pattern = r'''(?x)    
    (?:\d{1,3}(?:\.\d{3})+)
    | (?:[Ss]r\.|[Ss]ra\.|art\.) 
    | (?:[A-Z]\.)+       
    | \w+(?:-\w+)*        
    | \$?\d+(?:\.\d+)?%?  
    | \.\.\.            
    | [][.,;"'?():-_`]  
    '''

    tokenizer = RegexpTokenizer(pattern)
    corpus = PlaintextCorpusReader('.', 'ML.txt', word_tokenizer=tokenizer)
    sents = corpus.sents()

    training_sents = sents[:int(0.9*len(sents))]
    test_sents = sents[int(0.9*len(sents)):]


    # compute the cross entropy
    log_prob = 0.0

    for i, sent in enumerate(sents):
        lp = model.sent_log_prob(sent)
        if lp == -math.inf:
            break
        log_prob += lp

    n = sum(len(sent) + 1 for sent in test_sents)  # count '</s>' event
    e = - log_prob / n
    p = math.pow(2.0, e)

    print('Log probability: {}'.format(log_prob))
    print('Cross entropy: {}'.format(e))
    print('Perplexity: {}'.format(p))
