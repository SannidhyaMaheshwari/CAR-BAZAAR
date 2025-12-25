from fastapi import FastAPI

app = FastAPI(title="CAR-BAZAAR API")

@app.get("/")
def root():
    return {"message": "CAR-BAZAAR backend is running"}
