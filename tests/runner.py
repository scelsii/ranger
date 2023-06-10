from .validator_test import ValidatorTest
from .expander_test import ExpanderTest

# create test class instances here
validator_test = ValidatorTest()
expander_test = ExpanderTest()

# run test suites
def runTests():
    validator_test.runSuite()
    expander_test.runSuite()
