from sqlalchemy.orm import Session
from app.db.observation_model import Observation
from app.schemas import ObservationCreate

class ObservationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, observation_data: ObservationCreate):
        observation = Observation(**observation_data.dict())
        self.db.add(observation)
        self.db.commit()
        self.db.refresh(observation)
        return observation

    def list(self, skip: int = 0, limit: int = 10):
        return self.db.query(Observation).offset(skip).limit(limit).all()

    def delete(self, observation_id: int):
        observation = self.db.query(Observation).filter(Observation.id == observation_id).first()
        if observation:
            self.db.delete(observation)
            self.db.commit()
        return observation
