from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    superhero_api_endpoint: str
    superhero_api_token: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
