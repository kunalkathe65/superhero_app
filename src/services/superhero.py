from src.core.superhero_exceptions import SuperheroNotFound
from src.core.user_exceptions import NotAuthorized

class SuperheroService:
    def __init__(self, repo):
        self.repo = repo

    def list_all_superheroes(self):
        superheroes = self.repo.get_all_superheroes()
        if not superheroes:
            raise SuperheroNotFound()
        return superheroes

    def get_superhero_details(self, superhero_id):
        superhero = self.repo.get_by_superhero_id(superhero_id)
        if not superhero:
            raise SuperheroNotFound()
        return superhero
    
    def update_superhero_details(self, update_params, superhero_id, user):
        if user.role != 1:
            raise NotAuthorized()
        superhero = self.repo.get_by_superhero_id(superhero_id)
        if not superhero:
            raise SuperheroNotFound()
        updated_superhero = self.repo.update_superhero(update_params, superhero_id)
        if not updated_superhero:
            return False
        return True