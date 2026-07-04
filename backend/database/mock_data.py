"""
Mock GitHub profile data and student profiles for ProjectHive.
This provides realistic student data for the Talent Scout Agent matching.
"""

from .models import StudentProfile

# ── Mock Student Profiles ────────────────────────────────────

STUDENTS = [
    StudentProfile(
        id="stu-001",
        name="Ananya Sharma",
        email="ananya.sharma@university.edu",
        skills=["Python", "Flask", "SQL", "JavaScript", "HTML", "CSS"],
        interests=["Web Development", "Backend APIs", "E-commerce"],
        github_username="ananya-sharma-dev",
        github_repos=[
            "ecommerce-api",
            "blog-platform",
            "task-manager-cli",
            "weather-dashboard",
        ],
        github_languages={
            "Python": 4,
            "JavaScript": 2,
            "HTML": 1,
            "CSS": 1,
        },
        experience_level="intermediate",
        availability=True,
        department="Computer Science",
        year=3,
        previous_projects=[
            "Built a REST API for a bookstore using Flask",
            "Developed a CLI task manager with SQLite backend",
        ],
    ),
    StudentProfile(
        id="stu-002",
        name="Rohit Patel",
        email="rohit.patel@university.edu",
        skills=[
            "Python",
            "Django",
            "React",
            "TypeScript",
            "PostgreSQL",
            "Docker",
        ],
        interests=["Full Stack", "Web Apps", "DevOps"],
        github_username="rohit-patel-dev",
        github_repos=[
            "django-blog",
            "react-dashboard",
            "inventory-system",
            "chat-app",
        ],
        github_languages={
            "Python": 3,
            "TypeScript": 2,
            "JavaScript": 2,
            "HTML": 1,
        },
        experience_level="advanced",
        availability=True,
        department="Computer Science",
        year=4,
        previous_projects=[
            "Built a full-stack inventory management system at internship",
            "Developed a real-time chat application with WebSockets",
        ],
    ),
    StudentProfile(
        id="stu-003",
        name="Priya Menon",
        email="priya.menon@university.edu",
        skills=["Python", "FastAPI", "MongoDB", "React", "Node.js"],
        interests=["Backend", "Database Design", "Cloud Computing"],
        github_username="priya-menon",
        github_repos=[
            "fastapi-crud",
            "mern-social",
            "cloud-deploy-demo",
            "api-gateway",
        ],
        github_languages={
            "Python": 3,
            "JavaScript": 2,
            "TypeScript": 1,
        },
        experience_level="intermediate",
        availability=True,
        department="Information Technology",
        year=3,
        previous_projects=[
            "Built a CRUD API using FastAPI with MongoDB",
            "Developed a MERN stack social media prototype",
        ],
    ),
    StudentProfile(
        id="stu-004",
        name="Arjun Singh",
        email="arjun.singh@university.edu",
        skills=["Java", "Spring Boot", "React", "MySQL", "REST APIs"],
        interests=["Enterprise Apps", "Microservices", "System Design"],
        github_username="arjun-singh-code",
        github_repos=[
            "spring-boot-ecommerce",
            "microservices-demo",
            "library-management",
            "spring-security-jwt",
        ],
        github_languages={
            "Java": 4,
            "JavaScript": 2,
            "SQL": 1,
        },
        experience_level="advanced",
        availability=False,
        department="Computer Science",
        year=4,
        previous_projects=[
            "Internship at a fintech company building microservices",
            "Built a library management system with Spring Boot",
        ],
    ),
    StudentProfile(
        id="stu-005",
        name="Neha Gupta",
        email="neha.gupta@university.edu",
        skills=[
            "Python",
            "Flask",
            "SQLite",
            "JavaScript",
            "HTML",
            "CSS",
            "Bootstrap",
        ],
        interests=["Web Development", "Frontend", "UI/UX"],
        github_username="neha-gupta-dev",
        github_repos=[
            "portfolio-website",
            "recipe-finder",
            "todo-app-vanilla",
            "landing-page-template",
        ],
        github_languages={
            "JavaScript": 3,
            "HTML": 2,
            "CSS": 2,
            "Python": 1,
        },
        experience_level="beginner",
        availability=True,
        department="Information Technology",
        year=2,
        previous_projects=[
            "Created a personal portfolio website",
            "Built a recipe finder app using vanilla JavaScript",
        ],
    ),
    StudentProfile(
        id="stu-006",
        name="Vikram Reddy",
        email="vikram.reddy@university.edu",
        skills=["Python", "Flask", "React", "MySQL", "Machine Learning"],
        interests=["AI/ML", "Data Science", "Web Apps"],
        github_username="vikram-reddy-ml",
        github_repos=[
            "ml-pipeline",
            "sentiment-analyzer",
            "flask-ml-api",
            "data-viz-dashboard",
        ],
        github_languages={
            "Python": 4,
            "JavaScript": 2,
            "Jupyter Notebook": 2,
        },
        experience_level="intermediate",
        availability=True,
        department="Computer Science (AI/ML)",
        year=3,
        previous_projects=[
            "Built an ML pipeline for sentiment analysis",
            "Developed a Flask API serving ML predictions",
        ],
    ),
    StudentProfile(
        id="stu-007",
        name="Sneha Kulkarni",
        email="sneha.kulkarni@university.edu",
        skills=["Node.js", "Express", "MongoDB", "React", "TypeScript"],
        interests=["Backend", "API Development", "Database"],
        github_username="sneha-kulkarni",
        github_repos=[
            "express-ecommerce",
            "mern-blog",
            "node-auth-boilerplate",
            "rest-api-templates",
        ],
        github_languages={
            "JavaScript": 3,
            "TypeScript": 2,
            "HTML": 1,
        },
        experience_level="intermediate",
        availability=True,
        department="Computer Science",
        year=3,
        previous_projects=[
            "Built an e-commerce backend with Node.js and Express",
            "Developed a blog platform with MERN stack",
        ],
    ),
    StudentProfile(
        id="stu-008",
        name="Aditya Verma",
        email="aditya.verma@university.edu",
        skills=["Go", "Python", "PostgreSQL", "Docker", "Kubernetes"],
        interests=["Cloud", "DevOps", "System Programming"],
        github_username="aditya-verma-dev",
        github_repos=[
            "go-microservice",
            "k8s-deployment",
            "cli-tools-go",
            "terraform-infra",
        ],
        github_languages={
            "Go": 3,
            "Python": 2,
            "HCL": 1,
        },
        experience_level="advanced",
        availability=False,
        department="Computer Science",
        year=4,
        previous_projects=[
            "Interned at a cloud startup working on Kubernetes deployments",
            "Built CLI tools in Go for DevOps automation",
        ],
    ),
]

