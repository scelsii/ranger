# iterator stop signal
TOP = '#'
TEN_OR_FACE_CARD = 'TJQKA'

class PokerIterator:
    _order = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A', TOP]

    def top(self):
        return TOP

    def current(self):
        return self._order[self.index]

    def __init__(self, start):
        try:
            start = int(start) if start not in TEN_OR_FACE_CARD else start
            self.index = self._order.index(start)
        except:
            raise IndexError(f'card {start} is not in 2-9TJQKA')

    def next(self):
        self.index += 1

    # other is a PokerIterator instance
    def __add__(self, other) -> str:
        return str(self.current()) + str(other.current())
