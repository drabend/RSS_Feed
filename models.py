from db import Base
from sqlalchemy import Column, Integer, String

class Feed(Base):
    __tablename__ = 'feeds'
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, unique=True, nullable=False, index=True)

