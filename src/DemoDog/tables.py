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

    user = relationship("User", backref='dogs')


class BaseUser(Base):
    __tablename__ = 'base-user'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    father_name = Column(String)
    date_create = Column(DateTime)
    date_update = Column(DateTime)
    is_deleted = Column(Boolean)
    type = Column(String(50))

    __mapper_args__ = {
        "polymorphic_identity": "base-user",
        "polymorphic_on": type,
    }


class User(BaseUser):
    __tablename__ = 'users'
    id = Column(Integer, ForeignKey("base-user.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "users",
    }


class Sitter(BaseUser):
    __tablename__ = 'sitters'
    id = Column(Integer, ForeignKey("base-user.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "sitters",
    }


class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    sitter_id = Column(Integer, ForeignKey("sitters.id"), Identity())
    date_create = Column(DateTime)
    date_update = Column(DateTime)
    walk_price = Column(Numeric(7, 2))
    overexpose_price = Column(Numeric(7, 2))

    sitter = relationship("Sitter", backref='prices')


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

    user = relationship("User", backref='orders')
    sitter = relationship("Sitter", backref='orders')
