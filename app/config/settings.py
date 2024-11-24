from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    google_client_id: str
    google_client_secret: str
    google_redirect_url: str
    client_url: str
    token_secret: str

    class Config:
        env_file = Path(__file__).parent / ".env"


settings = Settings()
