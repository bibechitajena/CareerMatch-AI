
def calculate_match(resume_skills, job_skills):

    # Convert skills into lowercase sets
    resume_skills = {
        skill.lower() for skill in resume_skills
    }

    job_skills = {
        skill.lower() for skill in job_skills
    }

    # Find matching and missing skills
    matched_skills = resume_skills.intersection(job_skills)

    missing_skills = job_skills.difference(resume_skills)

    # Calculate match percentage
    if len(job_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = round(
            (len(matched_skills) / len(job_skills)) * 100,
            2
        )

    return {
        "match_percentage": match_percentage,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }
