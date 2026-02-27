"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

import os
from typing import Dict, List, Tuple

REQUIRED_SECTIONS = {
    "implementation": [
        "# Implementation Plan:",
        "## User Review Required",
        "## Proposed Changes",
        "## Verification Plan",
        "## Acceptance Criteria"
    ],
    "task": [
        "# AiTDL Task Document:",
        "## Task Breakdown",
        "- [ ]"
    ],
    "walkthrough": [
        "# AiTDL Walkthrough Document:",
        "## Architecture Summary",
        "## Execution Flow",
        "## File-Level Impact",
        "## System Impact"
    ]
}

class StructureValidator:
    """
    Validates the existence and structural integrity of generated documentation.
    Enforces v1.5 STABLE standards.
    """

    def validate_set(self, doc_paths: Dict[str, str]) -> Tuple[bool, str]:
        """
        Validates all three documents in the set.
        """
        expected_keys = ["implementation_path", "task_path", "walkthrough_path"]
        
        # 1. Check if exactly 3 documents are present
        if len(doc_paths) != 3 or not all(k in doc_paths for k in expected_keys):
            return False, "Missing mandatory documentation paths (exactly 3 required)."

        for key, path in doc_paths.items():
            doc_type = key.replace("_path", "")
            
            # 2. Check file existence
            if not os.path.exists(path):
                return False, f"Document file not found: {path}"

            # 3. Check folder mapping
            folder = os.path.dirname(path)
            subfolder = os.path.basename(folder)
            
            # Special case for 'Walkthrough' folder case sensitivity
            expected_folder = "Walkthrough" if doc_type == "walkthrough" else doc_type
            if subfolder != expected_folder:
                return False, f"Incorrect folder mapping for {doc_type}: expected {expected_folder}, got {subfolder}"

            # 4. Check contents
            is_valid, error = self._validate_content(doc_type, path)
            if not is_valid:
                return False, error

        return True, ""

    def _validate_content(self, doc_type: str, path: str) -> Tuple[bool, str]:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.strip():
            return False, f"Document is empty: {path}"

        # Check for mandatory headers
        required = REQUIRED_SECTIONS.get(doc_type, [])
        for section in required:
            if section not in content:
                return False, f"Missing required section '{section}' in {doc_type} doc."

        # Special rule for Task doc: No explanation paragraphs
        if doc_type == "task":
            # Identify paragraphs that are not headers, not bolded metadata, and not checklist items
            paragraphs = [p for p in content.split("\n\n") if p and not p.strip().startswith("#") and not p.strip().startswith("**") and "- [" not in p]
            
            # Exclude copyright header and license sections from paragraph check
            forbidden_paragraphs = []
            for p in paragraphs:
                p_clean = p.strip()
                if any(x in p_clean for x in ["Copyright", "Jawahar Mallah", "Licensed under", "MIT License"]):
                    continue
                forbidden_paragraphs.append(p_clean)

            if any(len(p.split()) > 10 for p in forbidden_paragraphs):
                 return False, "Task document contains unauthorized explanation paragraphs (v1.5 rules)."

        return True, ""

validator = StructureValidator()
