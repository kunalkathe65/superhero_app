class TeamError(Exception):
    """Base team related exception"""

class TeamAlreadyExists(TeamError):
    pass

class TeamNotFound(TeamError):
    pass

class BalancedTeamsNotFound(TeamError):
    pass

class NotEnoughBalancedTeams(TeamError):
    pass

class SpecialtyTeamsNotFound(TeamError):
    pass

class NotEnoughSpecialtyTeams(TeamError):
    pass