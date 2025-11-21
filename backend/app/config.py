import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuration simple de l'application"""
    
    # Base de données
    DATABASE_URL: str = "postgresql://notesuser:notespassword123@postgres:5432/notesdb"
    
    # Token pour sécuriser l'API
    API_TOKEN: str = "mon-super-token-secret-123"
    
    class Config:
        env_file = ".env"


# Instance de configuration
settings = Settings()
