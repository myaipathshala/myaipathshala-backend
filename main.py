"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import learning

from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from app.core.config import settings

app = FastAPI(
    title="MYAIPATHSHALA Learning Engine API", 
    version="0.1",
    docs_url="/docs" if not settings.is_production else None,
    redoc_url="/redoc" if not settings.is_production else None,
)

# Enforce HTTPS in production
if settings.is_production:
    app.add_middleware(HTTPSRedirectMiddleware)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(learning.router, prefix="/api/v1", tags=["learning"])

@app.get("/")
async def root():
    return {"message": "Welcome to MYAIPATHSHALA Learning Engine API (AiTDL-Driven)"}
