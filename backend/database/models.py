from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# ── Student Profile ──────────────────────────────────────────

class StudentProfile(BaseModel):
    id: str
    name: str
    email: str
    skills: List[str]
    interests: List[str]
    github_username: str
    github_repos: List[str] = []
    github_languages: dict = {}  # {"Python": 3, "JavaScript": 2}
    experience_level: str  # beginner / intermediate / advanced
    availability: bool = True
    department: str
    year: int  # 1-4
    previous_projects: List[str] = []
    match_score: Optional[float] = None


class StudentCreate(BaseModel):
    name: str
    email: str
    skills: List[str]
    interests: List[str]
    github_username: str
    experience_level: str = "beginner"
    availability: bool = True
    department: str
    year: int
    previous_projects: List[str] = []


# ── Business Request / PRD ────────────────────────────────────

class BusinessRequest(BaseModel):
    id: str
    business_name: str
    owner_name: str
    email: str
    description: str
    prd: Optional[str] = None  # Generated PRD markdown
    tech_stack: Optional[dict] = None  # From solution architect
    quality_score: Optional[int] = None  # Quality review score out of 100
    status: str = "submitted"  # submitted / in_review / matched / in_progress / completed
    created_at: str = ""
    matched_students: List[str] = []
    project_id: Optional[str] = None


class BusinessRequestCreate(BaseModel):
    business_name: str
    owner_name: str
    email: str
    description: str


# ── Project ───────────────────────────────────────────────────

class Project(BaseModel):
    id: str
    business_request_id: str
    business_name: str
    title: str
    description: str
    assigned_students: List[str]  # student IDs
    tech_stack: dict = {}
    milestones: List[dict] = []
    status: str = "planning"  # planning / in_progress / completed / on_hold
    progress: float = 0.0  # 0-100
    created_at: str = ""
    updated_at: str = ""
    deadline: Optional[str] = None


class ProjectCreate(BaseModel):
    business_request_id: str
    title: str
    description: str
    assigned_students: List[str]
    tech_stack: dict = {}
    deadline: Optional[str] = None


# ── Match Result ─────────────────────────────────────────────

class MatchResult(BaseModel):
    student: StudentProfile
    score: float
    skill_match: List[str]
    missing_skills: List[str]
    reason: str
