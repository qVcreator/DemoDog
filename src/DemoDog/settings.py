from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host : str = 'localhost'
    server_port : int = 8000

    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD = 'qwe123'
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: str = '5432'
    POSTGRES_DB: str = 'DemoDog'
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()