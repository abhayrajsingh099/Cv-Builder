from django.db import models

# Create your models here.

class Profile(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    github = models.CharField(max_length=500)
    project_1 = models.TextField(max_length=500)
    project_2 = models.TextField(max_length=500)
    degree = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    university = models.CharField(max_length=500)
    previous_work = models.CharField(max_length=500)
    skills = models.TextField(max_length=2000)
    frameworks = models.TextField(max_length=2000,default="None")
