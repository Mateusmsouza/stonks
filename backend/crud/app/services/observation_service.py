from sqlalchemy.orm import Session
from app.repositories.observation_repository import ObservationRepository
from app.schemas import ObservationCreate

class ObservationService:
    def __init__(self, db: Session):
        self.repository = ObservationRepository(db)

    def create_observation(self, observation_data: ObservationCreate):
        return self.repository.create(observation_data)

    def list_observations(self, skip: int = 0, limit: int = 10):
        return self.repository.list(skip, limit)

    def delete_observation(self, observation_id: int):
        return self.repository.delete(observation_id)
