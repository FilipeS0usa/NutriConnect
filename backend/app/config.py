from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    api_key: str = "your-api-key-here"

settings = Settings()
