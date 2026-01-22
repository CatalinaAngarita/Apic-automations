from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Apic Automations"
    DATABASE_URL: str = "sqlite:///./app.db"
    N8N_WEBHOOK_URL: str = "https://tu-n8n-instance.com/webhook"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()