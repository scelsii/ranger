class H:
    SUCCESS_EMOJI = u'\u2705'
    FAIL_EMOJI = u'\u274C'

class TestUtils:

    def success(self, msg: str) -> None:
        print(H.SUCCESS_EMOJI + ' ' + msg)

    def fail(self, msg: str) -> None:
        print(H.FAIL_EMOJI + ' ' + msg)

U = TestUtils()
