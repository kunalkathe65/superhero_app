from src.models.superhero import Superhero
from typing import List

class SuperheroRepository:

    def __init__(self,db):
        self.db=db

    def get_by_superhero_id(self, superhero_id) -> Superhero:
        return self.db.query(Superhero).filter(Superhero.superhero_id == superhero_id).first()
    
    def update_superhero(self, update_params, superhero_id) -> Superhero:
        superhero = self.db.query(Superhero).filter(Superhero.superhero_id == superhero_id).first()
        print("before", superhero.name)
        # Update only provided fields
        update_params = update_params.model_dump(exclude_unset=True)
        for key, value in update_params.items():
            if hasattr(superhero, key):
                setattr(superhero, key, value)
        self.db.commit()
        self.db.refresh(superhero)
        print("after", superhero.name)
        return superhero

    def get_all_superheroes(self) -> List[Superhero]:
        return self.db.query(Superhero).all()

