from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    previous_cgpa = models.FloatField()

    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class JobOffer(models.Model):
    salary = models.IntegerField()
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Offer: {self.salary} | Feedback: {self.feedback}"

