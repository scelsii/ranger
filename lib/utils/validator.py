import re
from .hands import K, Hands


class Validator:
    hands = Hands()

    def isValid(self, combo: str):
        for pattern in self.hands.matchers.values():
            if re.compile(r"^" + pattern + r"$").match(combo) is not None:
                return True
        return False

    # matches ATdd, ATdd+
    def isSpecificSuitedCombo(self, combo: str):
        return self.hands.getMatchKey(combo) in [K.EXACT_SUITED, K.ALL_GREATER_SPECIFIC_SUITED_COMBOS]

    # checks for matching suit flags in 'JThh(+)'
    def isValidSpecificSuitedCombo(self, combo: str):
        [a, b] = combo[2:4]
        return self.isValid(combo) and a == b
