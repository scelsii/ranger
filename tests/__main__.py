import sys

from .utils.validator_test import ValidatorTest
from .utils.expander_test import ExpanderTest

# create test class instances here
validator_test = ValidatorTest()
expander_test = ExpanderTest()

# run test suites
def runTests(is_debug: bool):
    validator_test.runSuite(is_debug)
    expander_test.runSuite(is_debug)

if __name__ == '__main__':
    is_debug = False
    if len(sys.argv) > 1:
        is_debug = True
    runTests(is_debug)
