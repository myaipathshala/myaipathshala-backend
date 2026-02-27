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
from sqlalchemy.exc import IntegrityError

class IdentityCommand(BaseCommand):
    async def execute(self, params: dict):
        action = params.get("action")
        db = SessionLocal()
        service = LearningService(db)
        
        try:
            if action == "register":
                try:
                    user = service.create_user(
                        username=params["username"],
                        email=params["email"],
                        password=params["password"],
                        role=params.get("role", "student")
                    )
                    return {"status": "success", "user_id": user.id, "message": "User registered successfully."}
                except IntegrityError:
                    db.rollback()
                    return {"status": "error", "message": "Username or email already exists."}
            else:
                return {"status": "error", "message": f"Unknown identity action: {action}"}
        finally:
            db.close()
