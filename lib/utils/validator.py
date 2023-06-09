import re
from .hands import Hands

"""
combo: shorthand hand accepted by ps_eval
eg., 22+, 76s, QThh, AdTd, 56s-T9s, QJo
"""

class Validator:
    hands = Hands()

    def is_valid(self, combo: str):
        for pattern in self.hands.matchers.values():
            if re.compile(r"^" + pattern + r"$").match(combo) is not None:
                return True

        return False
