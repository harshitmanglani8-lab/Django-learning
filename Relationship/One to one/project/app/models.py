from django.db import models

# Create your models here.

class Aadharmodel(models.Model):
    adhar_no=models.IntegerField()

    def __str__(self):
        return str(self.adhar_no)

class Studentmodel(models.Model):
    name=models.CharField(max_length=100)
    aadhar_no=models.OneToOneField(Aadharmodel, on_delete=models.CASCADE)
# cascade srif adhar no delete karega
# protect pura data delete kar dega

    def __str__(self):
        return self.name
