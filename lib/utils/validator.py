import re
from .hands import Hands


class Validator:
    hands = Hands()

    def isValid(self, combo: str):
        for pattern in self.hands.matchers.values():
            if re.compile(r"^" + pattern + r"$").match(combo) is not None:
                return True

        return False

    # checks for matching suit flags in 'JThh(+)'
    def isValidSpecificSuitedCombo(self, combo: str):
        [a, b] = combo[2:4]
        return self.isValid(combo) and a == b
