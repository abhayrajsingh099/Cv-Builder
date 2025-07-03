from django.db import models

# Create your models here.

class Profile(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    project_1 = models.TextField(max_length=500)
    project_2 = models.TextField(max_length=500)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.CharField(max_length=200)
    skills = models.TextField(max_length=2000)
    frameworks = models.TextField(max_length=2000,default="None")