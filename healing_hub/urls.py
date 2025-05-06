from django.urls import path 
from .views import AddCourse, MentorList
from .views import ValidateSalaryView, SubmitFeedbackView

from . import views

urlpatterns = [
    path('api/add-course/', AddCourse.as_view(), name='add_course'),
    path('api/mentors/', MentorList.as_view(), name='mentor_list'),
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    path('job_offer/', views.job_offer, name='job_offer'),
    path('movie_list', views.movie_list, name='movie_list'),
    path('api/validate_salary/', ValidateSalaryView.as_view(), name='validate_salary'),
    path('api/submit_feedback/', SubmitFeedbackView.as_view(), name='submit_feedback'),
    path('fun/', views.fun, name='fun'),
    path('skill/', views.skill, name='skill'),
    path('meet/', views.meet, name='meet'),


]

