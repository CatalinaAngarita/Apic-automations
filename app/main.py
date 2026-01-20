"""
Punto de entrada de FastAPI
"""
from fastapi import FastAPI

app = FastAPI(
    title="Repoc Automations API",
    description="API para automatizaciones",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Repoc Automations API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
