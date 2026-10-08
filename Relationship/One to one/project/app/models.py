from django.db import models

# Create your models here.

class Aadharmodel():
    adhar_no=models.IntegerField()

    def __str__(self):
        return str(self.adhar_no)

class Studentmodel(models.Model):
    name=models.CharField(max_length=100)
    aadhar_no=models.OneToOneField(Aadharmodel)

    def __str__(self):
        return self.name
