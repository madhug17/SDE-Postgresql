from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "anime_macha"

    anime_id = Column(Integer,primary_key=True)
    anime_name = Column(String(100),nullable=False,default='NONE')
    email = Column(String(100),nullable=True,unique=True)
    status = Column(String(30),nullable=True,default='Watching')
    rating = Column(Integer,nullable=False,server_default='5')
class AnimeStudio(Base):
    __tablename__ = "anime_studios"
    studio_id = Column(Integer, primary_key=True)
    studio__name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=True)