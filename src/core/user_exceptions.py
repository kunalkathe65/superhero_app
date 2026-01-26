class AuthError(Exception):
    """Base auth exception"""

class UserNotFound(AuthError):
    pass

class InvalidPassword(AuthError):
    pass

class UserAlreadyExists(AuthError):
    pass

class SuperheroAlreadyFavourite(AuthError):
    pass

class NoFavSuperheroesFound(AuthError):
    pass

class NotAuthorized(AuthError):
    pass
