from .hands import MatcherKey, K, Hands, RangeOrDiscrete
from .poker_iterator import PokerIterator
from .expansion_adapters import ExpansionAdapters
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
    adapters = ExpansionAdapters()

    def expand(self, combo: str) -> str:
        (match_key, qualifier) = self.hands.qualify(combo)
        pprint({ 'combo': combo, 'match_key': match_key, 'qualifier': qualifier })
        return self.expandDiscrete(match_key, combo) if qualifier == RangeOrDiscrete.DISCRETE else self.expandRange(combo)

    def expandRange(self, combo: str) -> list[str]:
        range = combo.split('-')
        combos = []
        match_keys = [] # debugging only, remove later
        for _combo in range:
            match_key = self.hands.getMatchKey(_combo)
            combos.append(self.expandDiscrete(match_key, _combo))
            match_keys.append(match_key) # debugging only
        print(f'expanding range = {range} with match_keys = {match_keys}')

    def expandDiscrete(self, match_key: MatcherKey, combo: str) -> list[str]:
        expansion = None

        if match_key == K.EXACT:
            expansion = self.adapters.exactSuited(combo)

        elif match_key == K.EXACT_SUITED:
            expansion = self.adapters.exactSuited(combo)

        elif match_key == K.ALL_COMBOS:
            expansion = self.adapters.allCombos(combo)

        elif match_key == K.ALL_GREATER_COMBOS:
            expansion = self.adapters.allGreaterCombos(combo)

        elif match_key == K.ALL_OFFSUIT_COMBOS:
            expansion = self.adapters.allOffsuitCombos(combo)

        elif match_key == K.ALL_SUITED_COMBOS:
            expansion = self.adapters.allSuitedCombos(combo)

        elif match_key == K.ALL_GREATER_OFFSUIT_COMBOS:
            expansion = self.adapters.allGreaterOffsuitCombos(combo)

        elif match_key == K.ALL_GREATER_SUITED_COMBOS:
            expansion = self.adapters.allGreaterSuitedCombos(combo)

        elif match_key == K.ALL_COMBOS_BOUNDED:
            expansion = self.adapters.allCombosBounded()

        elif match_key == K.ALL_OFFSUIT_COMBOS_BOUNDED:
            expansion = self.adapters.allOffsuitCombosBounded(combo)

        elif match_key == K.ALL_SUITED_COMBOS_BOUNDED:
            expansion = self.adapters.allSuitedCombosBounded(combo)

        elif match_key == K.ALL_SPECIFIC_SUITED_COMBOS_BOUNDED:
            expansion = self.adapters.allSpecificSuitedCombosBounded(combo)

        else:
            raise ValueError(f'unsupported match_key = {match_key} in .expandDiscrete, unable to find adapter')

        print(expansion)
        return expansion
