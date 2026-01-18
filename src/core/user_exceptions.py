class AuthError(Exception):
    """Base auth exception"""

class UserNotFound(AuthError):
    pass

class InvalidPassword(AuthError):
    pass

class UserAlreadyExists(AuthError):
    pass