# ── Seed Business Requests (for testing) ─────────────────────

from .models import BusinessRequest
from datetime import datetime


SEED_BUSINESS_REQUESTS = [
    BusinessRequest(
        id="br-001",
        business_name="BakeHouse Delights",
        owner_name="Mrs. Sharma",
        email="sharma@bakehouse.test",
        description="I run a small bakery and want a website where customers can browse our menu, place orders for pickup, and pay online. I also need an admin panel to manage orders.",
        status="submitted",
        created_at=datetime.now().isoformat(),
    ),
    BusinessRequest(
        id="br-002",
        business_name="GreenLeaf Organics",
        owner_name="Mr. Patel",
        email="patel@greenleaf.test",
        description="I sell organic vegetables and want a platform where customers can subscribe for weekly vegetable boxes. Need delivery tracking and payment integration.",
        status="submitted",
        created_at=datetime.now().isoformat(),
    ),
]


# ── In-memory Store ──────────────────────────────────────────

class InMemoryDB:
    """Simple in-memory database for development and prototyping."""

    def __init__(self):
        self.students: dict[str, StudentProfile] = {}
        self.business_requests: dict[str, BusinessRequest] = {}
        self.projects: dict[str, "Project"] = {}  # noqa: F821
        self._seed()

    def _seed(self):
        for s in STUDENTS:
            self.students[s.id] = s
        for br in SEED_BUSINESS_REQUESTS:
            self.business_requests[br.id] = br

    # ── Students ──

    def get_all_students(self) -> list[StudentProfile]:
        return list(self.students.values())

    def get_student(self, student_id: str) -> StudentProfile | None:
        return self.students.get(student_id)

    def get_available_students(self) -> list[StudentProfile]:
        return [s for s in self.students.values() if s.availability]

    def add_student(self, student: StudentProfile):
        self.students[student.id] = student

    def update_student(self, student_id: str, updates: dict) -> StudentProfile | None:
        student = self.students.get(student_id)
        if not student:
            return None
        updated = student.model_copy(update=updates)
        self.students[student_id] = updated
        return updated

    # ── Business Requests ──

    def get_all_requests(self) -> list[BusinessRequest]:
        return list(self.business_requests.values())

    def get_request(self, request_id: str) -> BusinessRequest | None:
        return self.business_requests.get(request_id)

    def add_request(self, req: BusinessRequest):
        self.business_requests[req.id] = req

    def update_request(self, request_id: str, updates: dict) -> BusinessRequest | None:
        req = self.business_requests.get(request_id)
        if not req:
            return None
        updated = req.model_copy(update=updates)
        self.business_requests[request_id] = updated
        return updated

    # ── Projects ──

    def get_all_projects(self) -> list["Project"]:  # noqa: F821
        return list(self.projects.values())

    def get_project(self, project_id: str):
        return self.projects.get(project_id)

    def add_project(self, project: "Project"):  # noqa: F821
        self.projects[project.id] = project

    def update_project(self, project_id: str, updates: dict):
        proj = self.projects.get(project_id)
        if not proj:
            return None
        updated = proj.model_copy(update=updates)
        self.projects[project_id] = updated
        return updated

    def get_projects_for_student(self, student_id: str) -> list:
        return [p for p in self.projects.values() if student_id in p.assigned_students]


# Singleton instance
db = InMemoryDB()


def get_students():
    return db.get_all_students()


def seed_students():
    return db.get_all_students()


def seed_business_requests():
    return db.get_all_requests()


def get_business_requests():
    return db.get_all_requests()
