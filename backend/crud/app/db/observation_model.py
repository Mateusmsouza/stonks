from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Observation(Base):
    __tablename__ = "observations"

    id = Column(Integer, primary_key=True, index=True)
    cryptocurrency = Column(String, index=True)
    upper_limit = Column(Float, nullable=False)
    lower_limit = Column(Float, nullable=False)
