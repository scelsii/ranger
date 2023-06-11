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
        return H.combinations(combo)

    # 22+
    def allGreaterCombos(self, combo: str) -> list[str]:
        pass

    # QTo
    def allOffsuitCombos(self, combo: str) -> list[str]:
        pass

    # QTs
    def allSuitedCombos(self, combo: str) -> list[str]:
        pass

    # 76o+
    def allGreaterOffsuitCombos(self, combo: str) -> list[str]:
        pass

    # 76s+
    def allGreaterSuitedCombos(self, combo: str) -> list[str]:
        pass

    # 54-T9
    def allCombosBounded(self, combo: str) -> list[str]:
        pass

    # 54-T9o
    def allOffsuitCombosBounded(self, combo: str) -> list[str]:
        pass

    # 54-T9s
    def allSuitedCombosBounded(self, combo: str) -> list[str]:
        pass

    # 54-T9cc
    def allSpecificSuitedCombosBounded(self, combo: str) -> list[str]:
        pass
