import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_prd(business_description: str):
    prompt = f"""
You are ProjectHive's Requirements Engineer AI.

Your job is to convert business ideas into professional software project requirements.

Business Description:
{business_description}

Generate:

# Project Overview

# Problem Statement

# Objectives

# Core Features

# Recommended Tech Stack

# Student Skills Required

# Estimated Timeline

# Deliverables

Rules:
- Keep the language professional.
- Maximum 500 words.
- Use markdown headings.
- Focus on practical implementation.
"""

    response = model.generate_content(prompt)
    return response.text