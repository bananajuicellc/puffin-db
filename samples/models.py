from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class JustIntegers(Base):
    __tablename__ = "just_integers"

    id_ = Column("id", Integer, primary_key=True)
    value = Column(Integer)

