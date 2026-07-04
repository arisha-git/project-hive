from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_students_endpoint_returns_seed_data():
    response = client.get("/students")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 3
    assert any(student["name"] == "Ananya Sharma" for student in data)


def test_business_request_creation_and_matching():
    response = client.post(
        "/business-requests",
        json={
            "business_name": "Bright Bakery",
            "owner_name": "Sara",
            "email": "sara@example.com",
            "description": "We need a website with online orders and admin tools.",
        },
    )
    assert response.status_code == 200
    created = response.json()
    assert created["business_name"] == "Bright Bakery"

    match_response = client.post(f"/business-requests/{created['id']}/match")
    assert match_response.status_code == 200
    matches = match_response.json()
    assert isinstance(matches, list)
    assert len(matches) > 0


def test_crud_flow_for_student_business_and_project():
    student_response = client.post(
        "/students",
        json={
            "name": "Maya Rao",
            "email": "maya@example.com",
            "skills": ["Python", "FastAPI"],
            "interests": ["Backend"],
            "github_username": "maya-dev",
            "department": "Computer Science",
            "year": 2,
            "previous_projects": ["API starter"],
        },
    )
    assert student_response.status_code == 200
    student_id = student_response.json()["id"]

    update_student = client.put(f"/students/{student_id}", json={"availability": False})
    assert update_student.status_code == 200
    assert update_student.json()["availability"] is False

    project_response = client.post(
        "/projects",
        json={
            "business_request_id": "br-001",
            "title": "Bakery website",
            "description": "Launch storefront and orders",
            "assigned_students": [student_id],
            "tech_stack": {"frontend": "Next.js"},
        },
    )
    assert project_response.status_code == 200
    project_id = project_response.json()["id"]
    assert project_response.json()["milestones"][0]["name"] == "Initial planning"

    delete_project = client.delete(f"/projects/{project_id}")
    assert delete_project.status_code == 200

    delete_student = client.delete(f"/students/{student_id}")
    assert delete_student.status_code == 200

