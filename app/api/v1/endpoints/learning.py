"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from fastapi import APIRouter, Depends
from app.core.ai_agent import ai_agent
from app.core.database import init_db
from app.schemas.identity import IdentityRequest

router = APIRouter()

# Initialize Database on startup
init_db()

@router.post("/identity")
async def identity_actions(request: IdentityRequest):
    """
    Orchestrated Identity Actions (register, login, verify)
    """
    # Merge action into parameters for the AIAgent layer
    params = request.params.copy()
    params["action"] = request.action
    return await ai_agent.execute_command("manage_identity", params)

@router.get("/identity")
async def identity_health():
    """
    Health check and connectivity test for Identity route.
    """
    return {"status": "ok", "route": "/api/v1/identity", "methods": ["GET", "POST"]}

@router.post("/learning")
async def learning_actions(params: dict):
    """
    Orchestrated Learning Actions (courses, progress, enrollment)
    """
    return await ai_agent.execute_command("manage_learning", params)

@router.post("/planner")
async def planner_actions(params: dict):
    """
    Orchestrated Study Planning Actions
    """
    return await ai_agent.execute_command("manage_planner", params)
