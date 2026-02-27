"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from typing import Any, Dict
from app.core import aitdl_protocol
from app.core.planner import planner
from agent.base import agent_manager

class AIAgent:
    """
    The AiTDL Orchestration Layer.
    All execution must flow through this agent.
    """

    async def execute_command(self, intent: str, params: Dict[str, Any]) -> aitdl_protocol.AiTDLResponse:
        # 1. Validate Intent
        if not aitdl_protocol.validate_intent(intent):
            return aitdl_protocol.format_error(
                intent=intent,
                message=f"Invalid intent: {intent}. Allowed master intents only."
            )

        # 2. Planning Phase (v1.5 STABLE: 3 Docs Mandatory)
        doc_paths = planner.generate_documentation_set(intent, params)
        print(f"Documentation set generated in {planner.DOC_ROOT}")

        # 3. Structure Validation Phase (v1.5 STABLE Requirement)
        from app.core.validator import validator
        is_valid, error_msg = validator.validate_set(doc_paths)
        
        if not is_valid:
            print(f"Structure validation FAILED: {error_msg}")
            return aitdl_protocol.format_error(
                intent=intent,
                message=f"Documentation Structure Validation Failed: {error_msg}"
            )
        
        print("Structure validation SUCCESSFUL.")

        try:
            # 4. Architecture Guard Phase (v1.7 STABLE)
            from app.core.architecture_guard import guard
            guard.validate_flow(intent, doc_paths)
            guard.check_layer_violations()
            print("Architecture Guard checks PASSED.")

            # 5. Execution Phase
            result = await agent_manager.run(intent, params)
            
            # 6. Log Execution (v1.6 STABLE)
            from app.core.execution_logger import execution_logger
            execution_logger.log_execution(intent, doc_paths, "success")

            # 6. Return Structured Response (v1.5 STABLE)
            return aitdl_protocol.format_success(
                intent=intent,
                data={
                    "result": result,
                    "integrity_verified": True,
                    "structure_validated": True
                },
                implementation_doc_path=doc_paths.get("implementation_path"),
                task_doc_path=doc_paths.get("task_path"),
                walkthrough_doc_path=doc_paths.get("walkthrough_path")
            )
        except Exception as e:
            # Log violation attempt if it's an ArchitectureViolation
            if "ArchitectureViolation" in str(type(e)):
                print(f"CRITICAL VIOLATION DETECTED: {e}")
                from app.core.execution_logger import execution_logger
                execution_logger.log_execution(intent, doc_paths, "CRITICAL_VIOLATION_FAILED")
            
            return aitdl_protocol.format_error(
                intent=intent,
                message=str(e)
            )

ai_agent = AIAgent()
