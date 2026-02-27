"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

import logging
from datetime import datetime
from typing import Any, Dict
from app.core.database import SessionLocal
from app.core.models import ExecutionLog

logger = logging.getLogger("execution_logger")

class ExecutionLogger:
    """
    Handles persistent database logging of AiTDL intent executions.
    Replaces local disk-based doc/EXECUTION_LOG.md.
    """

    def log_execution(self, intent: str, doc_data: Dict[str, Any], status: str, error_message: str = None):
        """
        Persists a formatted log entry to the database.
        """
        db = SessionLocal()
        try:
            docs = doc_data.get("documents", {})
            log_entry = ExecutionLog(
                intent=intent,
                status=status,
                integrity_verified=(status == "success"),
                structure_validated=(status == "success"),
                implementation_content=docs.get("implementation", {}).get("content"),
                task_content=docs.get("task", {}).get("content"),
                walkthrough_content=docs.get("walkthrough", {}).get("content"),
                error_message=error_message
            )
            db.add(log_entry)
            db.commit()
            logger.info(f"Execution logged to DB: {intent} [{status}]")
        except Exception as e:
            db.rollback()
            logger.error(f"Stateless fallback: Failed to log to DB: {e}")
            # Fallback to standard logging for serverless safety
            print(f"--- [FALLBACK LOG] ---")
            print(f"Intent: {intent} | Status: {status} | Error: {error_message}")
        finally:
            db.close()

execution_logger = ExecutionLogger()
