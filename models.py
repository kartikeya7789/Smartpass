from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)


class Leave(Base):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True)
    student = Column(String)
    reason = Column(String)
    status = Column(String)
