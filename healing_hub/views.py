from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Mentor
from .models import JobOffer
from .serializer import CourseSerializer, MentorSerializer
from rest_framework.decorators import api_view



class AddCourse(APIView):
    def post(self, request):
        course_name = request.data.get('name')
        previous_cgpa = request.data.get('prev_cgpa')
        if course_name and previous_cgpa:
            course = Course.objects.create(name=course_name, previous_cgpa=previous_cgpa)
            course.save()
            return Response({"study_plan": "Custom study plan created!"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid data!"}, status=status.HTTP_400_BAD_REQUEST)

class MentorList(APIView):
    def get(self, request):
        mentors = Mentor.objects.all()
        serializer = MentorSerializer(mentors, many=True)
        return Response(serializer.data)


class ValidateSalaryView(APIView):
    def post(self, request):
        salary = request.data.get("salary")

        if salary == 70000:
            return Response({"is_accepted": False, "message": " bhaag beta abul"}, status=status.HTTP_200_OK)
        else:
            job_offer = JobOffer.objects.create(salary=salary)
            return Response({"is_accepted": True, "message": " baba bolo, kobul"}, status=status.HTTP_200_OK)
class SubmitFeedbackView(APIView):
    def post(self, request):
        salary = request.data.get("salary")
        feedback = request.data.get("feedback")

        job_offer = JobOffer.objects.filter(salary=salary).first()
        if job_offer:
            job_offer.feedback = feedback
            job_offer.save()
            return Response({"message": "Feedback submitted successfully!"}, status=status.HTTP_200_OK)
        return Response({"message": "Offer not found!"}, status=status.HTTP_404_NOT_FOUND)



# TMDb API configurations
API_KEY = ''
BASE_URL = 'https://api.themoviedb.org/3'
import requests
def fetch_movies():
    url = f'{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres=18&sort_by=popularity.desc'
    response = requests.get(url)
    data = response.json()
    return data['results']

def movie_list(request):
    movies = fetch_movies()
    return render(request, 'movies.html', {'movies': movies})

from django.shortcuts import render
def home(request):
    return render(request, 'homei.html')

def todo(request):
    return render(request, 'todo.html')

def job_offer(request):
    return render(request, 'jobs.html')
    
def fun(request):
    return render(request, 'fun.html')

def skill(request):
    return render(request,'skill.html')


def meet(request):
    return render(request,'meet.html')
