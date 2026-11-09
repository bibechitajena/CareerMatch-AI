
import re
import PyPDF2

SKILLS_LIST = [
    "python", "java", "c++", "c",
    "django", "flask", "html", "css",
    "javascript", "react", "mysql",
    "sql", "mongodb", "machine learning",
    "deep learning", "data analysis",
    "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch", "git",
    "github", "excel", "power bi",
    "aws", "docker", "rest api",
    "communication", "leadership",
    "problem solving", "data structures",
    "algorithms", "spring boot"
]


def extract_resume_text(pdf_file):
    pdf_file.seek(0)

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    extracted_text = ""

    for page in pdf_reader.pages:
        extracted_text += page.extract_text() or ""

    pdf_file.seek(0)

    return extracted_text


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_LIST:
        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills
