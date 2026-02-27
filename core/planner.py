"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

import os
from datetime import datetime
from typing import Any, Dict, List, Tuple

DOC_ROOT = "doc"
SUBFOLDERS = ["implementation", "task", "Walkthrough"]

INTENT_TITLES = {
    "init_project": "Project Initialization",
    "develop_project": "Project Development",
    "add_feature": "Feature Addition",
    "refactor_project": "Code Refactoring",
    "analyze_project": "System Analysis",
    "finalize_project": "Project Finalization",
    "lock_framework": "Framework Stabilization"
}

class Planner:
    """
    The Planning System for AiTDL v2.0 STABLE.
    Generates three mandatory documents for every intent with enterprise formatting.
    """
    DOC_ROOT = DOC_ROOT
    VERSION = "1.5"
    STATUS = "STABLE"

    def __init__(self):
        self._ensure_directories()

    def _ensure_directories(self):
        if not os.path.exists(DOC_ROOT):
            os.makedirs(DOC_ROOT)
        for folder in SUBFOLDERS:
            path = os.path.join(DOC_ROOT, folder)
            if not os.path.exists(path):
                os.makedirs(path)

    def generate_documentation_set(self, intent: str, params: Dict[str, Any]) -> Dict[str, str]:
        """
        Generates mandatory set of 3 documents.
        Returns a dictionary of paths.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        paths = {}

        for folder in SUBFOLDERS:
            filename = f"{intent}_{timestamp}.md"
            filepath = os.path.join(DOC_ROOT, folder, filename)
            
            content = self._create_template(folder, intent, params, timestamp)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            paths[f"{folder.lower()}_path"] = filepath

        return paths

    def _create_template(self, doc_type: str, intent: str, params: Dict[str, Any], timestamp: str) -> str:
        intent_title = INTENT_TITLES.get(intent, intent.replace("_", " ").title())
        
        header = f"""Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.

"""
        if doc_type == "implementation":
            title = f"# Implementation Plan: {intent_title} v{self.VERSION} {self.STATUS}"
            intro = f"""This document outlines the architectural strategy and technical specifications for the `{intent}` operation. 
It defines the scope of modifications within the AiTDL framework to ensure systemic integrity and modular purity."""
            
            body = f"""{title}

{intro}

## User Review Required
The following architectural considerations warrant stakeholder review:
- Standard parameter validation for `{intent}` will be enforced.
- Execution will be logged as a unique immutable documentation set in `doc/`.

## Proposed Changes
### Core System Integration
- Intent mapping confirmed for `{intent}`.
- Payload parameters: {', '.join([f'{k}={v}' for k, v in params.items()]) or 'None'}.
- Documentation set generation triggered across three mandatory layers.

## Verification Plan
### Automated Tests
- Intent validation logic check.
- Documentation path availability check.
- Payload structure integrity test.

### Manual Verification
- Review auto-generated markdown files for structural compliance.
- Audit the execution logs in the documentation layer.

## Acceptance Criteria
- All 3 documentation files generated successfully.
- Logic execution returns status code 200 or equivalent success signal.
- Response payload matches AiTDL v{self.VERSION} STABLE schema.
"""
        elif doc_type == "task":
            body = f"""# AiTDL Task Document: {intent_title}

**Timestamp:** {timestamp}
**Intent Name:** {intent}
**Execution Flow:** API Layer → AiTDL Layer → Planner Layer → Service Layer → Documentation Layer

## Task Breakdown
- [ ] Initialize Environment
- [ ] Validate AiTDL Protocol
- [ ] Generate Documentation Set (3 Docs)
- [ ] Execute Core Logic
- [ ] Aggregate Results
"""
        else:  # Walkthrough
            body = f"""# AiTDL Walkthrough Document: {intent_title}

**Timestamp:** {timestamp}
**Intent Name:** {intent}
**Execution Flow:** API Layer → AiTDL Layer → Planner Layer → Service Layer → Documentation Layer

## Architecture Summary
- System leverages standardized AiTDL orchestration.
- Integration verified against version {self.VERSION} STABLE rules.

## Execution Flow
1. Intent interpreted as `{intent}`.
2. Planner generated mandatory documentation in `doc/`.
3. System status checked for stability.
4. Final response formatted to AiTDL v{self.VERSION} {self.STATUS} standard.

## File-Level Impact
- New markdown artifacts created in `doc/` subfolders.
- Response structure metadata updated.

## System Impact
- Enhanced observability via structured documentation.
- Framework integrity reinforced through mandatory planning step.
"""
        return header + body

planner = Planner()
