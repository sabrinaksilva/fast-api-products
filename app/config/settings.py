from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    class Config:
        env_file = Path(__file__).parent / ".env"

settings = Settings()
