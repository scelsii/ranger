from .utils.expander import Expander
from .utils.validator import Validator

class PsEvalInput:
    expander = Expander()
    validator = Validator()

    def preprocess(self, input: str) -> list[str]:
        combos = input.split(',')
        for c in combos:
            if not self.validator.isValid(c) or \
               (self.validator.isSpecificSuitedCombo(c) and \
                not self.validator.isValidSpecificSuitedCombo(c)):
                raise ValueError(f'combo = {c} is invalid')
        return combos

    def __init__(self, input: str):
        self.expansions = []
        valid_combos = self.preprocess(input)
        for vc in valid_combos:
            self.expansions.append(self.expander.expand(vc).formatForInput())
        self.formatted_input = ','.join(self.expansions)

    def getHand(self):
        return self.formatted_input

    # hero is PsEvalInput instance
    def remove(self, hero):
        hand: str = hero.getHand()
        mirror = hand[2:] + hand[0:2]
        self.formatted_input = self.formatted_input \
            .replace(hand + ',', '').replace(mirror + ',', '')
        return self
