"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from typing import List, Dict

class PlannerService:
    def generate_study_plan(self, course_title: str, modules: List[str], hours_per_week: int = 10):
        """
        Rule-based simple study planner MVP.
        """
        plan = {
            "course": course_title,
            "weekly_hours": hours_per_week,
            "schedule": []
        }
        
        # Simple distribution: 2 modules per week if time allowed
        week = 1
        for i in range(0, len(modules), 2):
            week_modules = modules[i:i+2]
            plan["schedule"].append({
                "week": week,
                "topics": week_modules,
                "recommended_focus": "Practical exercises and module review."
            })
            week += 1
            
        return plan
