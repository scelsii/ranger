SUIT_LIST = list('hdcs')

class ExpansionHelpers:

    def combinations(self, combo: str) -> list[str]:
        [top, bottom] = list(combo)
        return self.prune([top + x + bottom + y for x in SUIT_LIST for y in SUIT_LIST])

    def prune(self, perms):
        deduped = self.dedupe(perms)
        cleaned = self.clean(deduped)
        return cleaned

    def dedupe(self, perms):
        results = []
        seen = {}
        for p in perms:
            p_mirror = p[2:] + p[0:2]
            if p_mirror not in seen and p not in seen:
                results.append(p)
                seen[p] = True
                seen[p_mirror] = True
        return results

    def clean(self, deduped):
        result = []
        for v in deduped:
            if v[0:2] != v[2:]:
                result.append(v)
        return result

    def format(self, combos: list[str]) -> str:
        return ','.join(combos)

"""
def expandDiscrete(self, match_key: MatcherKey, combo: str) -> list[str]:
        print(f'expanding combo = {combo} with match_key = {match_key}')

        [a, b, *extra] = list(combo)
        c = PokerIterator(a)
        d = PokerIterator(b)

        card_only_perms = []

        while c.current() is not c.top() and d.current() is not d.top():
            card_only_perms.append(c + d)
            c.next(); d.next()

        expansion = []
        for p in card_only_perms:
            [top, bottom] = list(p)
            expansion += self.prune([top + x + bottom + y for x in SUIT_LIST for y in SUIT_LIST])

        print(expansion)

        return expansion
"""
