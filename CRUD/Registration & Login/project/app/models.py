from django.db import models

# Create your models here.

class Studentmodel(models.Model):
    stu_name= models.CharField(max_length=50)
    stu_email= models.CharField()
    stu_city= models.CharField(max_length=50)
    stu_mobile= models.CharField()
    stu_password= models.CharField(max_length=25)

