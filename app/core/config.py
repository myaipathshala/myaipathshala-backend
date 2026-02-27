"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "myaipathshala-fastapi-starter"
    API_V1_STR: str = "/api/v1"
    # Default: SQLite for local dev. Override DATABASE_URL in .env or Render env vars for PostgreSQL
    DATABASE_URL: str = "sqlite:///./myaipathshala.db"
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://myaipathshala.vercel.app",
        "https://myaipathshala-7p60rpbdw-myaipathshalas.vercel.app",
        "https://myaipathshala-frontend.vercel.app",
        "https://www.myaipathshala.com",
        "https://myaipathshala.com",
    ]
    ENV: str = "development"
    SECRET_KEY: str = "change-me-in-production-use-a-strong-random-key"

    @property
    def is_production(self) -> bool:
        return self.ENV == "production"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
