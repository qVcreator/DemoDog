from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .settings import settings

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
