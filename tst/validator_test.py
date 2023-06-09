from lib.utils.validator import Validator


class ValidatorTest:

    validator = Validator()

    VALID_HANDS = [
        "AdTd",
        "ATdd",
        "KK",
        "QTo",
        "65s",
        "76-AKs",
        "T9-KQss",
    ]

    INVALID_HANDS = [
        "AJd",
        "Add",
        "AJddd",
        "1Jdd",
        "KToo",
        "KTos",
    ]

    def runSuite(self):
        """main test runner"""

        self.validHands()
        self.invalidHands()
        # add new test calls here

    def validHands(self):
        print('.is_valid -> all *valid hands return "true"')

        for h in self.VALID_HANDS:
            if self.validator.is_valid(h) != True:
                raise ValueError(f'failure to check valid hand: {h}')


    def invalidHands(self):
        print('.is_valid -> all *invalid hands return "false"')

        for h in self.INVALID_HANDS:
            if self.validator.is_valid(h) != False:
                raise ValueError(f'failure to check invalid hand: {h}')
