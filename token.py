import nltk
nltk.download('gutenberg')
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


class Interval():
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

class Sentence(Interval):
    def __init__(self, start, end):
        super().__init__(start, end)

class Token(Interval):
    def __init__(self, start, end):
        super().__init__(start, end)

class Document():
    def __init__(self):
        self.text = gutenberg.raw('melville-moby_dick.txt')
        self.tokens = list()

    def getToken(self):
        #sentences = [sent for sent in sent_tokenize(moby_dick[117:300])]
        words = word_tokenize(self.text[117:300])
        return words

    def createTokens(self, words):
        offset = 0
        for i, w in enumerate(words):
            index = self.text[offset:].find(w)
            self.tokens[i] = Token(index, index + len(w))
            offset = index + len(w)

if __name__ == "__main__":
    test = Sentence(2,3)
    print(test.start)