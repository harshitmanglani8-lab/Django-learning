from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    City=models.CharField(max_length=100)

    def __str__(self):
        return self.Name
