class TeamError(Exception):
    """Base team related exception"""

class TeamAlreadyExists(TeamError):
    pass

class TeamNotFound(TeamError):
    pass