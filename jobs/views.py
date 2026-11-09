
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from resumes.models import Resume
from .models import Job
from .matching import calculate_match


@login_required
def job_matches(request):

    # Get the latest uploaded resume
    resume = Resume.objects.filter(
        user=request.user
    ).order_by('-uploaded_at').first()

    if not resume:
        return render(request, 'jobs/matches.html', {
            'error': 'Please upload your resume first.'
        })

    # Get all active jobs
    jobs = Job.objects.filter(is_active=True)

    matched_jobs = []

    # Compare resume skills with job requirements
    for job in jobs:

        result = calculate_match(
            resume.skills,
            job.required_skills
        )

        matched_jobs.append({
            'job': job,
            'match_percentage': result['match_percentage'],
            'matched_skills': result['matched_skills'],
            'missing_skills': result['missing_skills']
        })

    # Sort jobs from highest to lowest match
    matched_jobs.sort(
        key=lambda item: item['match_percentage'],
        reverse=True
    )

    # Dashboard statistics
    total_jobs = jobs.count()

    highest_match = (
        matched_jobs[0]['match_percentage']
        if matched_jobs else 0
    )

    context = {
        'matched_jobs': matched_jobs,
        'total_jobs': total_jobs,
        'analyzed_jobs': len(matched_jobs),
        'highest_match': highest_match,
        'resume_skills': resume.skills
    }

    return render(
        request,
        'jobs/matches.html',
        context
    )
