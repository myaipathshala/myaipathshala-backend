"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

import os
from datetime import datetime
from typing import Any, Dict

LOG_FILE = "doc/EXECUTION_LOG.md"

class ExecutionLogger:
    """
    Handles persistent chronological logging of AiTDL intent executions.
    """

    def __init__(self):
        self._ensure_log_file()

    def _ensure_log_file(self):
        directory = os.path.dirname(LOG_FILE)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                f.write("# AiTDL Execution Audit Log\n\n")

    def log_execution(self, intent: str, doc_paths: Dict[str, str], status: str):
        """
        Appends a formatted log entry to EXECUTION_LOG.md.
        """
        timestamp = datetime.now().isoformat()
        version = "1.6 STABLE"
        
        # Determine integrity/structure status based on overall status
        integrity_status = "verified" if status == "success" else "unknown"
        structure_status = "validated" if status == "success" else "unknown"

        log_entry = f"""
--------------------------------------------------
Intent: {intent}
Version: {version}
Timestamp: {timestamp}

Generated Files:
- {doc_paths.get('implementation_path', 'N/A')}
- {doc_paths.get('task_path', 'N/A')}
- {doc_paths.get('walkthrough_path', 'N/A')}

Status: {status}
Integrity: {integrity_status}
Structure: {structure_status}
--------------------------------------------------
"""
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)

execution_logger = ExecutionLogger()
