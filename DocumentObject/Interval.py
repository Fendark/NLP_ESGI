class Interval(object):

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        if self.start > self.end:
            raise ValueError('Start "{}" must not be greater than end "{}"'.format(self.start, self.end))
        if self.start < 0:
            raise ValueError('Start "{}" must not be negative'.format(self.start))

    def __len__(self) -> int:
        return self.end - self.start

    def __eq__(self, other: 'Interval') -> bool:
        return self.start == other.start and self.end == other.end

    def __contains__(self, item: int) -> bool:
        return self.start <= item < self.end

    def __repr__(self) -> str:
        return 'Interval[{}, {}]'.format(self.start, self.end)

    def __str__(self):
        return repr(self)

    def intersection(self, other: 'Interval') -> 'Interval':
        """ Return the interval common to self and other """
        a, b = sorted((self, other))
        if a.end <= b.start:
            return Interval(self.start, self.start)
        return Interval(b.start, min(a.end, b.end))

    def overlaps(self, other: 'Interval') -> bool:
        """ Return True if there exists an interval common to self and other """
        a, b = sorted((self, other))
        return a.end > b.start

    def shift(self, i: int):
        self.start += i
        self.end += i

