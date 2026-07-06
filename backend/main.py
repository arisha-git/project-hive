from datetime import datetime, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database.mock_data import db
from database.models import (
    BusinessRequest,
    BusinessRequestCreate,
    Project,
    ProjectCreate,
    StudentCreate,
    StudentProfile,
)

app = FastAPI(title="ProjectHive API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _next_id(prefix: str, existing: dict) -> str:
    count = len(existing) + 1
    return f"{prefix}-{count:03d}"


def _build_match_reason(student: StudentProfile, matched_skills: list[str], missing_skills: list[str]) -> str:
    if matched_skills:
        return f"Strong fit based on {', '.join(matched_skills[:3])}."
    if missing_skills:
        return f"Good general baseline with a few gaps in {', '.join(missing_skills[:2])}."
    return "Broadly suitable for the requested project scope."


def _score_student(student: StudentProfile, description: str) -> tuple[float, list[str], list[str], str]:
    text = description.lower()
    matched_skills: list[str] = []
    missing_skills: list[str] = []

    keyword_map = {
        "website": ["React", "JavaScript", "HTML", "CSS", "TypeScript", "Next.js"],
        "web": ["React", "JavaScript", "HTML", "CSS", "TypeScript", "Next.js"],
        "api": ["Python", "FastAPI", "Node.js", "Express", "Django", "Flask"],
        "backend": ["Python", "FastAPI", "Node.js", "Express", "Django", "Flask"],
        "database": ["SQL", "MongoDB", "PostgreSQL", "SQLite"],
        "order": ["React", "Node.js", "Express", "MongoDB", "SQL"],
        "payment": ["React", "Node.js", "Express", "MongoDB", "SQL"],
        "admin": ["Python", "Node.js", "React", "SQL"],
        "deploy": ["Docker", "Kubernetes", "Cloud", "DevOps"],
    }

    for keyword, skills in keyword_map.items():
        if keyword in text:
            for skill in skills:
                if skill in student.skills:
                    matched_skills.append(skill)

    matched_skills = list(dict.fromkeys(matched_skills))
    if not matched_skills:
        matched_skills = [student.skills[0]] if student.skills else []

    score = 1.0 + (0.5 if student.availability else 0.0)
    score += min(len(matched_skills), 4) * 0.6
    score += 0.4 if student.experience_level == "advanced" else 0.2 if student.experience_level == "intermediate" else 0.1

    if "React" in matched_skills or "TypeScript" in matched_skills:
        missing_skills.append("Frontend UI")
    if "FastAPI" in matched_skills or "Node.js" in matched_skills or "Express" in matched_skills:
        missing_skills.append("Backend APIs")
    if "MongoDB" in matched_skills or "PostgreSQL" in matched_skills or "SQL" in matched_skills:
        missing_skills.append("Database design")

    reason = _build_match_reason(student, matched_skills, missing_skills)
    return round(score, 2), matched_skills, missing_skills, reason


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to ProjectHive API!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "projecthive"}


@app.get("/students", response_model=list[StudentProfile])
def list_students() -> list[StudentProfile]:
    return db.get_all_students()


@app.get("/students/available", response_model=list[StudentProfile])
def list_available_students() -> list[StudentProfile]:
    return db.get_available_students()


@app.get("/students/{student_id}", response_model=Optional[StudentProfile])
def get_student(student_id: str) -> Optional[StudentProfile]:
    return db.get_student(student_id)


@app.post("/students", response_model=StudentProfile)
def create_student(student: StudentCreate) -> StudentProfile:
    student_id = _next_id("stu", db.students)
    new_student = StudentProfile(
        id=student_id,
        name=student.name,
        email=student.email,
        skills=student.skills,
        interests=student.interests,
        github_username=student.github_username,
        github_repos=[],
        github_languages={},
        experience_level=student.experience_level,
        availability=student.availability,
        department=student.department,
        year=student.year,
        previous_projects=student.previous_projects,
    )
    db.add_student(new_student)
    return new_student


@app.put("/students/{student_id}", response_model=StudentProfile)
def update_student(student_id: str, updates: dict) -> StudentProfile:
    updated = db.update_student(student_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated


@app.delete("/students/{student_id}")
def delete_student(student_id: str) -> dict[str, str]:
    student = db.get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.students.pop(student_id, None)
    return {"message": "Student deleted", "student_id": student_id}


@app.get("/business-requests", response_model=list[BusinessRequest])
def list_business_requests() -> list[BusinessRequest]:
    return db.get_all_requests()


@app.get("/business-requests/{request_id}", response_model=Optional[BusinessRequest])
def get_business_request(request_id: str) -> Optional[BusinessRequest]:
    return db.get_request(request_id)


@app.post("/business-requests", response_model=BusinessRequest)
def create_business_request(payload: BusinessRequestCreate) -> BusinessRequest:
    request_id = _next_id("br", db.business_requests)
    new_request = BusinessRequest(
        id=request_id,
        business_name=payload.business_name,
        owner_name=payload.owner_name,
        email=payload.email,
        description=payload.description,
        created_at=datetime.now(timezone.utc).isoformat(),
        status="submitted",
    )
    db.add_request(new_request)
    return new_request


@app.put("/business-requests/{request_id}", response_model=BusinessRequest)
def update_business_request(request_id: str, updates: dict) -> BusinessRequest:
    updated = db.update_request(request_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Business request not found")
    return updated


@app.delete("/business-requests/{request_id}")
def delete_business_request(request_id: str) -> dict[str, str]:
    request = db.get_request(request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Business request not found")
    db.business_requests.pop(request_id, None)
    return {"message": "Business request deleted", "request_id": request_id}


@app.post("/business-requests/{request_id}/match")
def match_students(request_id: str) -> list[dict]:
    request = db.get_request(request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Business request not found")

    matches = []
    for student in db.get_available_students():
        score, matched_skills, missing_skills, reason = _score_student(student, request.description)
        matches.append(
            {
                "student": student.model_dump(),
                "score": score,
                "skill_match": matched_skills,
                "missing_skills": missing_skills,
                "reason": reason,
            }
        )

    matches.sort(key=lambda item: item["score"], reverse=True)
    return matches[:5]


@app.get("/projects", response_model=list[Project])
def list_projects() -> list[Project]:
    return db.get_all_projects()


@app.get("/projects/{project_id}", response_model=Optional[Project])
def get_project(project_id: str) -> Optional[Project]:
    return db.get_project(project_id)


@app.post("/projects", response_model=Project)
def create_project(payload: ProjectCreate) -> Project:
    project_id = _next_id("proj", db.projects)
    request = db.get_request(payload.business_request_id)
    new_project = Project(
        id=project_id,
        business_request_id=payload.business_request_id,
        business_name=request.business_name if request else "",
        title=payload.title,
        description=payload.description,
        assigned_students=payload.assigned_students,
        tech_stack=payload.tech_stack,
        milestones=[{"name": "Initial planning", "status": "pending"}],
        status="planning",
        progress=0.0,
        created_at=datetime.now(timezone.utc).isoformat(),
        updated_at=datetime.now(timezone.utc).isoformat(),
        deadline=payload.deadline,
    )
    db.add_project(new_project)
    return new_project


@app.put("/projects/{project_id}", response_model=Project)
def update_project(project_id: str, updates: dict) -> Project:
    updated = db.update_project(project_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated


@app.delete("/projects/{project_id}")
def delete_project(project_id: str) -> dict[str, str]:
    project = db.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.projects.pop(project_id, None)
    return {"message": "Project deleted", "project_id": project_id}