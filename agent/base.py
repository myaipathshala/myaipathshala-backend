"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from typing import Any, Dict
from agent.interfaces import BaseCommand

class AgentInterpreter:
    def interpret(self, intent: str) -> str:
        # Map master intents to internal command names
        mapping = {
            "get_status": "status_command",
            "analyze_project": "status_command",
            "finalize_project": "status_command",
            "lock_framework": "status_command",
            "process_data": "data_command"
        }
        return mapping.get(intent, "unknown")

class AgentManager:
    def __init__(self):
        self._commands = {}
        # Pre-register some commands for educational purposes (v2.0 STABLE)
        from agent.commands.status import StatusCommand
        
        # All master intents map to a demo command in this template
        intents = [
            "init_project", "develop_project", "add_feature", 
            "refactor_project", "analyze_project", "finalize_project", 
            "lock_framework"
        ]
        
        for intent in intents:
            self.register_command(intent, StatusCommand())
        
        # Legacy mappings
        self.register_command("status_command", StatusCommand())

        # Register Specialized Learning Engine MVP Commands
        from agent.commands.identity_command import IdentityCommand
        from agent.commands.learning_command import LearningCommand
        from agent.commands.planner_command import PlannerCommand

        self.register_command("manage_identity", IdentityCommand())
        self.register_command("manage_learning", LearningCommand())
        self.register_command("manage_planner", PlannerCommand())

    def register_command(self, name: str, command: BaseCommand):
        self._commands[name] = command

    async def run(self, command_name: str, params: Dict[str, Any]) -> Any:
        command = self._commands.get(command_name)
        if not command:
            raise ValueError(f"Command {command_name} not found")
        return await command.execute(params)

agent_interpreter = AgentInterpreter()
agent_manager = AgentManager()
