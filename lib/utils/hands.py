import re

from enum import Enum
from typing import Literal

"""hand type regexes"""
class R(Enum):
    NUMBER_OR_FACE_CARD = r"[2-9TJQKA]{1}"
    SUIT = r"[hdcs]{1}"
    OFFSUIT = r"o"
    SUITED = r"s"
    ALL_GREATER_COMBOS = r"\+"
    RANGE_OF_HANDS = r"\-"

"""matcher keys"""
class K(Enum):
    EXACT = 'EXACT'
    EXACT_SUITED = 'EXACT_SUITED'
    ALL_COMBOS = 'ALL_COMBOS'
    ALL_OFFSUIT_COMBOS = 'ALL_OFFSUIT_COMBOS'
    ALL_SUITED_COMBOS = 'ALL_SUITED_COMBOS'
    ALL_GREATER_OFFSUIT_COMBOS = 'ALL_GREATER_OFFSUIT_COMBOS'
    ALL_GREATER_SUITED_COMBOS = 'ALL_GREATER_SUITED_COMBOS'
    ALL_COMBOS_BOUNDED = 'ALL_COMBOS_BOUNDED'
    ALL_OFFSUIT_COMBOS_BOUNDED = 'ALL_OFFSUIT_COMBOS_BOUNDED'
    ALL_SUITED_COMBOS_BOUNDED = 'ALL_SUITED_COMBOS_BOUNDED'
    ALL_SPECIFIC_SUITED_COMBOS_BOUNDED = 'ALL_SPECIFIC_SUITED_COMBOS_BOUNDED'

"""categories"""
class C(Enum):
    EXACT = 'EXACT'
    BOUNDED = 'BOUNDED'
    UNBOUNDED = 'UNBOUNDED'

class RangeOrDiscrete(Enum):
    DISCRETE = 'DISCRETE'
    RANGE = 'RANGE'

# custom types for enums
MatcherKey = Literal[
    K.EXACT,
    K.EXACT_SUITED,
    K.ALL_COMBOS,
    K.ALL_OFFSUIT_COMBOS,
    K.ALL_SUITED_COMBOS,
    K.ALL_GREATER_OFFSUIT_COMBOS,
    K.ALL_GREATER_SUITED_COMBOS,
    K.ALL_COMBOS_BOUNDED,
    K.ALL_OFFSUIT_COMBOS_BOUNDED,
    K.ALL_SUITED_COMBOS_BOUNDED,
    K.ALL_SPECIFIC_SUITED_COMBOS_BOUNDED,
]

ShorthandCategory = Literal[
    C.EXACT,
    C.BOUNDED,
    C.UNBOUNDED,
]

ExpanderQualifier = Literal[
    RangeOrDiscrete.DISCRETE,
    RangeOrDiscrete.RANGE
]

class Hands:
    matchers = {
        """AdTd"""
        [K.EXACT]:
            R.NUMBER_OR_FACE_CARD
            + R.SUIT
            + R.NUMBER_OR_FACE_CARD
            + R.SUIT,

        """ATdd"""
        [K.EXACT_SUITED]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.SUIT
            + R.SUIT,

        """KK"""
        [K.ALL_COMBOS]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD,

        """QTo"""
        [K.ALL_OFFSUIT_COMBOS]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.OFFSUIT,

        """QTs"""
        [K.ALL_SUITED_COMBOS]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.SUITED,

        """76+"""
        [K.ALL_GREATER_OFFSUIT_COMBOS]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.OFFSUIT
            + R.ALL_GREATER_COMBOS,

        """76s+"""
        [K.ALL_GREATER_SUITED_COMBOS]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.SUITED
            + R.ALL_GREATER_COMBOS,

        """54-T9"""
        [K.ALL_COMBOS_BOUNDED]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.RANGE_OF_HANDS
            + R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD,

        """54-T9o"""
        [K.ALL_OFFSUIT_COMBOS_BOUNDED]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.RANGE_OF_HANDS
            + R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.OFFSUIT,

        """54-T9s"""
        [K.ALL_SUITED_COMBOS_BOUNDED]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.RANGE_OF_HANDS
            + R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.SUITED,

        """54-T9cc"""
        [K.ALL_SPECIFIC_SUITED_COMBOS_BOUNDED]:
            R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.RANGE_OF_HANDS
            + R.NUMBER_OR_FACE_CARD
            + R.NUMBER_OR_FACE_CARD
            + R.SUIT
            + R.SUIT,

        # need support for 54cc-T9cc? no it's clunky
        # also not supporting 54o-87o / 54s-87s
        # should throw validation error on these
        # and suggest removing bottom hand qualifier
    }

    categories = {
        C.EXACT: [
            K.EXACT,
            K.EXACT_SUITED
        ],
        C.BOUNDED: [
            K.ALL_COMBOS_BOUNDED,
            K.ALL_SUITED_COMBOS_BOUNDED,
            K.ALL_OFFSUIT_COMBOS_BOUNDED,
            K.ALL_SPECIFIC_SUITED_COMBOS_BOUNDED
        ],
        C.UNBOUNDED: [
            K.ALL_COMBOS,
            K.ALL_OFFSUIT_COMBOS,
            K.ALL_SUITED_COMBOS,
            K.ALL_GREATER_OFFSUIT_COMBOS,
            K.ALL_GREATER_SUITED_COMBOS
        ]
    }

    def isMatch(self, m: re.Pattern, combo: str) -> bool:
        return re.compile(r'^' + m + r'$').match(combo)

    def getMatchKey(self, combo: str) -> MatcherKey:
        for k, m in self.matchers.items():
            if self.isMatch(m, combo):
                return k

    def getCategory(self, combo: str) -> ShorthandCategory:
        match_key = self.getMatchKey(self, combo)
        for c, k in self.categories.items():
            if match_key in k:
                return c

    def getRangeOrDiscrete(self, combo: str) -> ExpanderQualifier:
        category = self.getCategory(combo)
        return RangeOrDiscrete.DISCRETE if category == C.EXACT else RangeOrDiscrete.RANGE
