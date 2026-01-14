class TornAPIError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"Error {code}: {message}")


# 0
class UnknownError(TornAPIError):
    pass

# 1
class NoKeyError(TornAPIError):
    pass

# 2
class IncorrectKeyError(TornAPIError):
    pass

# 3
class WrongTypeError(TornAPIError):
    pass

# 4
class WrongFieldsError(TornAPIError):
    pass

# 5
class TooManyRequestsError(TornAPIError):
    pass

# 6
class IncorrectIDError(TornAPIError):
    pass

# 7
class IncorredIDEntityRelationError(TornAPIError):
    pass

# 8
class IPBlockError(TornAPIError):
    pass

# 9
class APIDisabledError(TornAPIError):
    pass

# 10
class KeyOwnerInFederalJailError(TornAPIError):
    pass

# 11
class KeyChangeError(TornAPIError):
    pass

# 12
class KeyReadError(TornAPIError):
    pass

# 13
class KeyDisabledDueToInactivityError(TornAPIError):
    pass

# 14
class DailyLimitReachedError(TornAPIError):
    pass

# 15
class TemporaryError(TornAPIError):
    pass

# 16
class AccessLevelError(TornAPIError):
    pass