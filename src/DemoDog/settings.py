from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD = 'qwe123'
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: str = '5432'
    POSTGRES_DB: str = 'DemoDog'
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    JWT_SECRET = 'temp'
    JWT_ALGORITHM = 'HS256'
    JWT_EXPIRES_S = 3600


settings = Settings()
