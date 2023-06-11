import sys

from lib.command import ps_eval
from lib.ps_eval_input import PsEvalInput

"""
use:

$ python3 . <hero> <villain_range> [<board>]

example:

$ python3 . TcTs 77+,AK '3c4c5c'

The hand 7h7d,7h7c,7h7s,7d7c,7d7s,7c7s,8h8d,8h8c,8h8s,8d8c,8d8s,8c8s,9h9d,9h9c,9h9s,9d9c,9d9s,9c9s,ThTd,ThTc,ThTs,TdTc,TdTs,JhJd,JhJc,JhJs,JdJc,JdJs,JcJs,QhQd,QhQc,QhQs,QdQc,QdQs,QcQs,KhKd,KhKc,KhKs,KdKc,KdKs,KcKs,AhAd,AhAc,AhAs,AdAc,AdAs,AcAs,AhKh,AhKd,AhKc,AhKs,AdKh,AdKd,AdKc,AdKs,AcKh,AcKd,AcKc,AcKs,AsKh,AsKd,AsKc,AsKs has 44.9324 % equity (25179 1066 0 0)
The hand TcTs has 55.0676 % equity (31099 1066 0 0)
"""

hero = PsEvalInput(sys.argv[1])
villain_range = PsEvalInput(sys.argv[2])
board = None if len(sys.argv) < 4 else sys.argv[3]

args = ['-h', hero.getHand(), villain_range.remove(hero).getHand()]

if board is not None:
    args += ['-b', board]

ps_eval(args)
