# Ranger

A Holdem poker analysis CLI util for all systems

## Why

[PokerStove](https://github.com/andrewprock/pokerstove) is/was an amazing poker analysis tool developed as a GUI for Windows systems. The GUI is powered by a set of C++ libraries including `ps_eval`, which does not natively support poker ranges

We are `hero` and our opponent is `villain`. If we want to calculate the likelihood of hero winning against a set of villain hands -- this is a `range` -- then we need a way of creating that range from common shorthand poker notation

## How

Run scenarios with or without a `board` at any stage of play

- preflop = no board
- flop    = 3 cards
- turn    = 4 cards
- river   = 5 cards

```bash
$ python3 . TcTs 77+,AK '3c4c5c'
The hand TcTs has 55.0676 % equity (31099 1066 0 0)
The hand 77+,AK has 44.9324 % equity (25179 1066 0 0)
```

## Rules

- Hero can only supply one hand (we know what we're holding)
- Villain can supply any combination of discrete hands and ranges (comma-separated)

## Supported shorthand types and what they mean

The best way to see what inputs are supported is to run the Ranger test suites and look at the left-hand side of each `Expander` test case

```bash
$ python3 -m tests

Validator
✅ .isValid -> all valid hands return True
✅ .isValid -> all invalid hands return False
Expander
✅ JdTc -> K.EXACT
✅ JThh -> K.EXACT_SUITED
✅ KK -> K.ALL_COMBOS
✅ 22+ -> K.ALL_GREATER_COMBOS
✅ QTo -> K.ALL_OFFSUIT_COMBOS
✅ QTs -> K.ALL_SUITED_COMBOS
✅ 76o+ -> K.ALL_GREATER_OFFSUIT_COMBOS
✅ 76s+ -> K.ALL_GREATER_SUITED_COMBOS
✅ JThh+ -> K.ALL_GREATER_SPECIFIC_SUITED_COMBOS
✅ 54-T9 -> K.ALL_COMBOS_BOUNDED
✅ 54-T9o -> K.ALL_SUITED_COMBOS_BOUNDED
✅ 54-T9s -> K.ALL_SUITED_COMBOS_BOUNDED
✅ 54-T9cc -> K.ALL_SPECIFIC_SUITED_COMBOS_BOUNDED
```

> A note about hand ranges: notice we're using combinations, not permutations: `AdAc` and `AcAd` are the same hand. `K`-fields are pattern matchers for the type of shorthand notation that's under test

