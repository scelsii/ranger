from lib.command import ps_eval
from tst.validHandPatterns import main

# tests
main()

"""
what are possible inputs?

simple to complex

AdTd -> exactly what it says
ATdd -> same as above, but should also be valid
KK -> all KK combos
QTo -> all unsuited QT combos
65s -> all suited 65 combos
+ -> all combos above this up to highest card in combo
- -> all combos from first to last hand (same pattern)

if +, all suited, unsuited combos, unless s(uited)
"""

ps_eval(["-h", "AcAs", "KhKd", "-b", "3c4c5c"])
