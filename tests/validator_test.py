from .test_utils import U
from lib.utils.validator import Validator


class ValidatorTest:

    # 'AAd' not working

    validator = Validator()

    VALID_HANDS = [
        'AdTd',
        'ATdd',
        'KK',
        'QTo',
        '65s',
        '76-AKs',
        'T9-KQss',
    ]

    INVALID_HANDS = [
        'AJd',
        'Add',
        'AJddd',
        '1Jdd',
        'KToo',
        'KTos',
    ]

    def runSuite(self):
        """main test runner"""
        print(Validator.__name__)

        self.validHands()
        self.invalidHands()
        # add new test calls here



    def validHands(self):
        for h in self.VALID_HANDS:
            if self.validator.is_valid(h) != True:
                return U.fail(f'failed to recognize valid hand: {h}')

        U.success('.is_valid -> all valid hands return True')


    def invalidHands(self):
        for h in self.INVALID_HANDS:
            if self.validator.is_valid(h) != False:
                return U.fail(f'failed to recognize invalid hand: {h}')

        U.success('.is_valid -> all invalid hands return False')
