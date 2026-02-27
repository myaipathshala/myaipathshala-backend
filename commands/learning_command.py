"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from app.services.learning_service import LearningService
from app.core.database import SessionLocal
from agent.interfaces import BaseCommand

class LearningCommand(BaseCommand):
    async def execute(self, params: dict):
        action = params.get("action")
        db = SessionLocal()
        service = LearningService(db)
        
        try:
            if action == "create_course":
                course = service.create_course(params["title"], params["description"])
                return {"status": "success", "course_id": course.id}
            
            elif action == "add_module":
                module = service.add_module(params["course_id"], params["title"], params["order"])
                return {"status": "success", "module_id": module.id}
            
            elif action == "add_lesson":
                lesson = service.add_lesson(params["module_id"], params["title"], params["content"], params["order"])
                return {"status": "success", "lesson_id": lesson.id}
            
            elif action == "enroll":
                enrollment = service.enroll_user(params["user_id"], params["course_id"])
                return {"status": "success", "enrollment_id": enrollment.id}
            
            elif action == "complete_lesson":
                progress = service.mark_lesson_complete(params["user_id"], params["lesson_id"])
                return {"status": "success", "message": "Lesson marked complete."}
            
            elif action == "get_progress":
                percent = service.get_user_progress(params["user_id"], params["course_id"])
                return {"status": "success", "progress_percentage": percent}
                
            else:
                return {"status": "error", "message": f"Unknown learning action: {action}"}
        finally:
            db.close()
