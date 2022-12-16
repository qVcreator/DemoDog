from sqlalchemy import Column, Integer, String, Float, ForeignKey, Numeric, Boolean, DateTime, Identity
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Dog(Base):
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    date_create = Column(DateTime)
    date_update = Column(DateTime)
    weight = Column(Float)
    breed = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_deleted = Column(Boolean)

    user = relationship("User", back_populates="dogs")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    father_name = Column(String)
    date_create = Column(DateTime)
    date_update = Column(DateTime)
    is_deleted = Column(Boolean)


class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    sitter_id = Column(Integer, ForeignKey("sitters.id"), Identity())
    date_create = Column(DateTime)
    date_update = Column(DateTime)
    walk_price = Column(Numeric(7, 2))
    overexpose_price = Column(Numeric(7, 2))

    sitter = relationship("Sitter", back_populates="sitters")


class Sitter(Base):
    __tablename__ = 'sitters'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    father_name = Column(String)
    date_create = Column(DateTime)
    date_update = Column(DateTime)
    is_deleted = Column(Boolean)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    sitter_id = Column(Integer, ForeignKey("sitters.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    date_create = Column(DateTime)
    date_update = Column(DateTime)
    service_type = Column(String)
    status = Column(String)
    is_deleted = Column(Boolean)
