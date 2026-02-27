"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author
"""

import sys
import os

# Add the app directory to the path so we can import app modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.core.database import SessionLocal, init_db
from app.services.learning_service import LearningService
from app.core.models import User, Course

def seed():
    print("🌱 Initializing Database...")
    init_db()
    db = SessionLocal()
    service = LearningService(db)

    try:
        # 1. Create Sample User
        print("👤 Creating Sample User...")
        existing_user = db.query(User).filter(User.username == "admin").first()
        if not existing_user:
            user = service.create_user(
                username="admin", 
                email="admin@myaipathshala.com", 
                password="admin123", 
                role="admin"
            )
            print(f"✅ User 'admin' created (ID: {user.id})")
        else:
            print("ℹ️ User 'admin' already exists.")

        # 2. Create Sample Courses
        print("📚 Creating Sample Courses...")
        courses_data = [
            {
                "title": "Python for AI Beginners",
                "description": "Master the basics of Python optimized for AI system development.",
                "modules": [
                    {"title": "Introduction to Python", "lessons": ["Hello World", "Data Types"]},
                    {"title": "AI Libraries", "lessons": ["NumPy Basics", "Pandas Overview"]}
                ]
            },
            {
                "title": "Advanced AiTDL Architecture",
                "description": "Deep dive into the AiTDL protocol and orchestration patterns.",
                "modules": [
                    {"title": "AiTDL Protocol", "lessons": ["Understanding Intents", "Response Structures"]},
                    {"title": "Hardening Layer", "lessons": ["Architecture Guard", "Stateless Orchestration"]}
                ]
            }
        ]

        for c_data in courses_data:
            existing_course = db.query(Course).filter(Course.title == c_data["title"]).first()
            if not existing_course:
                course = service.create_course(c_data["title"], c_data["description"])
                print(f"✅ Course '{course.title}' created.")
                
                for i, m_data in enumerate(c_data["modules"]):
                    module = service.add_module(course.id, m_data["title"], i + 1)
                    for j, l_title in enumerate(m_data["lessons"]):
                        service.add_lesson(module.id, l_title, f"Content for {l_title}", j + 1)
            else:
                print(f"ℹ️ Course '{c_data['title']}' already exists.")

        print("✨ Seeding Complete!")

    except Exception as e:
        print(f"❌ Seeding Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
