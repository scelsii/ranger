from validate.validator import is_valid

def assertTrue(result):
    return result == True

def test(result):
    print(assertTrue(result))

def main():
    # all valid hands
    print("all valid hands")
    test(is_valid("AdTd"))
    test(is_valid("ATdd"))
    test(is_valid("KK"))
    test(is_valid("QTo"))
    test(is_valid("65s"))
    test(is_valid("76-AKs"))
    test(is_valid("T9-KQss"))

    print("\n")

    # all invalid hands
    print("all invalid hands")
    test(is_valid("AJd"))
    test(is_valid("Add"))
    test(is_valid("AJddd"))
    test(is_valid("1Jdd"))
    test(is_valid("KToo"))
    test(is_valid("KTos"))
