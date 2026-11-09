from matching import calculate_match

resume_skills = ["Python", "Django", "MySQL"]

job_skills = ["Python", "Django", "Java", "SQL"]

result = calculate_match(resume_skills, job_skills)

print(result)