from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey

Base = declarative_base()

# Create model url
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    client = relationship("Client", back_populates="user")
