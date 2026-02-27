"""
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""

from enum import Enum

class MasterIntent(str, Enum):
    INIT_PROJECT = "init_project"
    DEVELOP_PROJECT = "develop_project"
    ADD_FEATURE = "add_feature"
    REFACTOR_PROJECT = "refactor_project"
    ANALYZE_PROJECT = "analyze_project"
    FINALIZE_PROJECT = "finalize_project"
    LOCK_FRAMEWORK = "lock_framework"
    
    # MYAIPATHSHALA MVP Intents
    MANAGE_IDENTITY = "manage_identity"
    MANAGE_LEARNING = "manage_learning"
    MANAGE_PLANNER = "manage_planner"
