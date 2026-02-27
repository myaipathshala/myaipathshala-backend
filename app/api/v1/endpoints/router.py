"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from fastapi import APIRouter, HTTPException
from app.core.ai_agent import ai_agent
from app.api.v1.endpoints import health

router = APIRouter()

# Include sub-routers
router.include_router(health.router, tags=["Health"])

@router.post("/execute")
async def execute_intent(intent: str, params: dict = {}):
    """
    Structured execution through AiTDL Orchestration Layer.
    """
    response = await ai_agent.execute_command(intent, params)
    
    if response.status == "error":
        raise HTTPException(status_code=400, detail=response.message)
        
    return response.model_dump()

@router.get("/status")
async def get_status():
    """
    Legacy status endpoint routed through AiTDL Layer for consistency.
    Note: 'analyze_project' is used here as an example master intent.
    """
    # For educational purposes, mapping status to 'analyze_project'
    response = await ai_agent.execute_command("analyze_project", {"target": "system_status"})
    return response.model_dump()
