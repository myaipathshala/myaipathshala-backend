"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseCommand(ABC):
    @abstractmethod
    async def execute(self, params: Dict[str, Any]) -> Any:
        pass
