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

router = APIRouter()

# Initialize Database on startup
init_db()

@router.post("/identity")
async def identity_actions(params: dict):
    """
    Orchestrated Identity Actions (register, etc.)
    """
    return await ai_agent.execute_command("manage_identity", params)

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
