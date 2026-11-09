from django.urls import path
from . import views

urlpatterns = [
    path('matches/', views.job_matches, name='job_matches'),
]