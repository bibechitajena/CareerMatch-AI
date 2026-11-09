from django.db import models


class Job(models.Model):

    title = models.CharField(max_length=200)

    company = models.CharField(max_length=200)

    description = models.TextField()

    required_skills = models.JSONField(default=list)

    experience_level = models.CharField(max_length=100)

    location = models.CharField(max_length=150)

    job_url = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title