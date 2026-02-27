"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from app.services.planner_service import PlannerService
from agent.interfaces import BaseCommand

class PlannerCommand(BaseCommand):
    async def execute(self, params: dict):
        service = PlannerService()
        plan = service.generate_study_plan(
            course_title=params["course_title"],
            modules=params["modules"],
            hours_per_week=params.get("hours_per_week", 10)
        )
        return {"status": "success", "study_plan": plan}
