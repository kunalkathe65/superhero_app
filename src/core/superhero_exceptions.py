class SuperheroError(Exception):
    """Base superhero related exception"""

class SuperheroNotFound(SuperheroError):
    pass