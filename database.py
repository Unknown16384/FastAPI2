from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  declarative_base

class Sellers(declarative_base()):
    __tablename__ = 'Sellers'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
