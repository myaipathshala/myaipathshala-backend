"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from agent.commands.master_intents import MasterIntent

class AiTDLCommand(BaseModel):
    intent: MasterIntent
    params: Dict[str, Any] = Field(default_factory=dict)

class AiTDLResponse(BaseModel):
    status: str
    intent: str
    data: Dict[str, Any] = Field(default_factory=dict)
    message: Optional[str] = None
    implementation_doc_path: Optional[str] = None
    task_doc_path: Optional[str] = None
    walkthrough_doc_path: Optional[str] = None

def validate_intent(intent: str) -> bool:
    """Validates if the provided intent is a supported MasterIntent."""
    return intent in [item.value for item in MasterIntent]

def format_error(intent: str, message: str) -> AiTDLResponse:
    """Formats a standard error response."""
    return AiTDLResponse(
        status="error",
        intent=intent,
        message=message
    )

def format_success(
    intent: str, 
    data: Dict[str, Any], 
    message: Optional[str] = None,
    implementation_doc_path: Optional[str] = None,
    task_doc_path: Optional[str] = None,
    walkthrough_doc_path: Optional[str] = None
) -> AiTDLResponse:
    """Formats a standard success response with documentation paths."""
    return AiTDLResponse(
        status="success",
        intent=intent,
        data=data,
        message=message,
        implementation_doc_path=implementation_doc_path,
        task_doc_path=task_doc_path,
        walkthrough_doc_path=walkthrough_doc_path
    )
