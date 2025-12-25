from fastapi import FastAPI
from app.auth.routes import router as auth_router

app = FastAPI(title="CAR-BAZAAR API")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "CAR-BAZAAR backend is running"}
