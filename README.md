# myaipathshala-fastapi-starter v1.3 STABLE

An educational template for FastAPI applications following the AiTDL-driven architecture.

## AiTDL v1.3 STABLE Release Notes
- **Intent-based architecture**: Strict enforcement of master intents.
- **Planning engine**: Integrated auto-generation of documentation.
- **3-Doc Rule**: Every intent generates Implementation, Task, and Walkthrough docs.
- **Structured contract**: Predictable JSON response mapping.
- **MIT Licensed**: Open educational foundation.

## Features
- FastAPI based backend (v1.3 STABLE)
- AiTDL Agent Layer for intent-based execution
- Mandatory 3-Doc Planning System (`doc/`)
- Modular structure (API, Agent, Services, Schemas)
- Educational focus and MIT compliant

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`
4. Run the application: `uvicorn app.main:app --reload`

## AiTDL v1.3 Architecture

API Layer → AiTDL Layer → Planner Layer (3 Docs) → Guard Layer → Service Layer → Documentation Layer

No service is executed directly. Every action must pass through the AiTDL orchestration, planning, and guard layer.

## Architecture Guard Layer v1.7
AiTDL enforces structural discipline. Any violation of architectural principles (e.g., direct API-to-Service imports, unauthorized path access) results in immediate execution termination and is logged as a critical violation.

### Supported Master Intents

- `init_project`
- `develop_project`
- `add_feature`
- `refactor_project`
- `analyze_project`
- `finalize_project`
- `lock_framework`

### Response Structure (v1.3 STABLE)

```json
{
  "status": "success | error",
  "intent": "string",
  "data": {},
  "message": "optional string",
  "implementation_doc_path": "string",
  "task_doc_path": "string",
  "walkthrough_doc_path": "string"
}
```

---
Copyright (c) 2026 MYAIPATHSHALA.com | AITDL.com

Founded by Jawahar Mallah
AI System Architect & Author

Licensed under the MIT License.
See LICENSE file in the project root for full license information.
