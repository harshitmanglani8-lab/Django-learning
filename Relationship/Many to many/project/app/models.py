from django.db import models

# Create your models here.

fuel=(
    ("petrol","petrol")
    ("CNG","CNG")
    ("Diesel","Diesel")
)

class Fuelmodel(models.Model):
    fuel_type=models.CharField(max_length=100)

    def __str__(self):
        return self.fuel_type

cars=(
    ("Mercedes","Mercedes")
    ("BMW","BMW")
    ("Audi","Audi")
)

class Carmodel(models.Model):
    cars_name= models.CharField(max_length=50,choices=fuel)
    fuel_type=models.ManyToManyField(Fuelmodel)
