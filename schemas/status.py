"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from pydantic import BaseModel

class StatusResponse(BaseModel):
    status: str
    version: str
    health: str
    attribution: str
