# 🐝 ProjectHive

> **Building the future of AI-assisted collaboration between businesses and student innovators.**

ProjectHive is an AI-powered autonomous multi-agent platform that bridges the gap between small businesses and student developers.

A business owner simply describes their idea in natural language. ProjectHive automatically converts it into a structured project plan, recommends the ideal technology stack, matches the most suitable student team, monitors project progress, and adapts to changing requirements through intelligent AI agents.

Our goal is to help small businesses adopt digital solutions while giving students valuable real-world project experience.

---

# Problem Statement

Small businesses and non-profits often struggle to adopt digital tools such as e-commerce platforms, basic cybersecurity, and online business solutions because they lack technical expertise.

At the same time, Computer Science and IT students need real-world projects to build their portfolios and gain practical experience.

ProjectHive automates this entire process using an intelligent multi-agent system.

---

# Solution

ProjectHive acts as an AI consultancy that transforms simple business ideas into complete software projects.

Instead of manually coordinating between businesses, students, and university coordinators, ProjectHive autonomously:

- Understands business requirements
- Generates a structured project plan
- Recommends an appropriate technology stack
- Matches the most suitable student team
- Tracks project progress
- Handles requirement changes automatically

---

# AI Agents

## Requirements Engineer Agent

Converts business requirements written in plain English into a detailed Product Requirements Document (PRD).

Example:

Input:

> "I want customers to order cakes online."

Output:

- Functional Requirements
- Non-functional Requirements
- User Stories
- Project Deliverables
- Feature List

---

## Solution Architect Agent

Designs the technical solution by recommending:

- Frontend Framework
- Backend Technology
- Database
- APIs
- Authentication
- Third-party Integrations

---

## Quality Review Agent

Reviews the generated project before assignment.

Checks for:

- Missing requirements
- Timeline feasibility
- Scope completeness
- Missing user roles
- Project consistency

Also generates a **Project Readiness Score**.

---

## Talent Scout Agent

Matches students based on:

- Skills
- GitHub Profiles
- Technologies
- Interests
- Availability

---

## Project Pulse Agent

Continuously monitors project progress.

Tracks:

- Milestones
- Deadlines
- Weekly Updates
- Team Progress

---

## Conflict Resolution Agent

Handles unexpected changes such as:

- Client requirement updates
- Delayed milestones
- Scope changes
- Timeline adjustments

Automatically proposes revised plans for approval.

---

# Workflow

```text
Business Owner

        │

        ▼

Requirements Engineer Agent

        │

        ▼

Solution Architect Agent

        │

        ▼

Quality Review Agent

        │

        ▼

Talent Scout Agent

        │

        ▼

Project Pulse Agent

        │

        ▼

Conflict Resolution Agent
```

---

# Tech Stack

### Frontend

- Next.js
- React
- Tailwind CSS

### Backend

- FastAPI / Node.js

### AI

- Google Gemini API
- Google Agent Development Kit (ADK)

### Database

- PostgreSQL
- pgvector

### Cloud

- Google Cloud
- Vertex AI
- Cloud Run
- BigQuery (optional)

---

# Project Structure

```text
project-hive/
│
├── frontend/
│
├── backend/
│
├── prompts/
│
├── docs/
│
├── assets/
│
└── README.md
```

---

# Git Workflow

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Create Your Branch

### Arisha

```bash
git checkout -b arisha/frontend
```

### Sneha

```bash
git checkout -b sneha/backend
```

### Shubha

```bash
git checkout -b shubha/ai-agents
```

### Shreya

```bash
git checkout -b shreya/system
```

---

## 3. Commit Frequently

```bash
git add .

git commit -m "Describe your changes"
```

---

## 4. Push Your Branch

```bash
git push origin <branch-name>
```

Example:

```bash
git push origin arisha/frontend
```

---

## 5. Open a Pull Request

Do **NOT** push directly to the `main` branch.

Create a Pull Request and wait for it to be reviewed before merging.

---

# Team Responsibilities

## 👩‍💻 Arisha

- Git coordinator
- Frontend lead
- Product integration
- Final demo
- Merge everyone's work

---

## 👩‍💻 Sneha

- Backend APIs
- Database
- Matching Logic
- Data Models

---

## 👩‍💻 Shreya

- AI agents
- System architecture
- Gemini integration
- ADK workflow

---

## 👩‍💻 Shubha

- Prompt engineering
- Test datasets
- Documentation
- QA testing
- UI support

---

# Development Guidelines

- Always work on your own branch.
- Commit frequently.
- Pull the latest changes before starting new work.
- Keep commits small and meaningful.
- Open Pull Requests instead of pushing to `main`.
- Test your changes before requesting a merge.

---

# MVP Goal

By the end of the hackathon, ProjectHive should be able to:

- Accept a business idea in natural language.
- Generate a structured PRD.
- Recommend a technology stack.
- Match the most suitable student team.
- Create a project timeline.
- Handle project changes autonomously.

---

# Team

- **Arisha** — Frontend Developer & Git Coordinator
- **Sneha** — Backend Developer
- **Shubha** — AI Engineer
- **Shreya** — AI Engineer & System Architect

---

Built with ❤️ for the **Google Gen AI Academy APAC Hackathon 2026**.
