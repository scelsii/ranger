import sys

from lib.command import ps_eval
from lib.ps_eval_input import PsEvalInput

"""
use:

$ python3 . <hero> <villain_range> [<board>]

example:

$ python3 . TcTs 77+,AK '3c4c5c'
The hand TcTs has 55.0676 % equity (31099 1066 0 0)
The hand 77+,AK has 44.9324 % equity (25179 1066 0 0)
"""

hero = PsEvalInput(sys.argv[1])
villain_range = PsEvalInput(sys.argv[2])
board = None if len(sys.argv) < 4 else sys.argv[3]

hero_hand = hero.getHand()
villain_hand = villain_range.remove(hero).getHand()

args = ['-h', hero_hand, villain_hand]

if board is not None:
    args += ['-b', board]

output = ps_eval(args)
print(output.replace(villain_hand, sys.argv[2]))
