from django.db import models

# Create your models here.
class Departmentmodel(models.Model):
    depart_name = models.CharField(max_length=100)

    def __str__(self):
        return self.depart_name

class Studentdepartmodel(models.Model):
    stu_name = models.CharField(max_length=50)
    depart_name = models.ForeignKey(Departmentmodel, on_delete=models.CASCADE)
