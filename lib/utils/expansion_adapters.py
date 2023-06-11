from .expansion_flags import F
from .expansion_helpers import ExpansionHelpers

H = ExpansionHelpers()

class ExpansionAdapters:

    # AdTd
    def exact(self, combo: str) -> list[str]:
        return [combo]

    # ATdd
    def exactSuited(self, combo: str) -> list[str]:
        return [combo]

    # KK
    def allCombos(self, combo: str) -> list[str]:
        raw_hand = H.getRawHand(combo)
        return H.combinations(raw_hand)

    # 22+
    def allGreaterCombos(self, combo: str) -> list[str]:
        raw_hand = H.getRawHand(combo)
        return H.allGreaterCombinations(raw_hand)

    # QTo
    def allOffsuitCombos(self, combo: str) -> list[str]:
        raw_hand = H.getRawHand(combo)
        return H.combinations(raw_hand, filters=H.getFilters(F.OFFSUIT))

    # QTs
    def allSuitedCombos(self, combo: str) -> list[str]:
        raw_hand = H.getRawHand(combo)
        return H.combinations(raw_hand, filters=H.getFilters(F.SUITED))

    # 76o+
    def allGreaterOffsuitCombos(self, combo: str) -> list[str]:
        raw_hand = H.getRawHand(combo)
        return H.allGreaterCombinations(raw_hand, filters=H.getFilters(F.OFFSUIT))

    # 76s+
    def allGreaterSuitedCombos(self, combo: str) -> list[str]:
        raw_hand = H.getRawHand(combo)
        return H.allGreaterCombinations(raw_hand, filters=H.getFilters(F.SUITED))

    # JThh+
    def allGreaterSpecificSuitedCombos(self, combo: str) -> list[str]:
        raw_hand = H.getRawHand(combo)
        combo_suit = H.getComboSuit(combo)
        return H.allGreaterCombinations(raw_hand, H.getFilters(F.SUITED, combo_suit))

    # 54-T9
    def allCombosBounded(self, combo: str) -> list[str]:
        [raw_hand, ceiling] = H.getRawHandAndCeiling(combo)
        return H.allGreaterCombinations(raw_hand, ceiling)

    # 54-T9o
    def allOffsuitCombosBounded(self, combo: str) -> list[str]:
        [raw_hand, ceiling] = H.getRawHandAndCeiling(combo)
        return H.allGreaterCombinations(raw_hand, ceiling, H.getFilters(F.OFFSUIT))

    # 54-T9s
    def allSuitedCombosBounded(self, combo: str) -> list[str]:
        [raw_hand, ceiling] = H.getRawHandAndCeiling(combo)
        return H.allGreaterCombinations(raw_hand, ceiling, H.getFilters(F.SUITED))

    # 54-T9cc
    def allSpecificSuitedCombosBounded(self, combo: str) -> list[str]:
        [raw_hand, ceiling] = H.getRawHandAndCeiling(combo)
        suit = H.getComboSuit(ceiling)
        return H.allGreaterCombinations(raw_hand, ceiling, filters=H.getFilters(F.SUITED, suit))
