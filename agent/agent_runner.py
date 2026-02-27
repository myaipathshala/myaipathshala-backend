"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from typing import Any, Dict
from agent.base import agent_manager

class AgentRunner:
    """
    Executes commands through the agent_manager.
    Acts as the bridge between AiTDL layer and Agent Layer.
    """
    
    async def run_intent(self, intent: str, params: Dict[str, Any]) -> Any:
        return await agent_manager.run(intent, params)

agent_runner = AgentRunner()
