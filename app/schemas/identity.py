"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
"""

from pydantic import BaseModel, Field
from typing import Any, Dict, Optional
from enum import Enum

class IdentityAction(str, Enum):
    REGISTER = "register"
    LOGIN = "login"
    VERIFY = "verify"

class IdentityRequest(BaseModel):
    action: IdentityAction = Field(..., description="The identity action to perform (e.g., register, login)")
    params: Dict[str, Any] = Field(default_factory=dict, description="Action-specific parameters (username, password, etc.)")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Client metadata (browser, IP, etc.)")
