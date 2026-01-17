import requests
import json
from sqlalchemy import create_engine, text
from config.settings import Settings

class SuperheroSeeder:
    def __init__(self, db_url, api_token, max_id=371):
        self.engine = create_engine(db_url)
        self.api_token = api_token
        self.base_url = settings.superhero_api_endpoint + api_token
        self.max_id = max_id

    def fetch_superhero(self, superhero_id):
        response = requests.get(f"{self.base_url}/{superhero_id}", timeout=10)
        if response.status_code != 200:
            return None
        data = response.json()
        if data.get("response") != "success":
            return None
        return data

    def seed(self):
        inserted = 0
        with self.engine.begin() as conn:
            for superhero_id in range(1, self.max_id + 1):
                superhero = self.fetch_superhero(superhero_id)
                try:
                    conn.execute(
                        text("""
                            INSERT INTO superheroes (
                                id,
                                name,
                                powerstats,
                                biography,
                                appearance,
                                work,
                                connections,
                                image_url
                            ) VALUES (
                                :id,
                                :name,
                                :powerstats,
                                :biography,
                                :appearance,
                                :work,
                                :connections,
                                :image_url
                            )
                            ON CONFLICT (id) DO NOTHING
                        """),
                        {
                            "id": superhero_id,
                            "name": json.dumps(superhero["name"]),
                            "powerstats": json.dumps(superhero["powerstats"]),
                            "biography": json.dumps(superhero["biography"]),
                            "appearance": json.dumps(superhero["appearance"]),
                            "work": json.dumps(superhero["work"]),
                            "connections": json.dumps(superhero["connections"]),
                            "image_url": json.dumps(superhero["image"]["url"]),
                        }
                    )
                    inserted += 1
                    print(f"Inserted : {superhero['name']} ({superhero_id})")

                except Exception as exception:
                    print(f"Error with ID {superhero_id} : {exception}")
        print(f"Total number of superheroes inserted : {inserted}")

if __name__ == "__main__":
    settings = Settings()
    seeder = SuperheroSeeder(
        db_url=settings.database_url,
        api_token=settings.superhero_api_token
    )
    seeder.seed()
