from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.observation_service import ObservationService
from app.schemas import Observation, ObservationCreate

class ObservationRouter:
    def __init__(self):
        self.router = APIRouter()
        self._setup_routes()

    def _get_db(self):
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def _setup_routes(self):
        @self.router.post("/", response_model=Observation)
        def create_observation(
            observation_data: ObservationCreate,
            db: Session = Depends(self._get_db),
        ):
            service = ObservationService(db)
            return service.create_observation(observation_data)

        @self.router.get("/", response_model=list[Observation])
        def list_observations(
            skip: int = 0,
            limit: int = 10,
            db: Session = Depends(self._get_db),
        ):
            service = ObservationService(db)
            return service.list_observations(skip, limit)

        @self.router.delete("/{observation_id}", response_model=Observation)
        def delete_observation(
            observation_id: int,
            db: Session = Depends(self._get_db),
        ):
            service = ObservationService(db)
            observation = service.delete_observation(observation_id)
            if not observation:
                raise HTTPException(status_code=404, detail="Observation not found")
            return observation
