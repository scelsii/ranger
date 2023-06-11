from .hands import MatcherKey, K, Hands, RangeOrDiscrete
from .poker_iterator import PokerIterator
from .expansion_adapters import ExpansionAdapters
from pprint import pprint

H = Hands()
A = ExpansionAdapters()

class Expansion:
    def __init__(self, expansion):
        self._expansion = expansion

    def __getitem__(self):
        return self._expansion

    def formatForInput(self):
        return ','.join(self._expansion)

class Expander:
    """
    given a range of hands in possibly shorthand notation,
    return a list of discrete hands for ps_eval fn

    [
        22, 33, ... AA,\n
        7s6s, 8s7s, ... AsKs (and all other suited combos),\n
        QcJd, KcQd, ... AcKd (etc),\n
        KsJs, AsQs, KdJd, ... AhQh (etc)\n
    ]
    """

    def expand(self, combo: str, debug=False) -> Expansion:
        (match_key, qualifier) = H.qualify(combo)
        if debug:
            pprint({
                'combo': combo,
                'match_key': match_key,
                'qualifier': qualifier
            })
        return Expansion(self.expandWithAdapter(match_key, combo))

    def expandWithAdapter(self, match_key: MatcherKey, combo: str) -> list[str]:
        expansion = None

        if match_key == K.EXACT:
            expansion = A.exact(combo)

        elif match_key == K.EXACT_SUITED:
            expansion = A.exactSuited(combo)

        elif match_key == K.ALL_COMBOS:
            expansion = A.allCombos(combo)

        elif match_key == K.ALL_GREATER_COMBOS:
            expansion = A.allGreaterCombos(combo)

        elif match_key == K.ALL_OFFSUIT_COMBOS:
            expansion = A.allOffsuitCombos(combo)

        elif match_key == K.ALL_SUITED_COMBOS:
            expansion = A.allSuitedCombos(combo)

        elif match_key == K.ALL_GREATER_OFFSUIT_COMBOS:
            expansion = A.allGreaterOffsuitCombos(combo)

        elif match_key == K.ALL_GREATER_SUITED_COMBOS:
            expansion = A.allGreaterSuitedCombos(combo)

        elif match_key == K.ALL_GREATER_SPECIFIC_SUITED_COMBOS:
            expansion = A.allGreaterSpecificSuitedCombos(combo)

        elif match_key == K.ALL_COMBOS_BOUNDED:
            expansion = A.allCombosBounded(combo)

        elif match_key == K.ALL_OFFSUIT_COMBOS_BOUNDED:
            expansion = A.allOffsuitCombosBounded(combo)

        elif match_key == K.ALL_SUITED_COMBOS_BOUNDED:
            expansion = A.allSuitedCombosBounded(combo)

        elif match_key == K.ALL_SPECIFIC_SUITED_COMBOS_BOUNDED:
            expansion = A.allSpecificSuitedCombosBounded(combo)

        else:
            raise ValueError(f'unsupported match_key = {match_key} in .expandDiscrete, unable to find adapter')

        return expansion

