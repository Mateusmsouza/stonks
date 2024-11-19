from pydantic import BaseModel

class ObservationBase(BaseModel):
    cryptocurrency: str
    upper_limit: float
    lower_limit: float

class ObservationCreate(ObservationBase):
    pass

class Observation(ObservationBase):
    id: int

    class Config:
        orm_mode = True
