"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from sqlalchemy.orm import Session
from app.core.models import User, Course, Module, Lesson, Enrollment, UserProgress
from datetime import datetime
from typing import List, Dict, Any

class LearningService:
    def __init__(self, db: Session):
        self.db = db

    # Identity Layer
    def create_user(self, username: str, email: str, password: str, role: str = "student"):
        user = User(username=username, email=email, hashed_password=password, role=role) # In MVP, plain text/simple hash
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    # Course Engine
    def create_course(self, title: str, description: str):
        course = Course(title=title, description=description)
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def add_module(self, course_id: int, title: str, order: int):
        module = Module(course_id=course_id, title=title, order=order)
        self.db.add(module)
        self.db.commit()
        self.db.refresh(module)
        return module

    def add_lesson(self, module_id: int, title: str, content: str, order: int):
        lesson = Lesson(module_id=module_id, title=title, content=content, order=order)
        self.db.add(lesson)
        self.db.commit()
        self.db.refresh(lesson)
        return lesson

    def enroll_user(self, user_id: int, course_id: int):
        enrollment = Enrollment(user_id=user_id, course_id=course_id)
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)
        return enrollment

    # Progress Tracking
    def mark_lesson_complete(self, user_id: int, lesson_id: int):
        progress = UserProgress(user_id=user_id, lesson_id=lesson_id, is_completed=True, completed_at=datetime.utcnow())
        self.db.add(progress)
        self.db.commit()
        self.db.refresh(progress)
        return progress

    def get_user_progress(self, user_id: int, course_id: int):
        # Calculate progress percentage
        course = self.db.query(Course).filter(Course.id == course_id).first()
        if not course:
            return 0.0
        
        total_lessons = self.db.query(Lesson).join(Module).filter(Module.course_id == course_id).count()
        if total_lessons == 0:
            return 0.0
            
        completed_lessons = self.db.query(UserProgress).join(Lesson).join(Module).filter(
            UserProgress.user_id == user_id, 
            Module.course_id == course_id,
            UserProgress.is_completed == True
        ).count()
        
        return (completed_lessons / total_lessons) * 100
