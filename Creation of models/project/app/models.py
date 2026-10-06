from django.db import models

# Create your models here.

class Studentmodel(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    City = models.CharField(max_length=200)
    Address = models.TextField()

class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Salary = models.CharField()
    City = models.CharField(max_length=100)

