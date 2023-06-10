from .test_utils import U
from lib.utils.expander import Expander


class ExpanderTest:

    expander = Expander()

    def runSuite(self):
        """main test runner"""
        print(Expander.__name__)

        self.unboundedPair()
        self.boundedPair()

    # add new test calls here
    def unboundedPair(self):
        """22+"""
        self.expander.expand('22+')
        pass

    def boundedPair(self):
        """22-77"""
        self.expander.expand('22-77')
        pass
