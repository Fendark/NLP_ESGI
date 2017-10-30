import nltk
nltk.download('gutenberg')
from nltk.corpus import gutenberg


class Interval():
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

class Sentence(Interval):
    def __init__(self, start, end):
        super().__init__(start, end)

class Tokenize(Interval):
    def __init__(self, start, end):
        super().__init__(start, end)

class Document():
    def __init__(self, document):
        self.tokens = list()

    # def fileReader(self):

if __name__ == "__main__":
    test = Sentence(2,3)
    print(test.start)