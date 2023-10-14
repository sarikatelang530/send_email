from django.db import models

# Create your models here.

class Employee(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    work_anniversary = models.DateField()
    email = models.EmailField()