from src.core.team_exceptions import TeamAlreadyExists, TeamNotFound, NotEnoughSpecialtyTeams, SpecialtyTeamsNotFound, NotEnoughBalancedTeams, BalancedTeamsNotFound
from random import shuffle

class TeamService:
    def __init__(self, repo):
        self.repo = repo
    
    def serialize_superhero(self, superhero):
        return {
            "superhero_id": superhero.superhero_id,
            "name": superhero.name,
            "powerstats": superhero.powerstats,
            "image_url": superhero.image_url,
        }
    
    def safe_int(self, val):
        try:
            return int(val)
        except:
            return 0

    def create_team(self, data, user_id):
        team_does_exist = self.repo.get_by_name(data.name)
        if team_does_exist:
            raise TeamAlreadyExists()
        return self.repo.create(data, user_id)
    
    def get_user_teams(self, user_id):
        teams = self.repo.get_by_user_id(user_id)
        if teams:
            return teams
        raise TeamNotFound
    
    def recommend_balanced_teams(self, limit):
        recommended_teams = []
        minimum_stat_val = 50
        superheroes = self.repo.get_superheroes(limit)
        if superheroes:
            serialized_superheroes = [self.serialize_superhero(superhero) for superhero in superheroes]
            eligible = []
            for superhero in serialized_superheroes:
                total = sum(self.safe_int(v) for v in superhero.get("powerstats", {}).values())
                # Balanced team is : whose sum of all stats is at least 50
                if total >= minimum_stat_val:
                    eligible.append(superhero)
            # Shuffle to randomize team assignment
            shuffle(eligible)
            for i in range(limit):
                team = []
                for j in range(limit):
                    superhero = eligible[i * limit + j]
                    team.append({
                        "superhero_id": superhero["superhero_id"],
                        "name": superhero["name"],
                        "image_url": superhero["image_url"],
                        "powerstat_total": sum(self.safe_int(v) for v in superhero.get("powerstats", {}).values())
                    })
                recommended_teams.append(team)
            if recommended_teams:
                return recommended_teams
            raise BalancedTeamsNotFound()
        raise NotEnoughBalancedTeams()

    def recommend_specialty_team(self, limit, specialty):
        superheroes = self.repo.get_superheroes(limit)
        POWERSTATS = ["intelligence", "strength", "speed", "durability", "power", "combat"]
        recommended_team = []
        if superheroes:
            serialized_superheroes = [self.serialize_superhero(superhero) for superhero in superheroes]
            for superhero in serialized_superheroes:
                stats = {
                    stat: self.safe_int(superhero["powerstats"].get(stat))
                    for stat in POWERSTATS
                }

                # Check if passed stat is the highest for THIS hero
                max_stat_value = max(stats.values())

                if stats[specialty] == max_stat_value and max_stat_value > 0 and len(recommended_team) < 6:
                    recommended_team.append(superhero)
            
            if recommended_team:
                return recommended_team
            raise SpecialtyTeamsNotFound()
        raise NotEnoughSpecialtyTeams()

    def recommend_random_team(self):
        superheroes = self.repo.get_random_superheroes()
        if superheroes:
            return [self.serialize_superhero(superhero) for superhero in superheroes]
        raise TeamNotFound()

    def list_all_teams(self):
        teams = self.repo.get_all_teams()
        if teams:
            return teams
        raise TeamNotFound()