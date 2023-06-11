from ..test_utils import U
from lib.utils.expander import Expander, Expansion
from lib.utils.hands import K

E = Expander()
SEP = ' -> '

class ExpanderTest:
    def runSuite(self):
        """main test runner"""
        print(Expander.__name__)

        self.exact()
        self.exactSuited()
        self.allCombos()
        self.allGreaterCombos()
        self.allOffsuitCombos()
        self.allSuitedCombos()
        self.allGreaterOffsuitCombos()
        self.allGreaterSuitedCombos()
        self.allGreaterSpecificSuitedCombos()
        self.allCombosBounded()
        self.allOffsuitCombosBounded()
        self.allSuitedCombosBounded()
        self.allSpecificSuitedCombosBounded()
        # add new test calls here

    def getMessage(self, hand, matcher_key):
        return SEP.join([hand, str(matcher_key)])

    def test(self, expected: list[str], actual: Expansion, msg):
        return U.success(msg) if expected == actual._expansion else U.fail(msg)

    def exact(self):
        hand = 'JdTc'
        expected = [hand]
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.EXACT)
        self.test(expected, actual, msg)

    def exactSuited(self):
        hand = 'JThh'
        normalized = 'JhTh'
        expected = [normalized]
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.EXACT_SUITED)
        self.test(expected, actual, msg)

    def allCombos(self):
        hand = 'KK'
        expected = ['KhKd', 'KhKc', 'KhKs', 'KdKc', 'KdKs', 'KcKs']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_COMBOS)
        self.test(expected, actual, msg)

    def allGreaterCombos(self):
        hand = '22+'
        expected = ['2h2d', '2h2c', '2h2s', '2d2c', '2d2s', '2c2s', '3h3d', '3h3c', '3h3s', '3d3c', '3d3s', '3c3s', '4h4d', '4h4c', '4h4s', '4d4c', '4d4s', '4c4s', '5h5d', '5h5c', '5h5s', '5d5c', '5d5s', '5c5s', '6h6d', '6h6c', '6h6s', '6d6c', '6d6s', '6c6s', '7h7d', '7h7c', '7h7s', '7d7c', '7d7s', '7c7s', '8h8d', '8h8c', '8h8s', '8d8c', '8d8s', '8c8s', '9h9d', '9h9c', '9h9s', '9d9c', '9d9s', '9c9s', 'ThTd', 'ThTc', 'ThTs', 'TdTc', 'TdTs', 'TcTs', 'JhJd', 'JhJc', 'JhJs', 'JdJc', 'JdJs', 'JcJs', 'QhQd', 'QhQc', 'QhQs', 'QdQc', 'QdQs', 'QcQs', 'KhKd', 'KhKc', 'KhKs', 'KdKc', 'KdKs', 'KcKs', 'AhAd', 'AhAc', 'AhAs', 'AdAc', 'AdAs', 'AcAs']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_GREATER_COMBOS)
        self.test(expected, actual, msg)

    def allOffsuitCombos(self):
        hand = 'QTo'
        expected = ['QhTd', 'QhTc', 'QhTs', 'QdTh', 'QdTc', 'QdTs', 'QcTh', 'QcTd', 'QcTs', 'QsTh', 'QsTd', 'QsTc']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_OFFSUIT_COMBOS)
        self.test(expected, actual, msg)

    def allSuitedCombos(self):
        hand = 'QTs'
        expected = ['QhTh', 'QdTd', 'QcTc', 'QsTs']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_SUITED_COMBOS)
        self.test(expected, actual, msg)

    def allGreaterOffsuitCombos(self):
        hand = '76o+'
        expected = ['7h6d', '7h6c', '7h6s', '7d6h', '7d6c', '7d6s', '7c6h', '7c6d', '7c6s', '7s6h', '7s6d', '7s6c', '8h7d', '8h7c', '8h7s', '8d7h', '8d7c', '8d7s', '8c7h', '8c7d', '8c7s', '8s7h', '8s7d', '8s7c', '9h8d', '9h8c', '9h8s', '9d8h', '9d8c', '9d8s', '9c8h', '9c8d', '9c8s', '9s8h', '9s8d', '9s8c', 'Th9d', 'Th9c', 'Th9s', 'Td9h', 'Td9c', 'Td9s', 'Tc9h', 'Tc9d', 'Tc9s', 'Ts9h', 'Ts9d', 'Ts9c', 'JhTd', 'JhTc', 'JhTs', 'JdTh', 'JdTc', 'JdTs', 'JcTh', 'JcTd', 'JcTs', 'JsTh', 'JsTd', 'JsTc', 'QhJd', 'QhJc', 'QhJs', 'QdJh', 'QdJc', 'QdJs', 'QcJh', 'QcJd', 'QcJs', 'QsJh', 'QsJd', 'QsJc', 'KhQd', 'KhQc', 'KhQs', 'KdQh', 'KdQc', 'KdQs', 'KcQh', 'KcQd', 'KcQs', 'KsQh', 'KsQd', 'KsQc', 'AhKd', 'AhKc', 'AhKs', 'AdKh', 'AdKc', 'AdKs', 'AcKh', 'AcKd', 'AcKs', 'AsKh', 'AsKd', 'AsKc']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_GREATER_OFFSUIT_COMBOS)
        self.test(expected, actual, msg)

    def allGreaterSuitedCombos(self):
        hand = '76s+'
        expected = ['7h6h', '7d6d', '7c6c', '7s6s', '8h7h', '8d7d', '8c7c', '8s7s', '9h8h', '9d8d', '9c8c', '9s8s', 'Th9h', 'Td9d', 'Tc9c', 'Ts9s', 'JhTh', 'JdTd', 'JcTc', 'JsTs', 'QhJh', 'QdJd', 'QcJc', 'QsJs', 'KhQh', 'KdQd', 'KcQc', 'KsQs', 'AhKh', 'AdKd', 'AcKc', 'AsKs']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_GREATER_SUITED_COMBOS)
        self.test(expected, actual, msg)

    def allGreaterSpecificSuitedCombos(self):
        hand = 'JThh+'
        expected = ['JhTh', 'QhJh', 'KhQh', 'AhKh']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_GREATER_SPECIFIC_SUITED_COMBOS)
        self.test(expected, actual, msg)

    def allCombosBounded(self):
        hand = '54-T9'
        expected = ['5h4h', '5h4d', '5h4c', '5h4s', '5d4h', '5d4d', '5d4c', '5d4s', '5c4h', '5c4d', '5c4c', '5c4s', '5s4h', '5s4d', '5s4c', '5s4s', '6h5h', '6h5d', '6h5c', '6h5s', '6d5h', '6d5d', '6d5c', '6d5s', '6c5h', '6c5d', '6c5c', '6c5s', '6s5h', '6s5d', '6s5c', '6s5s', '7h6h', '7h6d', '7h6c', '7h6s', '7d6h', '7d6d', '7d6c', '7d6s', '7c6h', '7c6d', '7c6c', '7c6s', '7s6h', '7s6d', '7s6c', '7s6s', '8h7h', '8h7d', '8h7c', '8h7s', '8d7h', '8d7d', '8d7c', '8d7s', '8c7h', '8c7d', '8c7c', '8c7s', '8s7h', '8s7d', '8s7c', '8s7s', '9h8h', '9h8d', '9h8c', '9h8s', '9d8h', '9d8d', '9d8c', '9d8s', '9c8h', '9c8d', '9c8c', '9c8s', '9s8h', '9s8d', '9s8c', '9s8s', 'Th9h', 'Th9d', 'Th9c', 'Th9s', 'Td9h', 'Td9d', 'Td9c', 'Td9s', 'Tc9h', 'Tc9d', 'Tc9c', 'Tc9s', 'Ts9h', 'Ts9d', 'Ts9c', 'Ts9s']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_COMBOS_BOUNDED)
        self.test(expected, actual, msg)

    def allOffsuitCombosBounded(self):
        hand = '54-T9o'
        expected = ['5h4d', '5h4c', '5h4s', '5d4h', '5d4c', '5d4s', '5c4h', '5c4d', '5c4s', '5s4h', '5s4d', '5s4c', '6h5d', '6h5c', '6h5s', '6d5h', '6d5c', '6d5s', '6c5h', '6c5d', '6c5s', '6s5h', '6s5d', '6s5c', '7h6d', '7h6c', '7h6s', '7d6h', '7d6c', '7d6s', '7c6h', '7c6d', '7c6s', '7s6h', '7s6d', '7s6c', '8h7d', '8h7c', '8h7s', '8d7h', '8d7c', '8d7s', '8c7h', '8c7d', '8c7s', '8s7h', '8s7d', '8s7c', '9h8d', '9h8c', '9h8s', '9d8h', '9d8c', '9d8s', '9c8h', '9c8d', '9c8s', '9s8h', '9s8d', '9s8c', 'Th9d', 'Th9c', 'Th9s', 'Td9h', 'Td9c', 'Td9s', 'Tc9h', 'Tc9d', 'Tc9s', 'Ts9h', 'Ts9d', 'Ts9c']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_SUITED_COMBOS_BOUNDED)
        self.test(expected, actual, msg)

    def allSuitedCombosBounded(self):
        hand = '54-T9s'
        expected = ['5h4h', '5d4d', '5c4c', '5s4s', '6h5h', '6d5d', '6c5c', '6s5s', '7h6h', '7d6d', '7c6c', '7s6s', '8h7h', '8d7d', '8c7c', '8s7s', '9h8h', '9d8d', '9c8c', '9s8s', 'Th9h', 'Td9d', 'Tc9c', 'Ts9s']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_SUITED_COMBOS_BOUNDED)
        self.test(expected, actual, msg)

    def allSpecificSuitedCombosBounded(self):
        hand = '54-T9cc'
        expected = ['5c4c', '6c5c', '7c6c', '8c7c', '9c8c', 'Tc9c']
        actual = E.expand(hand)
        msg = self.getMessage(hand, K.ALL_SPECIFIC_SUITED_COMBOS_BOUNDED)
        self.test(expected, actual, msg)
