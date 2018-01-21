from DocumentObject.Interval import Interval


class Token(Interval):
    def __init__(self, document, start: int, end: int, pos: str = None, shape: str = None, text: str = None, label: str = None):
        Interval.__init__(self, start, end)
        self._doc = document
        self._pos = pos
        self._shape = shape
        self._text = text
        self._label = label
    def __getitem__(self, item):
        return None

    def __repr__(self):
        return 'Token({}, {}, {}, {})'.format(self._text, self.start, self.end, self._pos)


