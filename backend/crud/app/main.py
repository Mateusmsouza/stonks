from fastapi import FastAPI
from app.routes.observation_router import ObservationRouter

app = FastAPI(title="Crypto Monitor API")

# Register routes
observation_router = ObservationRouter()
app.include_router(observation_router.router, prefix="/observations", tags=["Observations"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Crypto Monitor API"}
