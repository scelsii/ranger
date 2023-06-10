from .hands import K, MatcherKey, Hands, RangeOrDiscrete
from .order import Order
from pprint import pprint

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
        (match_key, qualifier) = self.hands.qualify(combo)
        pprint({ 'combo': combo, 'match_key': match_key, 'qualifier': qualifier })
        return self.expandDiscrete(match_key, combo) if qualifier == RangeOrDiscrete.DISCRETE else self.expandRange(combo)

    def expandRange(self, combo: str) -> str:
        range = combo.split('-')
        combos = []
        for _combo in range:
            match_key = self.hands.getMatchKey(_combo)
            combos.append(self.expandDiscrete(match_key, _combo))
        # return ','.join(combos)

    def expandDiscrete(self, match_key: MatcherKey, combo: str):
        print(f'expanding combo = {combo} with match_key = {match_key}')
