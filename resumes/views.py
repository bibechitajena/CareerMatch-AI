
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Resume
from .utils import extract_skills


@login_required
def upload_resume(request):

    if request.method == 'POST':

        if 'resume' not in request.FILES:
            messages.error(request, "Please select a resume.")
            return redirect('upload_resume')

        resume_file = request.FILES['resume']

        if not resume_file.name.lower().endswith('.pdf'):
            messages.error(request, "Please upload a PDF file.")
            return redirect('upload_resume')

        try:
            import PyPDF2

            pdf_reader = PyPDF2.PdfReader(resume_file)

            extracted_text = ""

            for page in pdf_reader.pages:
                extracted_text += page.extract_text() or ""

            if not extracted_text.strip():
                messages.error(request, "No readable text found in this PDF.")
                return redirect('upload_resume')

            skills = extract_skills(extracted_text)

            resume = Resume.objects.create(
                user=request.user,
                file=resume_file,
                extracted_text=extracted_text,
                skills=skills
            )

            messages.success(
                request,
                "Resume analyzed successfully!"
            )

            return render(request, 'resumes/result.html', {
                'resume': resume,
                'skills': skills
            })

        except Exception as e:
            messages.error(request, f"Resume processing failed: {e}")

    return render(request, 'resumes/upload.html')
