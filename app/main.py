from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
def read_root():
    return {
        "message": f"Bienvenido a {settings.PROJECT_NAME}",
        "n8n_target": settings.N8N_WEBHOOK_URL
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
