# iterator stop signal
TOP = '#'
ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A', TOP]

class PokerIterator:
    def top(self):
        return TOP

    def current(self):
        return ORDER[self.index]

    def __init__(self, start):
        try:
            self.index = ORDER.index(start)
        except:
            raise IndexError(f'card = {start} is not in 2-9TJQKA')

    def next(self):
        self.index += 1

    # other is a PokerIterator instance
    def __add__(self, other) -> str:
        return str(self.current()) + str(other.current())

    # gets upper bound for iteration if range was provided
    # c_top, d_top convention matches var names at callsite
    @staticmethod
    def getTops(ceiling: str = None) -> tuple[str, str]:
        if ceiling is None:
            return (TOP, TOP)
        [c_top, d_top] = list(ceiling)
        return (
            ORDER[ORDER.index(c_top) + 1],
            ORDER[ORDER.index(d_top) + 1]
        )

