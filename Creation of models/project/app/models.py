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

class Cybrom (models.Model):
    Name = models.CharField(max_length=100 ,verbose_name='cybrom_emp') 
    description = models.TextField()
    age = models.IntegerField()
    price = models.FloatField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    contact = models.IntegerField(null=True)
    # Date and time fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dob = models.DateField
    # Boolean field
    is_active = models.BooleanField(default=True)
    #Special fields
    email = models.EmailField(unique=True)
    website = models.URLField()
    slug = models.SlugField

    def __str__(self):
        return self.Name

    class Meta:
        ordering=['Name'] #order the name by ABCD
        verbose_name_plural = 'Cybrom'
