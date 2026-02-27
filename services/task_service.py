"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from typing import List, Dict, Any

class TaskService:
    def __init__(self):
        self._tasks = []

    def create_task(self, data: Dict[str, Any]) -> Dict[str, Any]:
        task = {
            "id": len(self._tasks) + 1,
            "title": data.get("title", "Untitled Task"),
            "status": "created"
        }
        self._tasks.append(task)
        return task

    def get_tasks(self) -> List[Dict[str, Any]]:
        return self._tasks

task_service = TaskService()
