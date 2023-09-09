from .expansion_flags import F
from .poker_iterator import PokerIterator
from .validator import Validator

SUIT_LIST = list('hdcs')

class ExpansionHelpers:

    validator = Validator()

    # strip flags and return cards only
    def getRawHand(self, combo: str) -> str:
        return combo[0:2]

    # '22-77' -> ['22', '77']
    def getRawHandAndCeiling(self, combo: str) -> list[str]:
        return [self.getRawHand(c) for c in combo.split('-')]

    def getRawHandAndCeilingWithSuit(self, combo: str) -> list[str]:
        suit = combo[5]
        return [self.getRawHand(c) for c in combo.split('-')] + [suit]

    # get suit from eg 'AJhh'
    def getComboSuit(self, combo: str) -> str:
        return combo[2]

    def allGreaterCombinations(self, raw_hand: str, filters={}, ceiling=None) -> list[str]:
        [a, b] = list(raw_hand)

        c = PokerIterator(a)
        d = PokerIterator(b)
        raw_hands = []

        (c_top, d_top) = PokerIterator.getTops(ceiling)

        while c.current() != c_top and d.current() != d_top:
            raw_hands.append(c + d)
            c.next(); d.next()

        expansion = []
        for p in raw_hands:
            expansion += self.combinations(p, filters)

        return expansion

    def combinations(self, raw_hand: str, filters={}) -> list[str]:
        [top, bottom] = list(raw_hand)
        result = self.prune([top + x + bottom + y for x in SUIT_LIST for y in SUIT_LIST])
        [offsuit, suited, suit] = self.unpackFilters(filters)
        if offsuit:
            return self.offsuit(result)
        elif suited:
            return self.suited(result, suit)
        else:
            return result

    def getFilters(self, flag, suit=None):
        result = {}
        if flag == F.OFFSUIT:
            result['offsuit'] = True
        elif flag == F.SUITED:
            result['suited'] = True
            result['suit'] = suit
        return result

    def unpackFilters(self, filters: dict):
        offsuit = filters.get('offsuit')
        suited = filters.get('suited')
        suit = filters.get('suit')
        return [offsuit, suited, suit]

    def offsuit(self, combs: list[str]):
        result = []
        for c in combs:
            [a, b] = [c[0:2], c[2:]]
            s1, s2 = a[1], b[1]
            if s1 != s2:
                result.append(c)
        return result

    def suited(self, combs: list[str], suit=None):
        result = []
        for c in combs:
            [a, b] = [c[0:2], c[2:]]
            s1, s2 = a[1], b[1]
            if suit is not None:
                if s1 == suit and s2 == suit:
                    result.append(c)
            else:
                if s1 == s2:
                    result.append(c)
        return result

    def prune(self, perms: list[str]):
        deduped = self.dedupe(perms)
        cleaned = self.clean(deduped)
        return cleaned

    # ATdd -> AdTd
    def normalizeSpecificSuitedCombo(self, combo: str):
        return combo[0] + combo[2] + combo[1] + combo[3]

    def getMirror(self, combo: str):
        return combo[2:] + combo[0:2]

    def dedupe(self, perms: list[str]):
        results = []
        seen = {}
        for p in perms:
            p_mirror = self.getMirror(p)
            if p_mirror not in seen and p not in seen:
                results.append(p)
                seen[p] = True
                seen[p_mirror] = True
        return results

    def clean(self, deduped: list[str]):
        result = []
        for v in deduped:
            if v[0:2] != v[2:]:
                result.append(v)
        return result

    def format(self, combos: list[str]) -> str:
        return ','.join(combos)
