from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False
)