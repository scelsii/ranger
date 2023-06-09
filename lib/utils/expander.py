from .hands import Hands, RangeOrDiscrete
from order import Order

class Expander:
    """
    given a range of hands in possibly shorthand notation,
    return a list of discrete hands for ps_eval fn

    eg 22+, 76s+, QJ+, KJs should expand to

    [
        22, 33, ... AA,
        7s6s, 8s7s, ... AsKs (and all other suited combos),
        QcJd, KcQd, ... AcKd (etc),
        KsJs, AsQs, KdJd, ... AhQh (etc)
    ]
    """

    hands = Hands()
    order = Order()

    def expand(self, combo: str) -> str:
        """
        steps (assume hand is validated)
        - get qualifier: 'RANGE' | 'DISCRETE'
        - plug expansion adapters into top-level .expand method
        """

        qualifier = self.hands.getRangeOrDiscrete(combo)
        return self.expandDiscrete(combo) if qualifier == RangeOrDiscrete.DISCRETE else self.expandRange(combo)

    def expandDiscrete():
        pass

    def expandRange():
        pass
