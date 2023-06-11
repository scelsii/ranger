# iterator stop signal
TOP = '#'
TEN_OR_FACE_CARD = 'TJQKA'
ORDER = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A', TOP]

class PokerIterator:
    def top(self):
        return TOP

    def current(self):
        return ORDER[self.index]

    def __init__(self, start):
        try:
            start = int(start) if start not in TEN_OR_FACE_CARD else start
            self.index = ORDER.index(start)
        except:
            raise IndexError(f'card {start} is not in 2-9TJQKA')

    def next(self):
        self.index += 1

    # other is a PokerIterator instance
    def __add__(self, other) -> str:
        return str(self.current()) + str(other.current())

    @staticmethod
    # gets upper bound for iteration if range was provided
    # eg, 22-77 should set top at 88
    # if ceiling is none, iterate all the way to 'A'
    def getTops(ceiling: str = None) -> tuple[str, str]:
        if ceiling is None:
            return (TOP, TOP)
        else:
            [c_top, d_top] = list(ceiling)
            return (
                ORDER.index(c_top) + 1,
                ORDER.index(d_top) + 1
            )

