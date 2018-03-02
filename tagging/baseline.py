from collections import defaultdict


class BadBaselineTagger:

    def __init__(self, tagged_sents):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        """
        pass

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        return 'nc0s000'

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return True


class BaselineTagger:

    def __init__(self, tagged_sents, default_tag='nc0s000'):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        default_tag -- tag for unknown words.
        """
        self.word_to_most_freq_tag = word_to_most_freq_tag = defaultdict(str)
        self.word_to_tags = word_to_tags = defaultdict(dict)
        self.default_tag = default_tag
        
        for sent in tagged_sents:
            for word, tag in sent:
                word_to_tags[word][tag] = word_to_tags.get(word, {}).get(tag, 0) + 1
        
        for word, tags in word_to_tags.items():
            most_freq_tag = max(tags.items(), key=lambda x: x[1])[0]
            word_to_most_freq_tag[word] = most_freq_tag
        

    def tag(self, sent):
        """Tag a sentence.
        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.
        w -- the word.
        """
        if self.unknown(w):
            return self.default_tag
        
        return self.word_to_most_freq_tag[w]

    def unknown(self, w):
        """Check if a word is unknown for the model.
        w -- the word.
        """
        return (w not in self.word_to_tags)
