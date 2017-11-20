from DocumentObject.Interval import Interval

class Sentence(Interval):

    def __init__(self, document, start: int, end: int):
        Interval.__init__(self, start, end)
        self._doc = document
        self._tokens = list()

    def __repr__(self):
        return 'Sentence({}, {})'.format(self.start, self.end)