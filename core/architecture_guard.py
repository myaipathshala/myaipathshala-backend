"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

import os
from typing import Dict, List

ALLOWED_ROOTS = ["app/", "agent/", "doc/", "tests/", "requirements.txt", "README.md", "pyproject.toml", ".env"]

class ArchitectureViolation(Exception):
    """Raised when an architectural principle is violated."""
    pass

class ArchitectureGuard:
    """
    Prevents AiTDL architectural principle violations.
    Enforces v1.7 STABLE standards.
    """

    def validate_path(self, path: str):
        """Ensures file operations stay within allowed directories."""
        # Normalize path
        norm_path = path.replace("\\", "/")
        
        # Check if path is in allowed roots
        is_allowed = any(norm_path.startswith(root) for root in ALLOWED_ROOTS)
        
        if not is_allowed and not os.path.abspath(path).startswith(os.getcwd()):
            raise ArchitectureViolation(f"Path violation detected: '{path}' is outside restricted zones.")

    def validate_flow(self, intent: str, doc_paths: Dict[str, str]):
        """Ensures all mandatory docs exist before execution."""
        required = ["implementation_path", "task_path", "walkthrough_path"]
        for key in required:
            path = doc_paths.get(key)
            if not path or not os.path.exists(path):
                raise ArchitectureViolation(f"Execution flow violation: Mandatory document '{key}' is missing or ungenerated.")

    def check_layer_violations(self):
        """
        Simple runtime check for direct service imports in the API layer.
        (Note: In a real app, this would be part of a build/test step)
        """
        api_dir = "app/api"
        if not os.path.exists(api_dir):
            return

        for root, _, files in os.walk(api_dir):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if "from app.services" in content or "import app.services" in content:
                            raise ArchitectureViolation(f"Layer violation in '{path}': API layer cannot import from services directly.")

guard = ArchitectureGuard()
