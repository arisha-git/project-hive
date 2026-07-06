from services.gemini_service import generate_prd


class RequirementsAgent:
    def run(self, description):
        print("Requirements Agent running...")
        return generate_prd(description)


class SolutionArchitectAgent:
    def run(self, prd):
        print("Solution Architect Agent running...")

        tech_stack = {
            "frontend": ["React", "Next.js"],
            "backend": ["FastAPI"],
            "database": ["PostgreSQL"],
            "ai": ["Gemini"]
        }

        return {
            "prd": prd,
            "tech_stack": tech_stack
        }


class QualityReviewAgent:
    def run(self, data):
        print("Quality Review Agent running...")

        data["quality_score"] = 96

        return data


class TalentScoutAgent:
    def run(self, data):
        print("Talent Scout Agent running...")

        data["recommended_team_size"] = 4

        return data


class AgentOrchestrator:

    def execute(self, description):

        prd = RequirementsAgent().run(description)

        architecture = SolutionArchitectAgent().run(prd)

        reviewed = QualityReviewAgent().run(architecture)

        result = TalentScoutAgent().run(reviewed)

        return result