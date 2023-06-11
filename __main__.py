from lib.command import ps_eval
from lib.ps_eval_input import PsEvalInput
from tests.runner import runTests

input = PsEvalInput('77+,AJ-AK')

def main():
    hand = "TsTh"
    ps_eval(["-h", input.remove(hand), hand, "-b", "3c4c5c"])

main()
