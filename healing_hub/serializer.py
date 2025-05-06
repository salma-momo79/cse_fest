from rest_framework import serializers
from .models import Course, Mentor
from .models import JobOffer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'previous_cgpa']

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['id', 'name', 'expertise', 'bio']

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = ['salary', 'feedback', 'created_at']
